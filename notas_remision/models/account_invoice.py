# -*- coding: utf-8 -*-

from odoo import api
from odoo import models
from odoo import fields
from odoo.exceptions import UserError

   
class FacturasRemision(models.Model):
    _inherit = 'account.invoice'
    
    x_solo_nota_remision = fields.Boolean(
                                          string="Solo crear Nota",
                                          default=True
                                          )

    @api.multi
    def invoice_validate(self):
        '''Generates the cfdi attachments for mexican companies when validated.'''
        result = super(FacturasRemision, self).invoice_validate()
        if self.x_solo_nota_remision==True:
            result=None
            print("Solo remision")
        else:
            version = self.l10n_mx_edi_get_pac_version()
            for record in self.filtered(lambda r: r.l10n_mx_edi_is_required()):
                if record.type == 'out_refund' and (
                    record.refund_invoice_id and not record.refund_invoice_id.l10n_mx_edi_cfdi_uuid):
                    record.message_post(
                        body='<p style="color:red">' + _(
                            'The invoice related has no valid fiscal folio. For this '
                            'reason, this refund didn\'t generate a fiscal document.') + '</p>',
                        subtype='account.mt_invoice_validated')
                    continue
                record.l10n_mx_edi_cfdi_name = ('%s-%s-MX-Invoice-%s.xml' % (
                    record.journal_id.code, record.number, version.replace('.', '-'))).replace('/', '')
                subscription = 'subscription_id' in record.invoice_line_ids._fields and record.invoice_line_ids.filtered(
                    'subscription_id')
                ctx = {}
                if subscription:
                    ctx = {'disable_after_commit': True}
                record.with_context(**ctx)._l10n_mx_edi_retry()
        return result
        
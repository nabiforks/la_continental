# -*- coding: utf-8 -*-

from odoo import api
from odoo import models
from odoo import fields
from odoo.exceptions import UserError

   
class PagosRemision(models.Model):
    _inherit = 'account.payment'

    x_solo_nota_remision = fields.Boolean(string='solo nota de remision',
                        related='invoice_ids.x_solo_nota_remision')
    
    @api.multi
    def post(self):
        """Generate CFDI to payment after that invoice is paid"""
        res = super(PagosRemision, self.with_context(
            l10n_mx_edi_manual_reconciliation=False)).post()
        if self.x_solo_nota_remision==True:
            print("solo crear nota remision")
        else:
            for record in self.filtered(lambda r: r.l10n_mx_edi_is_required()):
                record.l10n_mx_edi_cfdi_name = ('%s-%s-MX-Payment-10.xml' % (
                    record.journal_id.code, record.name))
                record._l10n_mx_edi_retry()
        return res
        
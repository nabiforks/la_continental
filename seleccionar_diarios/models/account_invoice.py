# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

   
class DiarioNotaRemision(models.Model):
    _inherit = 'account.invoice'
    
    journal_id = fields.Many2one(
                                 'account.journal',
                                 string="Diario",
                                 compute='_get_diario',
                                 store=True
                                 )

    # -*- coding: utf-8 -*-

from datetime import date
from odoo import api
import datetime
from odoo import models
from odoo.exceptions import UserError
import math

   
class PagosBonificacion(models.Model):
    _inherit = 'account.invoice'
    
    @api.multi
    def action_invoice_open(self):
        self.env.cr.commit()
        print ("En ACTION INVOICE_OPEN==")
        if self.x_solo_nota_remision == True:
            diario_registro = self.env['diario.nota.remision'].search([], limit=1)
            for record in self.invoice_line_ids:
                record.account_id = diario_registro.diario_remision.default_debit_account_id.id
        return super(PagosBonificacion, self).action_invoice_open()
                                     
    
    @api.onchange('x_solo_nota_remision')
    def _get_diario(self):
        diario_registro = self.env['diario.nota.remision'].search([], limit=1)
#        if len(diario_registro) != 1:
#            raise ValidationError('El número de registros en la configuración de diarios debe ser 1')
        if self.x_solo_nota_remision == True:
            self.journal_id = diario_registro.diario_remision.id
        else:
            self.journal_id = diario_registro.diario_facturas.id
            
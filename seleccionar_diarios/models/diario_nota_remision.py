# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class SeccionNivel(models.Model):
    _name = 'diario.nota.remision'
    _description = 'Seleccion del diario para notas de remision'

    name = fields.Char(string = 'Nombre', default = 'Configuracion Diarios')
    diario_remision = fields.Many2one(
                           comodel_name='account.journal'
                           , string='Diario para nota de remisión'
                           , required=True
                           )
                           
    diario_facturas = fields.Many2one(
                           comodel_name='account.journal'
                           , string='Diario para facturas'
                           , required=True
                           )
                           
    company_id = fields.Many2one(
                                 comodel_name='res.company'
                                 , string='Company'
                                 , required=True
                                 , default=lambda self: self.env.user.company_id
                                 )
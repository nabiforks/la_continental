# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class VehiculoCompatible(models.Model):
    _name='vehiculo.compatible'
    _description='Modelo para asociar vehiculos con productos'

    name = fields.Char(
                        string="Vehículo"
                        )
    #vehiculo_compatible=fields.Many2one(
    #    'product.template',
    #    string= 'Vehículo'
    #)
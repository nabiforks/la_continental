# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class ProductoVehiculo(models.Model):
    _inherit = 'product.template'

    x_vehiculos_compatible = fields.Many2many(
                                         'vehiculo.compatible',
                                        # 'vehiculo_compatible',
                                         string="Vehículos compatibles"
                                         )

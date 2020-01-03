# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api
# modelo de campos a editar desde factura borrados
class editable(models.Model):
	_inherit='fleet.vehicle'


	x_numero_unidad = fields.Char(string="numero de unidad")
	# x_porcentaje_combustible=fields.Selection(selection=[
 #                                                    ('G01', 'Adquisición de mercancías'), 
 #                                                    ('G02', 'Devoluciones, descuentos o bonificaciones'),
 #                                                    ('P01', 'por definir')
 #                                                    ],
 #                                                    compute='_compute_uso',
 #                                                    store=True, 
 #                                                    track_visibility='onchange',
 #                                                    )

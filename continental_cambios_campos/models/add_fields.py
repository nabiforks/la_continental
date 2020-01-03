# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api
# modelo de campos a editar desde factura borrados
class vista_lista(models.Model):
	_inherit='fleet.vehicle'

	porcentaje_combustible = fields.Selection(selection=[('01','1/4'),
		('02','1/2'),
		('03','3/4'),('04','LLENO'),],
		)


   	
	# @api.one
	# @api.depends('fleet_repair_line')
	# def _compute_vista(self):
	# 	for order in self:
	# 		print(order.fleet_repair_line.license_plate)
	# 		order.license_plate=order.fleet_repair_line.license_plate


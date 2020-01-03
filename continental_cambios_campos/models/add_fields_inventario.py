# -*- coding:utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api
# modelo de campos a editar desde factura borrados
class vista_lista(models.Model):
	_inherit='product.template'


	compatibleV=fields.Char(compute='_compute_compatible_vehiculo')
	# campatible=fields.Char()



	
	@api.multi #metodo calculado para concatenar las opciones de los carros que estan compatibles
	@api.depends('name')
	def _compute_compatible_vehiculo(self):
		print("hola entraste en el depends")
		for order in self:
			#print(order.x_vehiculos_compatible)
			order.compatibleV=" "
			for v in order.x_vehiculos_compatible:
				#print(v.name)
				# order.campatible=v.name+", "+order.campatible
				order.compatibleV=v.name+", "+order.compatibleV
			print("hola")
			print(order.compatibleV)

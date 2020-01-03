# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = "product.template"

    product_vehicle = fields.Char(compute='_get_product_vehicle', string='Vehiculos')

    def _get_product_vehicle(self):
        for record in self:
            product_vehicle_text = ''
            product_id = self.env['product.product'].sudo().search([('product_tmpl_id', '=', record.id)])
            if product_id:
                for v in product_id.x_vehiculos_compatible:
                    product_vehicle_text = product_vehicle_text + v.name + ','
                record.product_vehicle = product_vehicle_text

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ClientSaleReference(models.Model):
    _inherit = 'account.invoice'

    x_ref_client = fields.Char(string='No. Orden')

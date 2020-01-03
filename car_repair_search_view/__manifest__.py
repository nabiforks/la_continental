# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "Car Repair/Maintenance Management Odoo/OpenERP",
    "version" : "12.0.0.3",
    "depends" : ['base', 
                'sale', 
                'purchase', 
                'account', 
                'sale_stock', 
                'mail', 
                'product', 
                'stock', 
                'fleet',
                'sale_management'],
    "author": "Soluciones4G",
    "description": """
    BrowseInfo developed a new odoo/OpenERP module apps.
    """,
    'category': 'Industries',

    "data" :[
        'views/car_repair_search_view.xml',
    ]
}
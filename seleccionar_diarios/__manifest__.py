# -*- coding: utf-8 -*-
{
    'name': "seleccionar_diarios",

    'summary': """
        Configurar diario para notas de remisión
        """,

    'description': """
        Configurar diario para notas de remisión
    """,

    'author': "Soluciones4G",
    'website': "http://soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
    'account_accountant',
    'account',],
    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'views/seleccionar_diario_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}
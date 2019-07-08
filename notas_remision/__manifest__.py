# -*- coding: utf-8 -*-
{
    'name': "notas_remision",

    'summary': """
        Permite generar notas de remisión
        """,

    'description': """
        Permite generar notas de remisión
    """,

    'author': "Soluciones4G",
    'website': "solucoines4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Extras',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
    'l10n_mx_edi',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/nota_remision.xml',
        'views/nota_remision_qweb.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
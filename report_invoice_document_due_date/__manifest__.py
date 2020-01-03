# -*- coding: utf-8 -*-
{
    'name': "Ocultar vencimiento",

    'summary': """
        Oculta la fecha de vencimiento del PDF de factura""",

    'description': """
        Oculta la fecha de vencimiento del PDF de factura
    """,

    'author': "Soluciones 4G",
    'website': "http://www.soluciones4g.com",

    
    'category': 'Report',
    'version': '0.1',

    
    'depends': ['base', 'account', 'account_accountant',],

    
    'data': [
        'views/views.xml',
    ],
    
}
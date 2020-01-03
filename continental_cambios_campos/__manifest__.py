# -*- coding: utf-8 -*-
{
    'name': "Modificación de campos, taller mécanico",
    'description': """
       Modificación de campos en diferentes módulos de flota y car repair.
    """,
    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    'depends': [
                'base',
                'fleet',
                'car_repair_industry',
                
                ],
    'data': [
       #'views/vista_flota_mod.xml',
        'views/inventario.xml',
       # 'views/ventas_fields.xml',
       # 'views/atani_add_modelo.xml',
       #vistas de ventas con fields

        ],
    'installable':True,
    'auto_install':False,
}

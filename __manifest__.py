# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',

    'summary': """App to do simple accounting """,

    'description': """
        Training Module    
    """,
    'author': 'Hinamizawa',

    'website': 'https://www.odoo.com',

    'category': 'Training',

    'version': '14.0.0',

    'depends': ['base'],

    'data': [
        'odoo_academy/security/academy_security.xml',
        'odoo_academy/security/ir.model.access.csv',

    ],
    'demo': [
        'odoo_academy/demo/academy_demo.xml',

    ],

}

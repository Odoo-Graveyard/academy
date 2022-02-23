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
        'security/academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_demo.xml',

    ],
}

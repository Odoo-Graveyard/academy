# -*- coding: utf-8 -*-

{
    'name': 'Odoo Academy',

    'summary': """App to do simple accounting """,

    'description': """
        Training Module
        - level
        - Training
        - Interactive
    
    """,
    'author': 'Hinamizawa',

    'website': 'https://www.odoo.com',

    'category': 'Training',

    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/academy_security.xml',
        'security/ir.model.access.csv',

    ],
    'demo': [
            'demo/academy_demo.xml',

    ],

}

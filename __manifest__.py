# -*- coding: utf-8 -*-
{
    'name': "DietMeal",

    'summary': """
        add diet meals data for users""",

    'description': """
        add diet meals data for users
    """,

    'author': "Loai N Kanou",
    'website': "http://loai.xyz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Products Extra Diets',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'pos_sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
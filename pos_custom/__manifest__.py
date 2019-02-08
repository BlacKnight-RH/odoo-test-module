# -*- coding: utf-8 -*-
{
    'name': "My Custom POS",

    'summary': """
        woooh ooo ooo ooo Ma-Ma waaaah, in the jungle the mighty jungle, the lion sleeps tonight""",

    'description': """
        in the jungle the mighty jungle, the lion sleeps tonight
    """,

    'author': "Mahmoud Magdy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'POS',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
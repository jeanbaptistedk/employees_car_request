# -*- coding: utf-8 -*-
{
    'name': "Employees Car request",

    'summary': """
        Request a car, gey the approval""",

    'description': """
        Long description of module's purpose
    """,

    'author': "KARBOU Déhen Jean-Baptiste",
    'website': "http://newbrainfactory.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'fleet',],

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
}
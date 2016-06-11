# -*- coding: utf-8 -*-
{
    'name': "Builder",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'project', 'purchase', 'account', 'account_analytic_default','hr_expense', 'sale', 'ncf_purchase', 'product',
                'hr', 'hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/purchase_view.xml',
        'views/templates.xml',
        'views/account_view.xml',
        'views/cubage_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
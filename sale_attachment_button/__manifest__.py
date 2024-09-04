# -*- coding: utf-8 -*-
{
    'name': 'Sales Order Attachment Button',

    'version': '1.0',
    'summary': 'Adds an attachment button to Sales Order form',
    'description': 'This module adds a button to the Sales Order form to view attachments related to the sales order.',

    'author': "Ghiglione Pedro Matias",
    'website': "https://quimerasoftware.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move_views.xml',
        'views/account_payment_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
    ],
}

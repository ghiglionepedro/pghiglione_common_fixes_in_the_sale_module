# -*- coding: utf-8 -*-
{
    'name': 'sale_import_excel',

    'version': '1.0',
    'summary': '',
    'description': '',

    'author': "Ghiglione Pedro Matias",
    'website': "https://quimerasoftware.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [              # Dependencia para Sales Order
        'dusal_sale',                  # Dependencia para Stock Picking
    ],
    'data': [
        'views/sale_order_views.xml',
    ],
}

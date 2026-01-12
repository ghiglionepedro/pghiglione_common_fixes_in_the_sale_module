{
    'name': 'Partner Origin Type',
    'version': '16.0.1.0.0',
    'category': 'Sales',
    'summary': 'Adds customer origin type to partners and sale orders',
    'author': 'Quimera Software',
    'depends': ['sale', 'contacts'],
    'data': [
        'views/res_partner_view.xml',
        'views/sale_order_view.xml',
    ],
    'installable': True,
    'application': False,
}

{
    "name": "Remito Manual en Inventario",
    "version": "16.0.1.0.0",
    "category": "Inventory",
    "summary": "Agrega el campo Remito Manual en remitos y lo muestra en Ventas",
    "author": "Quimera Software",
    "depends": ["stock", "sale_stock"],
    "data": [
        "views/stock_picking_view.xml",
        "views/sale_order_view.xml",
    ],
    "installable": True,
    "application": False,
}
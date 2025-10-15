{
    "name": "Restricción de Establecer Ajustes de Inventario",
    "version": "16.0.1.0.0",
    "author": "Quimera Software",
    "website": "https://quimerasoftware.com",
    "category": "Inventory",
    "summary": "Restringe el botón 'Establecer cantidad en mano' solo a usuarios autorizados.",
    "depends": ["stock"],
    "data": [
        "security/restrict_inventory_group.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}

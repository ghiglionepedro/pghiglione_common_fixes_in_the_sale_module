from odoo import models, fields, _
from odoo.exceptions import UserError
import base64
import pandas as pd
from io import BytesIO

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    excel_file = fields.Binary(string="Archivo Excel")
    file_name = fields.Char(string="Nombre del Archivo")

    def action_import_products_from_excel(self):
        # Verifica si se cargó el archivo
        if not self.excel_file:
            raise UserError(_("Por favor, sube un archivo de Excel antes de continuar."))

        # Convierte el archivo en un DataFrame de pandas para leer el contenido
        file_content = base64.b64decode(self.excel_file)
        excel_data = pd.read_excel(BytesIO(file_content), engine='openpyxl')
        
        # los códigos de producto están en la columna "D" 
        reference_codes = excel_data.iloc[:, 3].dropna()  # Columna D (cero indexada)

        # Variable para el producto "VARIOS" (puedes crear un producto específico si prefieres)
        varios_product = self.env['product.product'].search([('name', '=', '-')], limit=1)
        
        if not varios_product:
            raise UserError(_("Por favor, crea un producto con nombre '-' para los productos no reconocidos."))

        for code in reference_codes:
            # Busca el producto por código de referencia
            product = self.env['product.product'].search([('default_code', '=', code)], limit=1)
            
            if not product:
                # Si no se encuentra el producto, usa "-"
                product = varios_product

            # Agrega la línea del producto al pedido
            self.order_line.create({
                'order_id': self.id,
                'product_id': product.id,
                'name': product.name,
                'product_uom_qty': 1.0,  # Cantidad (ajustable según necesidades)
                'price_unit': product.lst_price,  # Precio de lista del producto
            })

        return True
from odoo import models, fields, _
from odoo.exceptions import UserError
import base64
from openpyxl import load_workbook  # Para archivos .xlsx
from io import BytesIO

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    excel_file = fields.Binary(string="Archivo Excel para cargar presupuesto")
    file_name = fields.Char(string="Nombre del Archivo")

    def action_import_products_from_excel(self):
        # Verifica si se cargó el archivo
        if not self.excel_file:
            raise UserError(_("Por favor, sube un archivo de Excel antes de continuar."))

        # Convierte el archivo a BytesIO y abre el archivo con openpyxl
        file_content = base64.b64decode(self.excel_file)
        workbook = load_workbook(filename=BytesIO(file_content), data_only=True)
        sheet = workbook.active

        # Variable para el producto "VARIOS" (asegúrate de tener un producto con este código)
        varios_product = self.env['product.product'].search([('name', '=', '-')], limit=1)
        
        if not varios_product:
            raise UserError(_("Por favor, crea un producto con código '-' para los productos no reconocidos."))

        # Procesar cada fila de la hoja de cálculo, comenzando en la fila 2 para omitir el encabezado
        for row in range(13, sheet.max_row + 1):
            # Lee la columna C para la cantidad, verificando que sea un número
            quantity = sheet.cell(row=row, column=3).value
            if not isinstance(quantity, (int, float)):
                quantity = 1.0  # Asigna un valor por defecto si no es numérico

            # Lee la columna D para el código de referencia
            code = sheet.cell(row=row, column=4).value
            if not code:
                continue  # Si no hay código de producto, salta esta fila
            
            # Lee la columna H para el importe por unidad, verificando que sea un número
            unit_price = sheet.cell(row=row, column=8).value
            if not isinstance(unit_price, (int, float)):
                unit_price = 0.0  # Asigna un valor por defecto si no es numérico

            # Busca el producto por su código de referencia
            product = self.env['product.product'].search([('default_code', '=', code)], limit=1)
            
            if not product:
                # Si no se encuentra el producto, usa "VARIOS"
                product = varios_product

            # Agrega la línea del producto al pedido con la cantidad y precio extraídos
            self.order_line.create({
                'order_id': self.id,
                'product_id': product.id,
                'name': product.name,
                'product_uom_qty': quantity,  # Cantidad de la columna C
                'price_unit': unit_price,  # Precio unitario de la columna H
            })

        return True
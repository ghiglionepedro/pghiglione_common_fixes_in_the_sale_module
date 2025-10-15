from odoo import models, fields

class StockQuant(models.Model):
    _inherit = "stock.quant"

    product_image = fields.Image(
        string="Imagen del producto",
        related="product_id.image_1920",
        readonly=True,
    )
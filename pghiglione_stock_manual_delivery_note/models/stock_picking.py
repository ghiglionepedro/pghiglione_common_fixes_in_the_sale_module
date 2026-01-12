from odoo import models, fields

class StockPicking(models.Model):
    _inherit = "stock.picking"

    manual_delivery_note = fields.Char(
        string="Remito Manual",
        help="Número de remito físico"
    )

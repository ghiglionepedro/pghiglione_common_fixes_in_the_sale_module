from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    manual_delivery_note_ids = fields.One2many(
        "stock.picking",
        "sale_id",
        string="Remitos Manuales",
        domain=[("manual_delivery_note", "!=", False)]
    )

    manual_delivery_notes = fields.Char(
        string="Remitos Manuales",
        compute="_compute_manual_delivery_notes",
        store=True
    )

    @api.depends("picking_ids.manual_delivery_note")
    def _compute_manual_delivery_notes(self):
        for order in self:
            notes = order.picking_ids.filtered(
                lambda p: p.manual_delivery_note
            ).mapped("manual_delivery_note")

            order.manual_delivery_notes = ", ".join(notes)
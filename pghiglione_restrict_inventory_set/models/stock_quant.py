from odoo import models, api
from odoo.exceptions import UserError

class StockQuant(models.Model):
    _inherit = "stock.quant"

    @api.model
    def action_apply_inventory(self):
        user = self.env.user
        if not user.has_group("restrict_inventory_set.group_can_apply_inventory"):
            raise UserError("No tiene permisos para establecer ajustes de inventario.")
        return super().action_apply_inventory()

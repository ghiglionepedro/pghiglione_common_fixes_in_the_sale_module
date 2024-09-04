from odoo import models

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_view_attachments(self):
        self.ensure_one()

        # IDs de ventas relacionadas
        related_sale_order_ids = self.invoice_line_ids.mapped('sale_line_ids.order_id').ids
        # IDs de movimientos de stock relacionados
        related_picking_ids = self.invoice_line_ids.mapped('sale_line_ids.order_id.picking_ids').ids
        # IDs de pagos relacionados
        related_payment_ids = self.payment_id.ids
        
        domain = [
            '|', '|', '|',
            ('res_model', '=', 'account.move'),
            ('res_model', '=', 'sale.order'),
            ('res_model', '=', 'stock.picking'),
            ('res_model', '=', 'account.payment'),
            ('res_id', 'in', [self.id] + related_sale_order_ids + related_picking_ids + related_payment_ids)
        ]

        return {
            'name': 'Attachments',
            'type': 'ir.actions.act_window',
            'view_mode': 'tree,form',
            'res_model': 'ir.attachment',
            'domain': domain,
            'context': dict(self._context),
            'target': 'new',
        }

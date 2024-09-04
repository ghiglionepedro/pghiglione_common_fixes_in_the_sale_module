from odoo import models

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_view_attachments(self):
        self.ensure_one()
        
        # IDs de facturas relacionadas
        related_invoice_ids = self.move_id.id and [self.move_id.id] or []
        # IDs de ventas relacionadas
        related_sale_order_ids = self.move_id.invoice_line_ids.mapped('sale_line_ids.order_id').ids
        # IDs de movimientos de stock relacionados
        related_picking_ids = self.move_id.invoice_line_ids.mapped('sale_line_ids.order_id.picking_ids').ids
        
        domain = [
            '|', '|', '|',
            ('res_model', '=', 'account.payment'),
            ('res_model', '=', 'account.move'),
            ('res_model', '=', 'sale.order'),
            ('res_model', '=', 'stock.picking'),
            ('res_id', 'in', [self.id] + related_invoice_ids + related_sale_order_ids + related_picking_ids)
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
from odoo import models

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_view_attachments(self):
        self.ensure_one()

        related_sale_order_ids = self.invoice_line_ids.mapped('sale_line_ids.order_id').ids
        related_payment_ids = self.payment_id.ids
        related_payment_group_ids = self.payment_group_id.ids
        related_picking_ids = self.invoice_line_ids.mapped('sale_line_ids.order_id.picking_ids').ids

        domain = [
            '|', '|', '|', '|',
            (('res_model', '=', 'account.move'), ('res_id', 'in', [self.id]))
            (('res_model', '=', 'sale.order'), ('res_id', 'in', [related_sale_order_ids]))
            (('res_model', '=', 'account.payment'), ('res_id', 'in', [related_payment_ids]))
            (('res_model', '=', 'account.payment.group'), ('res_id', 'in', [related_payment_group_ids]))
            (('res_model', '=', 'stock.picking'), ('res_id', 'in', [related_picking_ids]))
        ]

        return {
            'name': 'Attachments',
            'type': 'ir.actions.act_window',
            'view_mode': 'kanban,form',
            'res_model': 'ir.attachment',
            'domain': domain,
            'context': dict(self._context),
            'target': 'new',
        }

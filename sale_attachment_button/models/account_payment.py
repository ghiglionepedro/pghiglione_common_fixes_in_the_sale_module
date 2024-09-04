from odoo import models

class AccountPayment(models.Model):
    _inherit = 'account.payment'

class AccountPayment(models.Model):
    _inherit = 'account.payment'

    def action_view_attachments(self):
        self.ensure_one()

        related_invoice_ids = self.move_id.id and [self.move_id.id] or []
        related_sale_order_ids = self.move_id.invoice_line_ids.mapped('sale_line_ids.order_id').ids
        related_picking_ids = self.move_id.invoice_line_ids.mapped('sale_line_ids.order_id.picking_ids').ids
        related_payment_group_ids = self.move_id.mapped('payment_group_id').ids

        domain = [
            '|', '|', '|', '|',
            ('res_model', '=', 'account.payment'),
            ('res_model', '=', 'account.move'),
            ('res_model', '=', 'sale.order'),
            ('res_model', '=', 'account.payment.group'),
            ('res_model', '=', 'stock.picking'),
            ('res_id', 'in', [self.id] + related_invoice_ids + related_sale_order_ids + related_picking_ids + related_payment_group_ids)
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
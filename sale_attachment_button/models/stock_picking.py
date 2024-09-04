from odoo import models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_view_attachments(self):
        self.ensure_one()

        related_sale_order_ids = self.sale_id.ids
        related_invoice_ids = self.sale_id.invoice_ids.ids
        related_payment_ids = self.sale_id.invoice_ids.mapped('payment_id').ids
        related_payment_group_ids = self.sale_id.invoice_ids.mapped('payment_group_id').ids

        domain = [
            '|', '|', '|', '|',
            ('res_model', '=', 'stock.picking'),
            ('res_model', '=', 'sale.order'),
            ('res_model', '=', 'account.move'),
            ('res_model', '=', 'account.payment'),
            ('res_model', '=', 'account.payment.group'),
            ('res_id', 'in', [self.id] + related_sale_order_ids + related_invoice_ids + related_payment_ids + related_payment_group_ids)
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

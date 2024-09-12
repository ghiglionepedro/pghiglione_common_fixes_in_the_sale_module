from odoo import models

class AccountPaymentGroup(models.Model):
    _inherit = 'account.payment.group'

    def action_view_attachments(self):
        self.ensure_one()

        related_payment_ids = self.payment_ids.ids
        related_invoice_ids = self.payment_ids.mapped('move_id').ids
        related_sale_order_ids = self.payment_ids.mapped('move_id.invoice_line_ids.sale_line_ids.order_id').ids
        related_picking_ids = self.payment_ids.mapped('move_id.invoice_line_ids.sale_line_ids.order_id.picking_ids').ids

        domain = [
            '|', '|', '|', '|',
            '&',('res_model', '=', 'account.payment.group'), ('res_id', 'in', [self.id]),
            '&',('res_model', '=', 'account.payment'),('res_id', 'in', [related_payment_ids]),
            '&',('res_model', '=', 'account.move'),('res_id', 'in', [related_invoice_ids]),
            '&',('res_model', '=', 'sale.order'),('res_id', 'in', [related_sale_order_ids]),
            '&',('res_model', '=', 'stock.picking'),('res_id', 'in', [related_picking_ids]),
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
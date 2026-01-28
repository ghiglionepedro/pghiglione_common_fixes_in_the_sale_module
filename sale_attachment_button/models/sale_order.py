from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_view_attachments(self):
        self.ensure_one()

        related_invoice_ids = self.invoice_ids.ids
        related_payment_ids = self.invoice_ids.mapped('payment_id').ids
        related_payment_group_ids = self.invoice_ids.mapped('payment_group_id').ids
        related_picking_ids = self.picking_ids.ids

        domain = [
            '|', '|', '|', '|',
            '&',('res_model', '=', 'sale.order'),('res_id', 'in', [self.id]),
            '&',('res_model', '=', 'account.move'),('res_id', 'in', [related_invoice_ids]),
            '&',('res_model', '=', 'account.payment'),('res_id', 'in', related_payment_ids),
            '&',('res_model', '=', 'account.payment.group'),('res_id', 'in', related_payment_group_ids),
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
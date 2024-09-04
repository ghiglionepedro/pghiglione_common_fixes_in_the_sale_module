from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_view_attachments(self):
        self.ensure_one()
        
        # IDs de las facturas, pagos, y movimientos de stock relacionados
        related_invoice_ids = self.invoice_ids.ids
        related_payment_ids = self.invoice_ids.mapped('payment_id').ids
        related_picking_ids = self.picking_ids.ids

        # Crear el dominio para buscar los adjuntos relacionados
        domain = [
            '|', '|', '|',
            ('res_model', '=', 'sale.order'),
            ('res_model', '=', 'account.move'),
            ('res_model', '=', 'account.payment'),
            ('res_model', '=', 'stock.picking'),
            ('res_id', 'in', [self.id] + related_invoice_ids + related_payment_ids + related_picking_ids)
        ]
        
        # Abrir la vista de adjuntos filtrada
        return {
            'name': 'Attachments',
            'type': 'ir.actions.act_window',
            'view_mode': 'kanban,form',
            'res_model': 'ir.attachment',
            'domain': domain,
            'context': dict(self._context),
            'target': 'new',
        }
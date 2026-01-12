import re
from odoo import models, api, _
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = "account.move"

    @api.constrains("move_name", "journal_id")
    def _check_move_name_afip_format(self):
        for move in self:
            if not move.move_name:
                continue

            # Solo validar diarios AFIP
            journal = move.journal_id
            if not journal.l10n_ar_afip_pos_id:
                continue

            # Solo facturas de venta y NC
            if move.move_type not in ("out_invoice", "out_refund"):
                continue

            # FA-A / FA-B / FA-C 00003-00001234
            if not re.match(r"^FA-[ABC]\s\d{5}-\d{8}$", move.move_name):
                raise ValidationError(_(
                    "Formato inválido de número de comprobante.\n\n"
                    "Debe ser exactamente:\n"
                    "FA-A 00003-00001234\n"
                    "FA-B 00003-00001234\n"
                    "FA-C 00003-00001234"
                ))
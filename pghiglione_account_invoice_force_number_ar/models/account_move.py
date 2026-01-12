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

            journal = move.journal_id

            # Solo validar diarios AFIP
            if not journal.l10n_ar_afip_pos_id:
                continue

            # Solo ventas (no compras ni asientos)
            if move.move_type not in ("out_invoice", "out_refund"):
                continue

            if not re.match(r"^FA-[ABC]\s\d{5}-\d{8}$", move.move_name):
                raise ValidationError(_(
                    "Formato inválido de número de factura.\n\n"
                    "Para diarios AFIP debe ser:\n"
                    "FA-A 00003-00001234\n"
                    "FA-B 00003-00001234\n"
                    "FA-C 00003-00001234"
                ))
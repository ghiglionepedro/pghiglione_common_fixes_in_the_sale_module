import re
from odoo import models, api, _
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = "account.move"

    @api.constrains("move_name")
    def _check_move_name_afip_format(self):
        for move in self:
            if move.move_name:
                if not re.match(r"^FA-[ABC]\s\d{5}-\d{8}$", move.move_name):
                    raise ValidationError(_(
                        "Formato inválido de número de factura.\n\n"
                        "Debe ser exactamente:\n"
                        "FA-A 00003-00001234\n"
                        "FA-B 00003-00001234\n"
                        "FA-C 00003-00001234"
                    ))
# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class invoice_add_custom_field_factura(models.Model):
    _inherit = 'account.move'

    field_custom_factura = fields.Char(
        string="Factura manual",
    )
# -*- coding: utf-8 -*-
from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_type_origin = fields.Selection([
        ('pos_customer', 'Cliente de mostrador'),
        ('account', 'Cuenta corriente'),
        ('web_customer', 'Cliente de sitio Web')
    ], string='Origen del cliente', related='partner_id.partner_type_origin', store=True, readonly=True)
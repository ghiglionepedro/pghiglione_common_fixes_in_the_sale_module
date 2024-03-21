# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SaleOrderPartnerTypeList(models.Model):
    _inherit = 'sale.order'

    partner_type = fields.Char(string='Customer Type', compute='_compute_partner_type', store=True)

    @api.depends('partner_id.is_company')
    def _compute_partner_type(self):
        for order in self:
            if order.partner_id and order.partner_id.is_company:
                order.partner_type = 'Compania'
            else:
                order.partner_type = 'Individual'
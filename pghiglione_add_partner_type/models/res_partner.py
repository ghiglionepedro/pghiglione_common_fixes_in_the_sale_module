from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_type_origin = fields.Selection([
        ('pos_customer', 'Cliente de mostrador'),
        ('account', 'Cuenta corriente'),
        ('web_customer', 'Cliente de sitio Web')
    ], string='Origen del cliente', default='pos_customer', required=True)
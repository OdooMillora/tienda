# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    pw_allow_refund = fields.Boolean(string='Restrict Refund')
    pw_refund_password = fields.Char('Refund Password')


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pw_allow_refund = fields.Boolean(related='pos_config_id.pw_allow_refund', readonly=False)
    pw_refund_password = fields.Char(related='pos_config_id.pw_refund_password', readonly=False)

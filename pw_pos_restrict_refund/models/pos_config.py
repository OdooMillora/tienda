# -*- coding: utf-8 -*-
from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    def _get_employee(self):
        domain =[('id', '=', -1)]
        cont=self.env.context
        if cont.get('params'):
            fv=self.env['res.config.settings'].browse(cont.get('params').get('cids'))
            domain =[('id', 'in', fv.pos_config_id.employee_ids.ids)]
       
        return domain

    pw_allow_refund = fields.Boolean(string='Restrict Refund')
    #pw_refund_password = fields.Char('Refund Password')
    pw_refund_employee_ids = fields.Many2one('hr.employee',string="PW Refund Employees")
#lambda self: [('id', 'in', [pos_config_id.config_id.employee_ids])]

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    pw_allow_refund = fields.Boolean(related='pos_config_id.pw_allow_refund', readonly=False)
    #pw_refund_password = fields.Char(related='pos_config_id.pw_refund_password', readonly=False)
    pw_refund_employee_ids = fields.Many2one(related='pos_config_id.pw_refund_employee_ids',readonly=False)

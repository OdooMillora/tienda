# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PosOrderLine(models.Model):
    _inherit = 'pos.order.line'

    user_id = fields.Many2one('hr.employee', string='Salesperson')

class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_commissionable=fields.Boolean('Is Commissionable')

class ProductProduct(models.Model):
    _inherit = "product.product"

    is_commissionable=fields.Boolean('Is Commissionable')

class PosSession(models.Model):
    _inherit = 'pos.session'

    def _loader_params_product_product(self):
        result = super()._loader_params_product_product()
        result['search_params']['fields'].append('is_commissionable')
        return result
#product.product
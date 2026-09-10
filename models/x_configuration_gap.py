# -*- coding: utf-8 -*-
from odoo import models, fields

class XConfigurationGap(models.Model):
    _inherit = 'x_configuration'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')

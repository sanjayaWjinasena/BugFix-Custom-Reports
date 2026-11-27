# -*- coding: utf-8 -*-
from odoo import fields, models


class XConfiguration(models.Model):
    _name = 'x_configuration'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name
    _inherit = ['mail.activity.mixin']
    _description = 'Configuration'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_sequence = fields.Integer(string='Sequence')

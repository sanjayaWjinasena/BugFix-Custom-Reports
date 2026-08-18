# -*- coding: utf-8 -*-
from odoo import fields, models


class XConfiguration(models.Model):
    _name = 'x_configuration'
    _description = 'Configuration'

    x_active = fields.Boolean(string='Active')
    x_name = fields.Char(string='Name')
    x_studio_sequence = fields.Integer(string='Sequence')

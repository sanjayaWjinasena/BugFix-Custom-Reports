# -*- coding: utf-8 -*-
from odoo import models, fields

class XCustomReportsGap(models.Model):
    _inherit = 'x_custom_reports'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_active = fields.Boolean(string='Active')
    x_color = fields.Integer(string='Color')
    x_custom_reports_line_ids_7ee39 = fields.One2many(comodel_name='x_custom_reports_line_c55e7', inverse_name='x_custom_reports_id', string='New Lines')
    x_name = fields.Char(string='Description', required=True)
    x_studio_notes = fields.Html(string='Notes')
    x_studio_tag_ids = fields.Many2many(comodel_name='x_custom_reports_tag', string='Tags')

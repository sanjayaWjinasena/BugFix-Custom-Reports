# -*- coding: utf-8 -*-
from odoo import models, fields

class XCustomReportsStageGap(models.Model):
    _inherit = 'x_custom_reports_stage'

    x_name = fields.Char(string='Stage Name', required=True)

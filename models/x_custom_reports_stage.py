# -*- coding: utf-8 -*-
"""Sentinel declaration for x_custom_reports_stage so cross-references resolve."""
from odoo import fields, models


class XCustomReportsStage(models.Model):
    _name = 'x_custom_reports_stage'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name
    _description = 'Custom Reports Stages'

    x_name = fields.Char(string='Stage Name')
    x_studio_sequence = fields.Integer(string='Sequence')

"""Sentinel declaration for x_custom_reports_stage so cross-references resolve."""

from odoo import fields, models


class XCustomReportsStage(models.Model):
    _name = "x_custom_reports_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _description = "Custom Reports Stages"

    name = fields.Char(string="Stage Name")
    sequence = fields.Integer(string="Sequence")


class XCustomReportsStageGap(models.Model):
    _inherit = "x_custom_reports_stage"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    name = fields.Char(string="Stage Name", required=True)

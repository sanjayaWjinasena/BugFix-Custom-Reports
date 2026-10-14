from odoo import fields, models


class XCustomReportsStageGap(models.Model):
    _inherit = 'x_custom_reports_stage'
    _rec_name = 'x_name'  # Clear-DB Studio model: records are named by x_name

    x_name = fields.Char(string='Stage Name', required=True)

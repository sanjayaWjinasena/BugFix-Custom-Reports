from odoo import fields, models


class XCustomReports(models.Model):
    _name = "x_custom_reports"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Custom Reports"

    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    name = fields.Char(string="Description")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    x_studio_currency_id = fields.Many2one("res.currency", string="Currency")
    x_studio_date = fields.Date(string="Date")
    x_studio_date_start = fields.Datetime(string="Start Date")
    x_studio_date_stop = fields.Datetime(string="End Date")
    x_studio_image = fields.Binary(string="Image")
    x_studio_kanban_state = fields.Selection(
        [("normal", "In Progress"), ("done", "Ready"), ("blocked", "Blocked")],
        string="Kanban State",
    )
    x_studio_partner_email = fields.Char(string="Email")
    x_studio_partner_id = fields.Many2one("res.partner", string="Contact")
    x_studio_partner_phone = fields.Char(string="Phone")
    custom_reports_priority = fields.Boolean(string="High Priority")
    sequence = fields.Integer(string="Sequence")
    x_studio_stage_id = fields.Many2one(
        "x_custom_reports_stage", string="Stage", ondelete="restrict"
    )
    x_studio_user_id = fields.Many2one("res.users", string="Responsible")
    x_studio_value = fields.Float(string="Value")  # was Monetary (no currency_field)


class XCustomReportsGap(models.Model):
    _inherit = "x_custom_reports"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    x_custom_reports_line_ids_7ee39 = fields.One2many(
        comodel_name="x_custom_reports_line_c55e7",
        inverse_name="x_custom_reports_id",
        string="New Lines",
    )
    name = fields.Char(string="Description", required=True)
    x_studio_notes = fields.Html(string="Notes")
    x_studio_tag_ids = fields.Many2many(
        comodel_name="x_custom_reports_tag", string="Tags"
    )

from odoo import fields, models


class XCustomReports(models.Model):
    _name = "custom_reports"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Custom Reports"

    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    name = fields.Char(string="Description")
    accounting_company_id = fields.Many2one("res.company", string="Company")
    accounting_currency_id = fields.Many2one("res.currency", string="Currency")
    date = fields.Date(string="Date")
    date_start = fields.Datetime(string="Start Date")
    date_stop = fields.Datetime(string="End Date")
    image = fields.Binary(string="Image")
    kanban_state = fields.Selection(
        [("normal", "In Progress"), ("done", "Ready"), ("blocked", "Blocked")],
        string="Kanban State",
    )
    partner_email = fields.Char(string="Email")
    partner_id = fields.Many2one("res.partner", string="Contact")
    partner_phone = fields.Char(string="Phone")
    custom_reports_priority = fields.Boolean(string="High Priority")
    sequence = fields.Integer(string="Sequence")
    stage_id = fields.Many2one(
        "custom_reports_stage", string="Stage", ondelete="restrict"
    )
    user_id = fields.Many2one("res.users", string="Responsible")
    value = fields.Float(string="Value")  # was Monetary (no currency_field)


class XCustomReportsGap(models.Model):
    _inherit = "custom_reports"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    color = fields.Integer(string="Color")
    custom_reports_line_ids_7ee39 = fields.One2many(
        comodel_name="custom_reports_line_c55e7",
        inverse_name="custom_reports_id",
        string="New Lines",
    )
    name = fields.Char(string="Description", required=True)
    notes = fields.Html(string="Notes")
    tag_ids = fields.Many2many(
        comodel_name="custom_reports_tag",
        relation="x_custom_reports_x_custom_reports_tag_rel",
        column1="x_custom_reports_id",
        column2="x_custom_reports_tag_id",
        string="Tags",
    )

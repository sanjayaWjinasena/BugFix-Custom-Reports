from odoo import fields, models


class XConfiguration(models.Model):
    _name = "x_configuration"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Configuration"

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")
    sequence = fields.Integer(string="Sequence")


class XConfigurationGap(models.Model):
    _inherit = "x_configuration"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean(string="Active")
    name = fields.Char(string="Name")

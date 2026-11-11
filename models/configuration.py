from odoo import fields, models


class XConfiguration(models.Model):
    _name = "configuration"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name
    _inherit = ["mail.activity.mixin"]
    _description = "Configuration"

    active = fields.Boolean()
    name = fields.Char()
    sequence = fields.Integer()


class XConfigurationGap(models.Model):
    _inherit = "configuration"
    _rec_name = "name"  # Clear-DB Studio model: records are named by name

    active = fields.Boolean()
    name = fields.Char()

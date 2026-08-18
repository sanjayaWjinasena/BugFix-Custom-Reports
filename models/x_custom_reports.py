# -*- coding: utf-8 -*-
from odoo import fields, models


class XCustomReports(models.Model):
    _name = 'x_custom_reports'
    _description = 'Custom Reports'

    x_active = fields.Boolean(string='Active')
    x_color = fields.Integer(string='Color')
    x_name = fields.Char(string='Description')
    x_studio_company_id = fields.Many2one('res.company', string='Company')
    x_studio_currency_id = fields.Many2one('res.currency', string='Currency')
    x_studio_date = fields.Date(string='Date')
    x_studio_date_start = fields.Datetime(string='Start Date')
    x_studio_date_stop = fields.Datetime(string='End Date')
    x_studio_image = fields.Binary(string='Image')
    x_studio_kanban_state = fields.Selection([], string='Kanban State')
    x_studio_partner_email = fields.Char(string='Email')
    x_studio_partner_id = fields.Many2one('res.partner', string='Contact')
    x_studio_partner_phone = fields.Char(string='Phone')
    x_studio_priority = fields.Boolean(string='High Priority')
    x_studio_sequence = fields.Integer(string='Sequence')
    x_studio_stage_id = fields.Many2one('x_custom_reports_stage', string='Stage')
    x_studio_user_id = fields.Many2one('res.users', string='Responsible')
    x_studio_value = fields.Float(string='Value')  # was Monetary (no currency_field)
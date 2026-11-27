# -*- coding: utf-8 -*-
"""x_custom_reports_line_c55e7.x_custom_reports_id, moved here from
BugFix-Studio-Misc (v0.0.112) in v0.0.18.

x_custom_reports is owned by BugFix-Custom-Reports, which loads AFTER
BugFix-Studio-Misc (where the line model itself is defined). Declared
upstream, the Many2one was rewritten to comodel '_unknown' at Studio-Misc's
setup pass and never recovered during upgrade-mode registry builds (Odoo 17
reuses the Field object). A declaration in the comodel-owning module is the
only load-order-proof fix. It is also the inverse of
x_custom_reports.x_custom_reports_line_ids_7ee39 (models/x_custom_reports_gap.py),
so both ends of the relation now live in this module.

Column data is preserved: the source module's pre-migrate drops its
ir.model.data pointer so Odoo's end-of-load cleanup never unlinks the field;
this module's reflection re-attaches the xmlid.
"""
from odoo import fields, models


class XCustomReportsLineC55e7(models.Model):
    _inherit = 'x_custom_reports_line_c55e7'

    x_custom_reports_id = fields.Many2one(comodel_name='x_custom_reports', string='X Custom Reports')

# -*- coding: utf-8 -*-
{
    'name': 'BugFix - Custom - Reports',
    'version': '17.0.0.0.3',
    'summary': 'Studio custom-reports config models (x_custom_reports, tags, stages, x_configuration)',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization — Odoo SH does not ship a manifest for it.
    'depends': ['base_setup'],
    'data': ['security/ir.model.access.csv', 'security/ir_model_pins.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}

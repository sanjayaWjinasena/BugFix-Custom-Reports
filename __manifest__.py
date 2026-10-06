# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : SubModule : Reporting : Custom Reports',
    'version': '17.0.0.0.22',
    'summary': 'Studio custom-reports config models (x_custom_reports, tags, stages, x_configuration)',
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    # Do NOT depend on studio_customization — Odoo SH does not ship a manifest for it.
    'depends': ['base_setup', 'BugFix-Studio-Misc'],
    'data': [
        'security/ir_model_pins.xml',
        'security/ir.model.access.csv',
        'data/record_rules_gap.xml',
        'data/window_actions_gap.xml',
        'data/ir_defaults_gap.xml',
        'views/x_configuration_e_views.xml',
        'views/x_custom_reports_e_views.xml',
        'views/views_final.xml',
        'views/x_custom_reports_stage_e_views.xml',
        'data/menus_f6.xml',
        'data/menus_jinasena_reports.xml',
        'data/menus_from_studio_misc.xml',
    ],
    # Staging_Migration: adopt existing Studio models for the ir.model pins.
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
'installable': True,
    'auto_install': False,
    'application': True,
}

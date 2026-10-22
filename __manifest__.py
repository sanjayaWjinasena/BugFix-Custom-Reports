{
    # upgrade-testing branch: data files below are commented out - this branch installs
    # functions only, no data is seeded.
    "name": "Jinasena : SubModule : Reporting : Custom Reports",
    "version": "17.0.0.0.20",
    "summary": "Studio custom-reports config models (x_custom_reports, tags, stages, "
    "x_configuration)",
    "author": "Jinasena Agricultural Machinery (Pvt) Ltd.",
    "category": "Extra Tools",
    "license": "LGPL-3",
    # Do NOT depend on studio_customization — Odoo SH does not ship a manifest for it.
    "depends": ["base_setup", "BugFix-Studio-Misc"],
    "data": [
        "security/ir_model_pins.xml",
        "security/bugfix_custom_reports_security.xml",
        "security/ir.model.access.csv",
        "data/x_configuration_data.xml",
        "data/x_custom_reports_data.xml",
        "views/x_configuration_views.xml",
        "views/x_custom_reports_stage_views.xml",
        "views/x_custom_reports_views.xml",
        "views/bugfix_custom_reports_menus.xml",
    ],
    "post_init_hook": "post_init_hook",
    "application": True,
}

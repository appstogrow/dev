# Copyright 2020 AppsToGROW
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Open inherited view in current window",
    "version": "15.0.1.0.0",
    "author": "AppsToGROW,Odoo Community Association (OCA)",
    "description": """
        Open inherited view in current window.
        The purpose is to create/edit and save child views
        when the parent view is readonly.""",
    "summary": "Open inherited view in current window.",
    "category": "Generic Modules",
    "website": "https://github.com/oca/server-ux",
    "depends": ["base"],
    "installable": True,
    "application": False,
    "images": [],
    "license": "AGPL-3",
    "data": ["views/ir.ui.view.xml"],
}

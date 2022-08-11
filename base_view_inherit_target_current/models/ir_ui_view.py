from odoo import models


class View(models.Model):
    _inherit = "ir.ui.view"

    """
    TODO
    The normal way to open an inherited view is by clicking anywhere on the record line.
    -> Trigger action_open_inherited_view()
    The normal way to create an inherited view is by clicking on "Add a line".
    -> Trigger action_create_inherited_view
    When this is implemented, remove the buttons.
    """

    def action_create_inherited_view(self, *args, **kwargs):
        test = 1
        self.ensure_one()
        context = {
            "default_name": self.name + " for " + self.env.company.name,
            "default_type": self.type,
            "default_model": self.model,
            "default_inherit_id": self.id,
            "default_mode": "extension",
        }
        return {
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "ir.ui.view",
            "target": "current",
            "context": context,
        }

    def action_open_inherited_view(self, *args, **kwargs):
        self.ensure_one()
        return {
            "name": self.display_name,
            "type": "ir.actions.act_window",
            "view_type": "form",
            "view_mode": "form",
            "res_model": "ir.ui.view",
            "res_id": self.id,
            "target": "current",
        }

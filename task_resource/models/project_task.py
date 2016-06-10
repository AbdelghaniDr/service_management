# -*- coding: utf-8 -*-
# © 2015 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
from openerp import api, fields, models
from openerp.exceptions import ValidationError, Warning
from openerp.tools.translate import _


class ProjectTask(models.Model):
    _inherit = "project.task"

    resource_ids = fields.One2many(
        comodel_name='task.resource',
        inverse_name='task_id',
        string='Task Resource',
        copy=True,)

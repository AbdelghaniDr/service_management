# -*- coding: utf-8 -*-
# © 2016 Eficent Business and IT Consulting Services S.L.
# (https://www.eficent.com).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import api, fields, models, _


class BusinessRequirementArtifact(models.Model):
    _name = "business.requirement.artifact"
    _description = "Business Requirement Artifact"

    name = fields.Char(string='Name')


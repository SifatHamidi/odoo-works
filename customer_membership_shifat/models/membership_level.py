from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError
import re


class MembershipLevel(models.Model):
    _name="membership.level"
    _description="Membership Level"
    _order='ranking'
    _rec_name='level_name'

    level_name=fields.Char('Level Name',required=True)
    ranking=fields.Integer("Ranking")
    display_name=fields.Char("Display Name", compute="_compute_display_name",readonly="1")

    @api.depends("level_name","ranking")
    def _compute_display_name(self):
        for rec in self:
            rec.display_name=(str(rec.ranking) or '') + ':' + (rec.level_name or '')

    @api.constrains('ranking')
    def _check_number_length(self):
        for rec in self:
            if len(str(rec.ranking)) != 1 or rec.ranking <0:
                raise ValidationError(_("Number Must be between 0 to 9"))

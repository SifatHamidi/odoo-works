from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError
import re



class ResPartner(models.Model):
    _inherit="res.partner"

    is_member_respartner=fields.Boolean(string="Is a memebr?")
    membership_level_respartner=fields.Many2one("membership.level", string="Membership Level")


class CustomerResPartner(models.Model):
    _inherit="res.partner"


    filter_customer_master=fields.Boolean("“Filter Products in SO Based on Pricelist")
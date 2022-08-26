# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError
import re



class VendorsDealers(models.Model):
    _inherit="res.partner"

    #dealers_info_ids
    # product_manuf_ids
    #Many2one  product_manuf_id

    dealers_info=fields.Many2many("product.manufacture",string="Dealers")
    email=fields.Char(string="Email",related="dealers_info.email")
    phone_number=fields.Char(string="Phone",related="dealers_info.phone_number")
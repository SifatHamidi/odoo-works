# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError



class ProductTemplate(models.Model):
    _inherit="product.template"

    authorized_manufacturer=fields.Many2one("product.manufacture",string="Authorized Manufacturer")
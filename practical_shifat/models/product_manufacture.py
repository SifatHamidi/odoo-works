# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError
import re

class ProductManufacture(models.Model):
    _name = "product.manufactured"
    _description = "Product Manufacture"


    name = fields.Char(string = "Name", required=True)
    street_name = fields.Char('Street Name')
    street_name2=fields.Char(string="Street2")
    building=fields.Char("Building")
    floor_room=fields.Char("Floor/Room#")
    city_name=fields.Char("City")
    zip_code=fields.Char("Zip")
    phone_number=fields.Char("Phone")
    email=fields.Char("Email")
    country_id=fields.Many2one("res.country","Country",required=True)
    state_id=fields.Many2one("res.country.state",string="State")

    
    # @api.onchange('phone_number')
    # def _onchange_phone_number(self):
    #     self.phone_number="+"+str(self.country_id.phone_code) + str(self.phone_number or '')

    @api.constrains("email")
    def _check_email(self):
        for rec in self:
            if not re.match('(\w+[.|\w])*@(\w+[.])*\w+', rec.email):
                 raise ValidationError("Not a valid E-mail ID")

    @api.onchange('country_id')
    def _onchange_country_id_wrapper(self):
        res = {'domain': {'state_id': []}}
        if self.country_id:
                res['domain']['state_id'] = [('country_id', '=', self.country_id.id)]
        return res

    @api.constrains('phone_number')
    def _check_phone_number(self):
        for rec in self:
            if rec.phone_number and len(rec.phone_number) < 10:
                raise ValidationError("Phone number should be 15 digit")
        return True

    


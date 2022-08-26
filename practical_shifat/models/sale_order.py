# -*- coding: utf-8 -*-

from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT,DEFAULT_SERVER_DATETIME_FORMAT
import re



class SalesOrderValidation(models.Model):
    _inherit="sale.order"



    name=fields.Many2one("product.manufacture",string="Product Info")

    @api.onchange('date_order')
    def _onchange_date(self):
        if datetime.strptime(str(self.date_order), DEFAULT_SERVER_DATETIME_FORMAT).date() < datetime.now().date():
            raise ValidationError(_("No previous date is allowed"))


    @api.constrains("validity_date","date_order")
    def _validity_date_change(self):
        if self.date_order and self.validity_date:
            date1 = datetime.strptime(str(self.date_order), DEFAULT_SERVER_DATETIME_FORMAT).date()
            date2 = datetime.strptime(str(self.validity_date), DEFAULT_SERVER_DATE_FORMAT).date()
            days_duration=int((date2 - date1).days)
            print("dayssss", days_duration)
            if days_duration < 5:
                raise ValidationError(_("Expiration date must be atleast 5 days ahead from quotation date"))


    @api.onchange('client_order_ref')
    def onchange_name(self):
        text=re.findall(r'\d+', str(self.client_order_ref))
        for i in text:
            if i in self.client_order_ref:
                if self.client_order_ref.index(i) == 0:
                    new=i +'-'
                else:
                    new="-" + i
                self.client_order_ref=self.client_order_ref.replace(i,new)
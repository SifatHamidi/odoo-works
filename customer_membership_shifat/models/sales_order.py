from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT,DEFAULT_SERVER_DATETIME_FORMAT
import re



class SalesOrder(models.Model):
    _inherit="sale.order"

    memership_level_sales_order=fields.Many2one("membership.level", string="Membership Level")
    memership_level_name = fields.Char(string="Membership Level")



class SalesOrderValidation(models.Model):
    _inherit="sale.order"

    @api.onchange('date_order','partner_id')
    def _onchange_date(self):
        if datetime.strptime(str(self.date_order), DEFAULT_SERVER_DATETIME_FORMAT).date() < datetime.now().date():
            raise ValidationError(_("No previous date is allowed"))
        if self.partner_id and self.partner_id.membership_level_respartner:
            self.memership_level_name = self.partner_id.membership_level_respartner.level_name


    @api.constrains("validity_date","date_order")
    def _validity_date_change(self):
        date1 = datetime.strptime(str(self.date_order), DEFAULT_SERVER_DATETIME_FORMAT).date()
        date2 = datetime.strptime(str(self.validity_date), DEFAULT_SERVER_DATE_FORMAT).date()
        days_duration=int((date2 - date1).days)
        print("dayssss", days_duration)
        if days_duration < 5:
            raise ValidationError(_("Expiration date must be atleast 5 days ahead from quotation date"))


    @api.onchange('client_order_ref')
    def _onchange_name(self):
        text=re.findall(r'\d+', str(self.client_order_ref))
        for number in text:
            if number in self.client_order_ref:
                if self.client_order_ref.index(number) == 0:
                    new=number +'-'
                else:
                    new="-" + number
                self.client_order_ref=self.client_order_ref.replace(number,new)

    # def action_confirm(self):
    #     print('josss')
    #     res=super(SalesOrderValidation,self).action_confirm()

    #     return res
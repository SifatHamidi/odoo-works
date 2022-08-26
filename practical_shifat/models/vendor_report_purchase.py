from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError


class VendorReportPurchaseNew(models.Model):
    _name="vendor.report.purchase.new"
    _description="Vendor Report Purchase New"


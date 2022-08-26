from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError


class VendorReportPurchase(models.Model):
    _name="vendor.report.purchase"
    _description="Vendor Report Purchase"


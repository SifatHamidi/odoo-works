from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError



class VendorReportPurchaseNewWizard(models.TransientModel):
    _name="vendor.report.purchase.new.wizard"
    _description="Vendor Report Purchase New Wizard"


    vendor_id=fields.Many2one('purchase.order', 'Vendor ID', domain="[('state', '=','purchase')]")
    vendor_name_purchase_confirm=fields.Many2one(related="vendor_id.partner_id", string="Confirmed Vendor")
    # vendor_name_purchase_confirm=fields.One2many('purchase.order', 'partner_id', string="Confirmed Vendor")


    # def name_get(self):
    #     result=[] 
    #     for rec in self:
    #         vendor=rec.vendor_id.partner_id
    #         result.append((rec.id,vendor))
    #     return result


    def action_print_excel_report(self):

        # domain=[]
        # vendor_id=self.vendor_id
        # if vendor_id:
        #     domain+=[('vendor_id','=',vendor_id.name)]
        # print('domain===-----',domain)
        vendor_info=self.env['purchase.order'].search_read([])
        data={

            "vendor_info" : vendor_info
        }
        return self.env.ref('practical_shifat.action_vendor_report_purchase_new_xlsx').report_action(self,data=data)
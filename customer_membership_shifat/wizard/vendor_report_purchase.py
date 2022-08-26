from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError



class VendorReportPurchaseWizard(models.TransientModel):
    _name="vendor.report.purchase.wizard"
    _description="Vendor Report Purchase Wizard"


    vendor_id=fields.Many2one('purchase.order', 'Vendor ID', domain="[('state', '=','purchase')]")
    vendor_name_purchase_confirm=fields.Many2one(related="vendor_id.partner_id", string="Confirmed Vendor")
    # vendor_name_purchase_confirm=fields.One2many('purchase.order', 'partner_id', string="Confirmed Vendor")


    def name_get(self):
        result=[] 
        for rec in self:
            vendor=rec.vendor_id.partner_id
            result.append((rec.id,vendor))
        return result

# section_id = fields.Many2one('model.section', string="Section") 

# def name_get(self, cr, uid, ids, context=None):
#     if not len(ids):
#         return []
#         res=[]
#         for section in self.browse(cr, uid, ids,context=context):
#             res.append((section.id,  str(section.subject_id.name)+" "+str(section.name)))           
#         return res 


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
        return self.env.ref('customer_membership_shifat.action_vendor_report_purchase_xlsx').report_action(self,data=data)
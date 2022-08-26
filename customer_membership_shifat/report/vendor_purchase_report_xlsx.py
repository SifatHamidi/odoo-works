from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError



class VendorReportPurchaseNewXlsx(models.AbstractModel):
    _name="report.customer_membership_shifat.vendor_report_purchase_xlsx"
    _inherit="report.report_xlsx.abstract"



    def generate_xlsx_report(self, workbook, data, partners):
        # print('vendor_info:', data['vendor_info'])

        data=self.env['purchase.order'].search([('state', '=','purchase')])
        sheet=workbook.add_worksheet("Vendor Information")
        bold=workbook.add_format({'bold':True})
        # sheet.set_row('C:D',25)
        row=0
        col=0
        sheet.write(row,col,'P0',bold)
        sheet.write(row,col+1,'Date',bold)
        sheet.write(row,col+2,'Vendor Name',bold)
        sheet.write(row,col+3,'PO Status',bold)
        sheet.write(row,col+4,'Total Amount',bold)

        for vendor in data:
            row+=1
            sheet.write(row,col,vendor.name)
            sheet.write(row,col+1,vendor.date_order)
            sheet.write(row,col+2,vendor.partner_id.name)
            sheet.write(row,col+3,vendor.state)
            sheet.write(row,col+4,vendor.amount_total)













        # for obj in partners:
        #     report_name = obj.name
        #     # One sheet by partner
        #     sheet = workbook.add_worksheet(report_name[:31])
        #     bold = workbook.add_format({'bold': True})
        #     sheet.write(0, 0, obj.name, bold)



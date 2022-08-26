# -*- coding: utf-8 -*-

import base64
import qrcode
from io import BytesIO
from odoo import models, fields, api, _ 
from odoo.exceptions import UserError


class QrCode(models.Model):
    
    
    _inherit = "bista.trainee"
    qr_code = fields.Binary('QRcode', compute="_generate_qr")
   
    def _generate_qr(self):
        for rec in self:
            if qrcode and base64:
                
                qr = qrcode.QRCode(version=1,error_correction= qrcode.constants.ERROR_CORRECT_L,box_size=3,border=4)
                qr.add_data("Name : ")
                qr.add_data(rec.name)
                qr.add_data("\n Email : ")
                qr.add_data(rec.email)
                qr.add_data("\n Designation : ")
                qr.add_data(rec.designation.name)
                qr.add_data("\n Joining Date : ")
                qr.add_data(rec.joining_date)
                qr.make(fit=True)
                img = qr.make_image()
                temp = BytesIO()
                img.save(temp, format="PNG")
                qr_image = base64.b64encode(temp.getvalue())
                rec.update({'qr_code':qr_image})
            else:
                raise UserError(_('Necessary Requirements To Run This Operation Is Not Satisfied'))
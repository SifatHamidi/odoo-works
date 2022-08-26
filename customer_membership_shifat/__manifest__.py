# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Customer Membership shifat',
    'version': '1.0',
    'category': 'Sales/Sales',
    'summary': 'For Practice Purposes',
    'description': """This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': ['base','sale','report_xlsx'],
    'data': [
        "security/ir.model.access.csv",
        "security/security.xml",
        'data/data_view.xml',
        "wizard/vendor_report_purchase_view.xml",
        "report/vendor_report_purchase.xml",
        "views/membership_level_views.xml",
        "views/sale_order_views.xml",
        "views/res_partner_view.xml",
        "views/vendor_report_purchase_view.xml"
        
        ],
   # 'demo': ["demo/demo.xml"],
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}

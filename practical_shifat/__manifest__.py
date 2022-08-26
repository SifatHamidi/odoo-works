# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Practical shifat',
    'version': '1.0',
    'category': 'Sales/Sales',
    'summary': 'For Practice Purposes',
    'description': """This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': ['base','product','sale','report_xlsx','purchase'],
    'data': [
        "security/ir.model.access.csv",
        "security/security.xml",
        "wizard/vendor_report_purchase_view.xml",
        "report/vendor_report_purchase.xml",
        "views/vendor_report_purchase_view.xml",
        "views/product_manufacture_view.xml",
        "views/vendors_dealers_view.xml",
        "views/product_template_view.xml",
        "views/sale_order_views.xml"
        
        ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'assets': {},
    'license': 'LGPL-3',
}

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{ 
    'name': 'Bista',
    'version': '1.0',
    'category':'Sales/Sales',
    'summary':'For Practice purposes',
    'description': """ This is a module for training and demonstration.""",
    'depends': ['base','mail','contacts'],
    'data' : [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        # "data/mail_template.xml",
        "views/bista_trainee_views.xml",
        "views/bista_trainer_views.xml",
        "views/bista_all_views.xml",
        "views/qr_code_views.xml",
        "report/report.xml" ,
    ],
    'demo':[],
    'installable': True,
    'auto_install': False,
    'assets':{},
    'license': 'LGPL-3',
    
}
# -*- coding: utf-8 -*-

# from turtle import done
from odoo import api, fields, models, SUPERUSER_ID, _,tools
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
import datetime
import base64
from odoo.modules.module import get_module_resource
from datetime import date
import re


class Trainee(models.Model):
    _name = "bista.trainee"
    _inherit =["mail.thread","mail.activity.mixin"]
    _description = "Bista Trainee"


    # def _get_default_image(self):
    #     image_path = get_module_resource('bista_module', "static\src\img", 'trainer.png')
    #     # return tools.image_resize_image_big(base64.b64encode(open(image_path, 'rb').read()))
    #     return base64.b64encode(open(image_path, 'rb').read())

    image=fields.Binary(string="Image")
    name=fields.Char(string="Name",compute='_compute_full_name',store=True)
    first_name=fields.Char()
    last_name=fields.Char()

    email=fields.Char("Email", tracking=True)
    gender=fields.Selection([
    ("male","Male"),
    ("female", "Female"),("other", "Other")], default="male")
    emp_code=fields.Char("Emp Code",Store=True,tracking=True)
    trainee_id = fields.Char(string="Trainee ID",required=True, readonly=True, default=lambda self: _('New'))
    trainer_details_ids = fields.Many2many('bista.trainer','trainers_trainee_rel','trainee_id','trainer_id',string='Trainer Detailes')
    # default= lambda self: self.env['ir.sequence'].next_by_code('bista.trainee')

    dob=fields.Date("DOB",tracking=True)
    date=fields.Date("Date",required=True, default=date.today())
    age=fields.Char("Age",compute='_compute_age',store=True)
    description=fields.Html(string="Description")
    joining_date=fields.Date("Joining Date")
    designation=fields.Many2one("bista.trainee.role","Designation", tracking=True, store=True)
    status=fields.Selection([("new","New"),("training","Training"),("rejected","Rejected"),("employed","Employed")], default='new')
    priority = fields.Selection([('0', 'Normal'),('1', 'Good'),('2', 'Very Good'),('3', 'Excellent')], "Appreciation", default='0')
    linkedin_id=fields.Char("LinkedIn Link")
    location=fields.Many2one("bista.location","Location",tracking=True)
    is_true=fields.Boolean("Is that True?")
    color=fields.Integer(string="Color")

    _sql_constraints = [("trainee_id_unique", "unique(trainee_id)","The User ID should be unique"),
     					("name_unique", "unique(name)","The Name should be unique"),]

    @api.model 
    def create(self,vals):
        print('self create---------------',vals)
        if vals.get('trainee_id', _('New')) == _('New'):
            vals['trainee_id'] = self.env['ir.sequence'].next_by_code('bista.trainee') or _('New')
        return super(Trainee,self).create(vals)

    def write(self,vals):
        print('self write---------------',self)
        return super(Trainee,self).write(vals)

    @api.depends('dob')
    def _compute_age(self):
        for record in self:
            if record.dob and record.dob <= fields.Date.today():
                record.age = relativedelta(
                    fields.Date.from_string(fields.Date.today()),
                    fields.Date.from_string(record.dob)).years 
            else: 
                record.age = 0
                
    # @api.depends('age')
    # def _inverse_compute_age(self):
    #     today=date.today()
    #     for rec in self:
    #         rec.dob=today - relativedelta(years=rec.age)
        
                
    # @api.depends('dob')
    # def _compute_age(self):
    #     for record in self:
    #         today=date.today()
    #         if record.dob:
    #             record.age=today.year - record.dob.year
    #         else: 
    #             record.age = 0
    
    def action_sent_email(self):
        print("sending email")
        template_id=self.env.ref("bista_module.bista_trainee_email_template").id
        self.env['mail.template'].browse(template_id).send_mail(self.id,force_send=True)

    @api.depends("first_name","last_name")
    def _compute_full_name(self):
        self.name=(self.first_name or '') + ' ' + (self.last_name or '')

    @api.constrains("trainee_id", "emp_code","email")
    def _check_description(self):
        for record in self:
            if record.trainee_id  and record.emp_code and (record.trainee_id == record.emp_code):
                raise ValidationError("ID and EMP Code must be different")
            if record.email and not re.match('(\w+[.|\w])*@(\w+[.])*\w+', record.email):
                 raise ValidationError("Not a valid E-mail ID")

    def action_post(self):
        print('Checked')

    def action_url(self):
        return {
             'type':'ir.actions.act_url',
             'target': 'new',
             'url':'https://www.odoo.com'
        }

class BistaLocation(models.Model):
    _name="bista.location"
    _inherit =["mail.thread","mail.activity.mixin"]
    _description="Bista Location"
    
    # _rec_name="location"
    
    location=fields.Char("Location",required=True)
    country_id = fields.Many2one('res.country', string="Country")
    state_id = fields.Many2one('res.country.state', string="State", store=True)
    street_1 =fields.Char("Street_1", required=False)
    street_2 =fields.Char("Street_2", required=False)
    city=fields.Char("City", required=False)


    @api.onchange('state_id')
    def _onchange_state(self): 
        if self.state_id:
            self.country_id = self.state_id.country_id

    def name_get(self):
        location_info=[]
        for record in self:
            final_values=str(record.city) + "," + str(record.location)
            location_info.append((record.id,final_values))
        return location_info


    # @api.onchange('state_id','country_id')
    # def set_values_to(self):
    #     for location in self:
    #         location.country_id=location.state_id.country_id.id



class TraineeRole(models.Model):

    _name="bista.trainee.role"
    _inherit =["mail.thread","mail.activity.mixin"]
    _description="Bista Trainee Role"

    name=fields.Char('Designation',required=True)
    sequence=fields.Integer('Sequence',required=False)



class TrainingStages(models.Model):

    _name="bista.training.stages"
    _inherit =["mail.thread","mail.activity.mixin"]
    _description="Bista Training Stages"

    name=fields.Char("Stage", required=True, help="New(draft),Pending Confirm(draft),Trainee Confirm(progrss),Training Completed(progress),Employed(Done)")
    available_batch=fields.Boolean("Available Batch")
    available_training_record=fields.Boolean("Available Training Record")
    status=fields.Selection([("draft","Draft"),("progress","Progress"),("done","Done")])
    
    # new=self.env['bista.trainee'].search(['|',('gender','=', 'male'),('id','=',10)], limit=3,order='id desc, name').name
    # new2=self.env['bista.trainee'].browse(72).name
    # new2=self.env['bista.trainee'].browse([1,67,72]).mapped('name') / self.env['bista.trainee'].browse(1).exists()
    # # alternate 
    # for i in new2:
    #     print(i.name)

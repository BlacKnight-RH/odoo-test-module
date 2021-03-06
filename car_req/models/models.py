# -*- coding: utf-8 -*-

from odoo import models, fields, api


# :: CONVENTION :: Class name in Pascal format  
class CarRequest(models.Model):

    _name = 'car.request'  # Table name in Database
    _description = 'Car for every one'
    _inherit = 'mail.thread'

    name = fields.Char(string='Request', required=True, )
    date_from = fields.Datetime(string='Starting date', required=True, default=fields.Datetime.now() )
    date_to = fields.Datetime(string='End date', required=True, )

    # Table, Relation name :: many of this class belongs to one of ::Table:: class
    car_id = fields.Many2one(comodel_name='fleet.vehicle', string='Car', required=True, )
    employee_id = fields.Many2one(comodel_name='hr.employee', string='Employee', required=True, )
    # selection = [(db field name, display name),]
    # track_visibility: to track the work-flow ::on change::
    state = fields.Selection(string="Status", selection=[('draft', 'Draft'),
                                                         ('confirm', 'Confirm'),
                                                         ('validate', 'Validated'),
                                                         ('refuse', 'Refuse'),
                                                         ('approved', 'Approved'), ],
                             default="draft", track_visibility='onchange', )

    @api.multi
    def confirm_request(self):
        self.state = 'confirm'

    @api.multi
    def validate_request(self):
        self.state = 'validate'

    @api.multi
    def refuse_request(self):
        self.state = 'refuse'

    @api.multi
    def approve_request(self):
        self.state = 'approved'

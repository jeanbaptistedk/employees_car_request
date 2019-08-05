# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CarRequest(models.Model):
    _name = "car.request" # Table DB => car_request
    _description  = "car request"

    name = fields.Char('Request', required=True)
    date_from = fields.Datetime('Starting date', default=fields.Datetime.now())
    date_to = fields.Datetime('End Date', required=False)
    employee_id = fields.Many2one('hr.employee', 'Employe', required=True, ondelete="cascade")
    car_id = fields.Many2one('fleet.vehicle', 'Car', required=True)

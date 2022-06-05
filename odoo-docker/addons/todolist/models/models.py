# -*- coding: utf-8 -*-

from odoo import models, fields, api

class todolist(models.Model):
    _name = 'todo.list'
    _description = 'model for to do list'
    customer_id = fields.Many2one('res.partner', string='Customers')
    description = fields.Text(string="Description", required=True)
    time = fields.Date(string="Date Time", required=True)



from odoo import api, fields, models

#model for registration form
class RegistrationForm(models.Model):
    #model detail
    _name ='registration.form'
    _description = 'data for registration form'

    #data fields
    #First name & last name, type string & mandatory
    first_name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    #gender, type selection (male, female or others) & mandatory
    gender = fields.Selection([('male','Male'),('female','Female'),('other','Other')], required=True, default='male')
    #address, type textbox & mandatory
    address = fields.Text(string="Address", required=True)


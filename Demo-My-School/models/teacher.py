from odoo import api, fields, models, _


class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'teacher'

    image = fields.Image(string="Profile Picture")
    _id = fields.Char('ID')
    name = fields.Char('Teacher Name', required=True)
    department = fields.Char('Department')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    birth_date = fields.Date('Date of birth')
    gender = fields.Selection([('M','Male'),('F','Female')],'Gender')
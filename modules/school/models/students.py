#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
     _name = "school.student"
     _description="Students table"
     

     name = fields.Char(string="Nombre",required=True)
     date_birthday=fields.Date(string="Fecha de nacimiento",required=True)
     employee_id=fields.Many2one(string="Profesor",comodel_name="hr.employee",required=True)
    #  value = fields.Integer()
    #  value2 = fields.Float(compute="_value_pc", store=True)
    #  description = fields.Text()
    #  @api.depends('value')
    #  def _value_pc(self):
    #      for record in self:
    #          record.value2 = float(record.value) / 100


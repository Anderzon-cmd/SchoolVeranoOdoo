#-*- coding: utf-8 -*-

from odoo import models, fields, api


class Subject(models.Model):
     _name = "school.subject"
     _description="Subject Table"
     

     name = fields.Char(string="Nombre",required=True)
     description=fields.Char(string="Descripcion",required=True)
    #  value = fields.Integer()
    #  value2 = fields.Float(compute="_value_pc", store=True)
    #  description = fields.Text()
    #  @api.depends('value')
    #  def _value_pc(self):
    #      for record in self:
    #          record.value2 = float(record.value) / 100


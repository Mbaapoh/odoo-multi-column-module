# -*- coding: utf-8 -*-

from odoo import models, fields, api


class publicSchoolUsa(models.Model):
    _name = 'public.school_usa'
    _description = 'Custom odoo module for the list of public schools in USA'

    school_name = fields.Char(string="School Name")
    state_name = fields.Char(string="State Name")
    state_abbr = fields.Char(string="State Abbr")
    school_type = fields.Char(string="School Type")
    pupil_teacher_ratio = fields.Float(string="Pupil/Teacher Ratio")
    web_site_url = fields.Char(string="Web Site URL")
    title1_eligible_schools = fields.Char(string="Title I Eligible School")
    grade9_offered = fields.Char(string="Grade 9 offered")
    grade10_offered = fields.Char(string="Grade 10 offered")
    grade11_offered = fields.Char(string="Grade 11 offered")
    grade12_offered = fields.Char(string="Grade 12 offered")
    free_lunch_eligible = fields.Integer(string="Free Lunch Eligible")
    grade9_student = fields.Char(string="Grade 9 Students")
    grade10_student = fields.Char(string="Grade 10 Students")
    grade11_student = fields.Char(string="Grade 11 Students")
    grade12_student = fields.Char(string="Grade 12 Students")
    phone_number = fields.Char(string="Phone Number")

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

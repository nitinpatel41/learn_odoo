from odoo import api, fields, models


class Course(models.Model):
    _name = "school.course"
    _description = "Course Detail"

    course_name = fields.Selection([
        ('science', 'Science'),
        ('commerce', 'Commerce'),
        ('iti', 'ITI'),
        ('be/b.tech', 'BE/B.Tech'),
        ('bsc', 'Bsc')], string="Select Course")

    school_fee = fields.Integer(string="School Fee")
    bus_fee = fields.Integer(string="Bus Fee")
    total_fee = fields.Integer(string="Total Fee",compute='calculate_total_fee')

    @api.depends('school_fee', 'bus_fee')
    def calculate_total_fee(self):
        tem_fee = 0
        for rec in self:
            rec.total_fee = rec.bus_fee + rec.school_fee

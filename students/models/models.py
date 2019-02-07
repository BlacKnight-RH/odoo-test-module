# -*- coding: utf-8 -*-

from odoo import models, fields, api

class students(models.Model):
    _name = 'students.students'

    name = fields.Char('Name')
    nfc = fields.Integer('NFC Card')
    parent_id = fields.Many2one('students.parent')
    ruls_id = fields.Many2many('students.rules', relation='rules_sutdents', column1='student_id', column12='rule_id')


class parent(models.Model):
    _name ='students.parent'

    name = fields.Char('Name')
    children_id = fields.One2many('students.students', 'parent_id')


class rules(models.Model):
    _name ='students.rules'

    rule_name = fields.Char('Rule Title')
    students_id = fields.Many2many('students.students', relation ='student_rules', column1 ='rule_id' ,column12='student_id')


    #"""
    # rules by day
    # rules by quantity
    # rules by
    # """


# class resPartner(models.Model):
#     _inherit ="res.partner"
#
#     membership_code = fields.Char('Membership')

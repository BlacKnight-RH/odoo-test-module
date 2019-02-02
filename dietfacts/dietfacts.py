# your code goes here

from odoo import models,fields

class Dietfacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer("calories")
    servsize = fields.Float("Serving Size")
    lastupdate = fields.Date("Last Update")
    isdietitem = fields.Boolean("Diet Item")


class DietFacts_res_users_meal(models.Model):
    _name = "res.users.meal"

    name = fields.Char('Meal Name')
    meal_date = fields.Datetime('Meal Date')
    user_id = fields.Many2one('res.users', 'Meal User')
    note = fields.Text('Meal Notes')
    # item_id = fields.One2many()

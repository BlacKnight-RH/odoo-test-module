from odoo import fields, models,api


class myModule_product_temlate(models.Model):
    _name = "product.template"
    _inherit = "product.template"

    calories = fields.Integer("calories")
    servsize = fields.Float("Serving Size")
    lastupdate = fields.Date("Last Update")
    isdietitem = fields.Boolean("Dite Item")



class myModule_res_user_meal(models.Model):
    # this's the model name which 'll be stored in the database
    _name ="res.user.meal"

    name      = fields.Char('Meal Name')
    meal_date = fields.Datetime('Meal Date')
    user_id   = fields.Many2one('res.users', 'Meal User')
    note      = fields.Text('Meal Note')
    item_ids   = fields.One2many('res.user.mealitem', 'meal_id')

    @api.one
    @api.depends('item_ids', 'item_ids.servings')
    def _calc_calories(self):
        current_calo = 0
        for meal_item in self.item_ids:
            current_calo += (meal_item.calories * meal_item.servings)
        self.totalcalories = current_calo

    totalcalories = fields.Integer(basestring='Total Meal Calories', store=True, compute='_calc_calories')



class myModule_res_user_mealitems(models.Model):
    _name = "res.user.mealitem"

    meal_id  = fields.Many2one('res.user.meal')
    item_id  = fields.Many2one('product.template', 'Meal Items')
    servings = fields.Float('Serving')
    notes    = fields.Text('Meal Item Notes')
    calories = fields.Integer(related='item_id.calories', string='Calories Per Serving', store= True, readonly= True)






































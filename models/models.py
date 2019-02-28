# -*- coding: utf-8 -*-

from odoo import models, fields, api

class DietProducts(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    calories = fields.Integer('Calories')
    serving_size = fields.Float('Serving Size')
    diet_item = fields.Boolean('is it Diet Item ?')
    last_update = fields.Date('Last Update')
    nutrient_ids = fields.One2many('product.template.nutrient', 'product_id', 'Nutrient')

class ProductNutrient(models.Model):
    _name = 'product.nutrient'
    _description = 'Product Nutrient'

    name = fields.Char('Nutrient Name')
    uom_id = fields.Many2one('product.uom', 'Unit of Measure')
    description = fields.Text('Nutrient Description')

class ProductTemplateNutrient(models.Model):
    _name = 'product.template.nutrient'
    nutrient_id = fields.Many2one('product.nutrient', string='Nutrient')
    product_id = fields.Many2one('product.template', string='Diet Item')
    value = fields.Float('Value')
    daily_percentage = fields.Float('Daily Percentage')
    uom = fields.Char(related='nutrient_id.uom_id.name', string='Unit of Measure', readonly=False)

class DietMeal(models.Model):
    _name = 'res.users.meal'
    _description = 'User Diet Meal'

    name = fields.Char('Meal Name')
    user_id = fields.Many2one('res.users', 'Meal User')
    meal_date = fields.Datetime('Meal Date')
    notes = fields.Text('Meal Notes')
    items = fields.One2many('res.users.meal.items', 'meal_id')
    meal_calories = fields.Integer(string='Total Meal Calories', store=True, compute='_total_calories', readonly=True)
    items_count = fields.Integer(string='Number of Items', store =False, compute='_total_items', readonly=True)
    total_records = fields.Integer(string='Number of Meals', store = False, compute='_total_records', readonly=True)

    @api.one
    @api.depends('items')
    def _total_calories(self):
        currentCalories = 0
        for item in self.items:
            currentCalories = currentCalories + (item.item_calories * item.serving)
        self.meal_calories = currentCalories

    @api.multi
    def _total_items(self):
        self.items_count = len(self.items)

    @api.multi
    def _total_records(self):
        self.total_records = len(self)

class DietMeal_Items(models.Model):
    _name = 'res.users.meal.items'

    meal_id = fields.Many2one('res.users.meal', 'Meal ID')
    item_id = fields.Many2one('product.template', 'Meal Item')
    serving = fields.Float('Serving')
    notes = fields.Text('Meal Item Notes')
    item_calories = fields.Integer(related='item_id.calories', string='Calories Per Serving', store=True, readonly=True)


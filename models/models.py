# -*- coding: utf-8 -*-

from odoo import models, fields, api


class bike_rent(models.Model):
    _name = 'bike.rent'
    _description = 'basic class to hold bike rent info'

    bike_name = fields.Char("Bike Model Name")
    bike_description = fields.Text("Bike Description")
    customer_name = fields.Char("Customer Name")
    price = fields.Float("Bike Rent Price")
    rent_start = fields.Date("Start of Rent Date", default=fields.Date.today)
    rent_stop = fields.Date("End of Rent Date", default=fields.Date.today)
    notes = fields.Text("Rent Notes")
    image = fields.Binary("Bike Picture")


"""
Q:  classical view syntax vs new one
    list vs tree
    specific field for prices? 
"""

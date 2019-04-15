# -*- coding: utf-8 -*-

from odoo import models, fields


class BikeRent(models.Model):
    _name = 'bike.rent'
    _description = 'basic class to hold bike rent info'

    bike_name = fields.Char("Bike Model Name")
    bike_description = fields.Text("Bike Description")
    customer_name = fields.Char("Customer Name")
    price = fields.Float("Bike Rent Price")
    rent_start = fields.Datetime("Rent Start Time", default=fields.Datetime.now)
    rent_stop = fields.Datetime("End of Rent Time")
    notes = fields.Text("Rent Notes")
    image = fields.Binary("Bike Picture")
    name = fields.Char("Model name, mainly used for UI purposes", default="Rent Info")

# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BikeRent(models.Model):
    _name = 'bike.rent'
    _description = 'basic class to hold bike rent info'

    bike_id = fields.Many2one('product.product', string='Bike Model Name')
    bike_description = fields.Text(related='bike_id.description', string='Bike Description')
    image = fields.Binary(related='bike_id.image', string='Bike Picture')
    partner_id = fields.Many2one('res.partner', string='Customer Name')
    price = fields.Float(string='Bike Rent Price')
    rent_start = fields.Datetime(string='Rent Start Time', default=fields.Datetime.now, required=True)
    rent_stop = fields.Datetime(string='End of Rent Time', required=True)
    number_of_days = fields.Char(string='Total Rent Time', compute='_compute_days')
    notes = fields.Text(string='Rent Notes')
    name = fields.Char(string='Model name, mainly used for UI purposes', default='Rent Info')

    @api.depends('rent_start', 'rent_stop')
    def _compute_days(self):
        for record in self:
            if not record.rent_stop:
                record.number_of_days = '0'
            else:
                record.number_of_days = str(record.rent_stop - record.rent_start)

    @api.onchange('rent_start', 'rent_stop')
    def _verify_stop_date(self):
        if not self.rent_stop:
            pass
        elif self.rent_stop < self.rent_start:
            return {
                'warning': {
                    'title': "Incorrect End Date",
                    'message': "End date cannot be earlier then start date.",
                },
            }

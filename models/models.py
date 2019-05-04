# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo import exceptions


class BikeRent(models.Model):
    _name = 'bike.rent'
    _description = 'basic class to hold bike rent info'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    bike_id = fields.Many2one('product.product', string='Bike Model Name', required=True,
                              domain=[('is_bike', '=', True)])
    bike_description = fields.Text(related='bike_id.description', string='Bike Description', store=True)
    image = fields.Binary(related='bike_id.image', string='Bike Picture', store=True)
    partner_id = fields.Many2one('res.partner', string='Customer Name')
    price = fields.Float(string='Bike Rent Price')
    rent_start = fields.Datetime(string='Rent Start Time', default=fields.Datetime.now, required=True)
    rent_stop = fields.Datetime(string='End of Rent Time', required=True)
    rent_time = fields.Char(string='Total Rent Time', compute='_compute_time', store=True)
    notes = fields.Text(string='Rent Notes')
    name = fields.Char(string='Model name, mainly used for UI purposes', default='Rent Info')

    @api.depends('rent_start', 'rent_stop')
    def _compute_time(self):
        for record in self:
            if not record.rent_stop:
                record.rent_time = '0'
            else:
                record.rent_time = str(record.rent_stop - record.rent_start)

    @api.onchange('rent_start', 'rent_stop')
    def _onchange_verify_stop_date(self):
        if self.rent_stop and self.rent_stop < self.rent_start:
            raise exceptions.UserError('End of Rent Time cannot be earlier than Rent Start Time')


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_bike = fields.Boolean(string="It's a Bike", default=False)
    manufacturer = fields.Char(string='Manufacturer')
    model = fields.Char(string='Model')


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def company_rent_history(self):
        action = self.env.ref('bike_rent.bike_rent_tree_view')  # .search([('partner_id', '=', active_id)])
        print(action.id)
        return {
            'name': "Company Rent History",
            'type': 'ir.actions.act_window',
            'res_model': 'bike.rent',
            'view_mode': 'tree',
            'view_id': action.id,
            'domain': "['|', ('partner_id', '=', active_id), ('partner_id', 'child_of', active_id)]",
        }

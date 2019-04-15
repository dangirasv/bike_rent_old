# -*- coding: utf-8 -*-
from odoo import http

# class BikeRent(http.Controller):
#     @http.route('/bike_rent/bike_rent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bike_rent/bike_rent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bike_rent.listing', {
#             'root': '/bike_rent/bike_rent',
#             'objects': http.request.env['bike_rent.bike_rent'].search([]),
#         })

#     @http.route('/bike_rent/bike_rent/objects/<model("bike_rent.bike_rent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bike_rent.object', {
#             'object': obj
#         })

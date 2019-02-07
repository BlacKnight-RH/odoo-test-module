# -*- coding: utf-8 -*-
from odoo import http

# class CarReq(http.Controller):
#     @http.route('/car_req/car_req/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/car_req/car_req/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('car_req.listing', {
#             'root': '/car_req/car_req',
#             'objects': http.request.env['car_req.car_req'].search([]),
#         })

#     @http.route('/car_req/car_req/objects/<model("car_req.car_req"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('car_req.object', {
#             'object': obj
#         })
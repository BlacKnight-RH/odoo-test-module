# -*- coding: utf-8 -*-
from odoo import http

# class MyPos(http.Controller):
#     @http.route('/my_pos/my_pos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_pos/my_pos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_pos.listing', {
#             'root': '/my_pos/my_pos',
#             'objects': http.request.env['my_pos.my_pos'].search([]),
#         })

#     @http.route('/my_pos/my_pos/objects/<model("my_pos.my_pos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_pos.object', {
#             'object': obj
#         })
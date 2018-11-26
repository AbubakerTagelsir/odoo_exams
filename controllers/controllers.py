# -*- coding: utf-8 -*-
from openerp import http

# class Examination(http.Controller):
#     @http.route('/examination/examination/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/examination/examination/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('examination.listing', {
#             'root': '/examination/examination',
#             'objects': http.request.env['examination.examination'].search([]),
#         })

#     @http.route('/examination/examination/objects/<model("examination.examination"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('examination.object', {
#             'object': obj
#         })
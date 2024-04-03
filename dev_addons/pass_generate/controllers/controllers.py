# -*- coding: utf-8 -*-
# from odoo import http


# class PassGenerate(http.Controller):
#     @http.route('/pass_generate/pass_generate', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pass_generate/pass_generate/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pass_generate.listing', {
#             'root': '/pass_generate/pass_generate',
#             'objects': http.request.env['pass_generate.pass_generate'].search([]),
#         })

#     @http.route('/pass_generate/pass_generate/objects/<model("pass_generate.pass_generate"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pass_generate.object', {
#             'object': obj
#         })

import json
import logging
import werkzeug
import werkzeug.utils
from datetime import datetime
from math import ceil

import openerp.http as http
from openerp.http import request

class WebsiteSurvey(http.Controller):

    @http.route(['/survey/scores/<model("survey.survey"):survey>/<string:token>'],
                type='http', auth='public', website=True)
    def get_scores(self, survey, token, page=None, **post):
        cr, uid, context = request.cr, request.uid, request.context
        user_input_line_obj = request.registry['survey.user_input_line']
        ret = {}

        # Fetch answers
        ids = user_input_line_obj.search(cr, SUPERUSER_ID, [('user_input_id.token', '=', token)], context=context)
        previous_answers = user_input_line_obj.browse(cr, uid, ids, context=context)

        # Compute score for each question
        for answer in previous_answers:
            tmp_score = ret.get(answer.question_id.id, 0.0)
            ret.update({answer.question_id.id: tmp_score + answer.quizz_mark})
            if json.dumps(ret)<70:
                return "Fill"
            elif json.dumps(ret)>=70:
               return "Pass"
#
# # class Examination(http.Controller):
# #     @http.route('/examination/examination/', auth='public')
# #     def index(self, **kw):
# #         return "Hello, world"
#
# #     @http.route('/examination/examination/objects/', auth='public')
# #     def list(self, **kw):
# #         return http.request.render('examination.listing', {
# #             'root': '/examination/examination',
# #             'objects': http.request.env['examination.examination'].search([]),
# #         })
#
# #     @http.route('/examination/examination/objects/<model("examination.examination"):obj>/', auth='public')
# #     def object(self, obj, **kw):
# #         return http.request.render('examination.object', {
# #             'object': obj
# #         })
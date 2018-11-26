# -*- coding: utf-8 -*-
from openerp.osv import fields, osv

import datetime
import logging
import re
import uuid

class Examination(osv.Model):
    _inherit = "survey.survey"

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
#

class SurveyScore(osv.Model):
    _inherit = "survey.user_input"

    score = fields.selection([('fill','Fill'),('pass','Pass')],compute="compute_score")
    def compute_score(self, cr, uid, ids, name, args, context=None):

        if self.quizz_score<70:
            return self.score=="fill"
        elif self.quizz_score>=70:
            return self.score=="pass"





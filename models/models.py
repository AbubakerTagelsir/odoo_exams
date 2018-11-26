# -*- coding: utf-8 -*-
from openerp import models, fields, api
from openerp.osv import fields, osv
from openerp.tools.translate import _
from openerp import SUPERUSER_ID
from openerp.tools import DEFAULT_SERVER_DATETIME_FORMAT as DF
from openerp.addons.website.models.website import slug
from urlparse import urljoin
from itertools import product
from collections import Counter
from collections import OrderedDict
from openerp.exceptions import UserError

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





# -*- coding:utf-8 -*-

from accounts.models import user_profile
from forum.models import question

from django.db import models
from django.utils.translation import ugettext_lazy as _

class question_voting (models.Model):
	voted = models.ForeignKey(question, null=False)
	voter = models.ForeignKey(user_profile, null=False)
	change = models.IntegerField(blank=False)
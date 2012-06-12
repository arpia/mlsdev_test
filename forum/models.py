# -*- coding:utf-8 -*-

import datetime

from accounts.models import user_profile
from voting.models import *

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

class question (models.Model):
	title = models.CharField(_(u'Title'), blank=False, max_length=50)
	body = models.TextField(_(u'Body'))
	sender = models.ForeignKey(user_profile, null=False)
	rating = models.BigIntegerField(_(u'Rating'), blank=False, default=0)
	view_count = models.BigIntegerField(_(u'View count'), blank=False, default=0)
	answer_count = models.BigIntegerField(_(u'Answer count'), blank=False, default=0)
	date = models.DateField(_(u'Date'), default=datetime.date.today)

	tags = models.ManyToManyField('tag', null=True, blank=True)

	def delete(self):
		for answer in self.answer_set.all():
			for vote in answer.answer_voting_set.all():
				vote.delete()
			answer.delete()
		for vote in self.question_voting_set.all():
			vote.delete()
		for tag in self.tags.all():
			tag.dec()
		super(question, self).delete()

	def inc_view (self):
		self.view_count += 1
		super(question, self).save()

	def inc_answers (self):
		self.answer_count += 1
		super(question, self).save()

	def vote (self, change):
		self.rating += change
		super(question, self).save()

	class Meta:
		verbose_name = _(u'question')
		verbose_name_plural = _(u'questions')


class answer (models.Model):
	question = models.ForeignKey(question, null=False)
	answer_body = models.TextField(_(u'Answer'), blank=False)
	sender = models.ForeignKey(user_profile, null=False)
	rating = models.BigIntegerField(_(u'Rating'), blank=False, default=0)

	def vote (self, change):
		self.rating += change
		super(answer, self).save()

	class Meta:
		verbose_name = _(u'answer')
		verbose_name_plural = _(u'answers')


class comment (models.Model):
	answer = models.ForeignKey(answer, null=False)
	body = models.TextField(_(u'Body'), null=False)

	class Meta:
		verbose_name = _(u'comment')
		verbose_name_plural = _(u'comments')


class tag (models.Model):
	title = models.CharField(_('Title'), blank=False, max_length=10, unique=True)
	count = models.IntegerField(blank=False, default=0)

	def __unicode__ (self):
		return self.title

	def set_count (self, change):
		self.count = change
		super(tag, self).save()

	def dec (self):
		self.count -= 1
		super(tag, self).save()

	class Meta:
		verbose_name = _(u'tag')
		verbose_name_plural = _(u'tags')



admin.site.register(question)
admin.site.register(answer)
admin.site.register(comment)
admin.site.register(tag)
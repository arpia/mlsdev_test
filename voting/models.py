# -*- coding:utf-8 -*-
# Хотел сделать нормально через ManyToManyField.
# Но из-за того, что будут корявости у модели user_profile при обратной связи (question_set), не сделал.
# (Надо же брать связи и по полю sender и по многие-к-многим)
# А "портить" модель пользователя не хотелось.

#необходимо оптимизировать - слишком много повторяющегося кода
#сделать наследование от одной общей модели

from accounts.models import user_profile
from forum.models import question, answer

from django.db import models
from django.contrib import admin

class question_voting (models.Model):
	voted = models.ForeignKey(question, null=False)
	voter = models.ForeignKey(user_profile, null=False)
	change = models.IntegerField(blank=False, default=0)

	def voteup (self):
		if self.change == 0:
			self.voted.vote(1)
		if self.change == -1:
			self.voted.vote(2)
		self.change = 1
		super(question_voting, self).save()

	def votedown (self):
		if self.change == 0:
			self.voted.vote(-1)
		if self.change == 1:
			self.voted.vote(-2)
		self.change = -1
		super(question_voting, self).save()


class answer_voting (models.Model):
	voted = models.ForeignKey(answer, null=False)
	voter = models.ForeignKey(user_profile, null=False)
	change = models.IntegerField(blank=False, default=0)

	def voteup (self):
		if self.change == 0:
			self.voted.vote(1)
		if self.change == -1:
			self.voted.vote(2)
		self.change = 1
		super(answer_voting, self).save()

	def votedown (self):
		if self.change == 0:
			self.voted.vote(-1)
		if self.change == 1:
			self.voted.vote(-2)
		self.change = -1
		super(answer_voting, self).save()


admin.site.register(question_voting)
admin.site.register(answer_voting)
# -*- coding:utf-8 -*-

from models import question, answer

from django import forms
from django.utils.translation import ugettext_lazy as _

class answer_form (forms.ModelForm):
	# question_id = forms.CharField(label=_(u'Question'), widget=forms.HiddenInput(), max_length=3)
	
	class Meta:
		model = answer
		exclude = ('rating', )
		widgets = {
			'question': forms.HiddenInput()
		}

	# def save (self, commit=True):
	# 	self.fields['question'].value = question.objects.get(id=self.cleaned_data.get('question_id'))
	# 	return super(answer_form, self).save(commit)
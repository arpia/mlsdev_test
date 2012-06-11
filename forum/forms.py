# -*- coding:utf-8 -*-

from models import question, answer

from django import forms
from django.utils.translation import ugettext_lazy as _

class answer_form (forms.ModelForm):
	class Meta:
		model = answer
		exclude = ('rating', )
		widgets = {
			'question': forms.HiddenInput(),
			'sender': forms.HiddenInput()
		}


class question_form (forms.ModelForm):
    class Meta:
        model = question
        fields = ('title', 'body', 'sender', 'tags', )
        widgets = {
			'sender': forms.HiddenInput(),
			# 'tags': forms.CheckboxSelectMultiple()
		}
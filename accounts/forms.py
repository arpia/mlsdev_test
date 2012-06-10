# -*- coding:utf-8 -*-

from models import user_profile

from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, login
from captcha.fields import CaptchaField

class registration_form (forms.ModelForm):
    captcha = CaptchaField()
    username = forms.CharField(label=_(u'Login'), max_length=8)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput, max_length=8)
    password_again = forms.CharField(label=_(u'Password again'), widget=forms.PasswordInput, max_length=8)

    class Meta:
        model = user_profile
        fields = ('username', 'password', 'password_again', 'avatar', 'first_name', 'last_name', 'gender', 'date_birth', 'email', 'jabber', 'captcha', )

    def clean (self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        password_again = self.cleaned_data.get('password_again')

        try:
            User.objects.get(username=username)
            if 'username' not in self._errors:
                self._errors['username'] = []
            self._errors['username'].append(_(u'This login already exists'))
        except User.DoesNotExist:
            'it\'s ok'

        if password != password_again:
            raise forms.ValidationError(_(u'Passwords does not match'))

        return self.cleaned_data

    def save (self, commit=True):
        user = super(registration_form, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user


class login_form (forms.Form):
    username = forms.CharField(label=_(u'Login'), max_length=8)
    password = forms.CharField(label=_(u'Password'), widget=forms.PasswordInput, max_length=8)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super(login_form, self).__init__(*args, **kwargs)

    def clean (self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        try:
            profile = User.objects.get(username=username)
        except User.DoesNotExist:
            if 'username' not in self._errors:
                self._errors['username'] = []
            self._errors['username'].append(_(u'Wrong username'))

        self.user_cache = authenticate(username=username, password=password)
        if self.user_cache is None:
            if 'password' not in self._errors:
                self._errors['password'] = []
            self._errors['password'].append(_(u'Wrong password'))

        return self.cleaned_data

    def get_user (self):
        return self.user_cache
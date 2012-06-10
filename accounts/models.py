# -*- coding:utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from sorl.thumbnail import ImageField
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
    (u'm', _(u'Male')),
    (u'f', _(u'Female')),
    (u'o', _(u'Other')),
)

class user_profile (User):
    date_birth = models.DateField(_(u'Birth date'), blank=True)
    gender = models.CharField(_(u'Sex'), max_length=1, choices=GENDER_CHOICES, blank=True)
    jabber = models.CharField(u'jabber', max_length=30, blank=True)
    avatar = ImageField(_(u'Avatar'), upload_to='avatars', blank=True, default='no_ava.png')

    class Meta:
        verbose_name = _(u'user profile')
        verbose_name_plural = _(u'user profiles')


admin.site.register(user_profile)

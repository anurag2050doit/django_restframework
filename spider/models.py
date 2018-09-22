# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class ApiKeys(models.Model):
    api_key = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    working = models.BooleanField(default=False)
    api_url = models.URLField()

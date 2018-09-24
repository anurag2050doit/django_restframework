# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from services import models

admin.register(models.Group)
admin.register(models.Photos)
admin.register(models.Tags)

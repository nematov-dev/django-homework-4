from django.contrib import admin

from . import models


admin.site.register(models.Blogger)
admin.site.register(models.Post)

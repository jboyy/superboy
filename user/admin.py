from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user import models
# Register your models here.
admin.site.register(models.Profile)


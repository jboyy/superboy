from django.contrib import admin
from blogcomment import models
# Register your models here.
admin.site.register(models.blog)
admin.site.register(models.BlogComment)


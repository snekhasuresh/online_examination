from django.contrib import admin
from exam import models
# Register your models here.
admin.site.register(models.Course)
admin.site.register(models.Question)
admin.site.register(models.Result)
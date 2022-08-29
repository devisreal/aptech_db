from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Courses)
class CourseAdmin(admin.ModelAdmin):
   list_display =('name', 'duration', 'price')
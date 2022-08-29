from django.contrib import admin
from . import models

@admin.register(models.Staff)
class StaffAdmin(admin.ModelAdmin):
   pass
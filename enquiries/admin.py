from django.contrib import admin
from . import models

@admin.register(models.Enquires)
class EnquiryAdmin(admin.ModelAdmin):
   pass
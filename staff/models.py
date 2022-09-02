from django.db import models
from django.template.defaultfilters import slugify

class Staff(models.Model):
   name = models.CharField(max_length=250)
   contact_no = models.CharField(max_length=14, blank=True)
   email = models.EmailField(max_length=200,blank=True)
   role = models.CharField(max_length=50, blank=True)   
   slug = models.SlugField(null=True, blank=True)
   date_employed = models.DateField(blank=True, null=True)
   
   def __str__(self):
      return self.name

   def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)

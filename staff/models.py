from django.db import models


class Staff(models.Model):
   name = models.CharField(max_length=200)
   contact_no = models.CharField(max_length=14, blank=True)
   email = models.EmailField(blank=True)
   role = models.CharField(max_length=50, blank=True)   

   def __str__(self):
      return self.name

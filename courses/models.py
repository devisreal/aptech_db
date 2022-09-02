from django.db import models

class Courses(models.Model):
   name = models.CharField(max_length=300)
   duration = models.CharField(max_length=20)
   description = models.TextField(blank=True)
   price = models.PositiveBigIntegerField(blank=True)   

   def __str__(self):
      return self.name

   class Meta:
      verbose_name = 'Course'
      verbose_name_plural = 'Courses'

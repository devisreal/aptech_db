from django.db import models
from courses.models import Courses

class Student(models.Model):
   gender_choices =  (      
      ('Male', 'Male'),
      ('Female', 'Female'),
      ('Other', 'Other'),      
   )
   studentId = models.CharField(max_length=20)
   first_name = models.CharField(max_length=200)
   middle_name = models.CharField(max_length=200, blank=True)
   last_name = models.CharField(max_length=200)
   gender = models.CharField(max_length=50, choices=gender_choices)
   email = models.EmailField(max_length=200, blank=True)
   date_of_birth =  models.DateField(blank=True, null=True)
   address = models.CharField(max_length=200, blank=True)
   contact_no = models.CharField(max_length=14, blank=True)
   guardians_name = models.CharField(max_length=200, blank=True)
   guardians_contact_no = models.CharField(max_length=14, blank=True)
   courses = models.ManyToManyField(Courses)
   completed_programs = models.BooleanField(default=False, blank=True)

   def __str__(self):
      return f'{self.first_name} {self.last_name}'
   
   class Meta:
      verbose_name = 'Student'
      verbose_name_plural = 'Students'
   
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models

@login_required
def courses(request):
   all_courses = models.Courses.objects.all()

   context = {
      'all_courses': all_courses
   }
   return render(request, 'courses/courses.html', context)
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models

@login_required
def courses(request):
   all_courses = models.Courses.objects.all()

   if request.method == 'POST':
      course_name = request.POST['course_name']
      course_duration = request.POST['course_duration']
      course_description = request.POST['course_description']
      course_price = request.POST['course_price']

      if not course_name and course_duration and course_description and course_price:
         messages.error(request, 'Enter complete details !')
      else:
         new_course = models.Courses(
            name=course_name,
            duration=course_duration,
            description=course_description,
            price=course_price
         )
         new_course.save()
         messages.success(request, 'New Course Added!')
         return redirect(request.META.get('HTTP_REFERER'))
      
   context = {
      'all_courses': all_courses
   }
   return render(request, 'courses/courses.html', context)


@login_required
def delete_course(request, id):
   course = models.Courses.objects.get(id=id)
   course.delete()
   messages.success(request, 'Course Deleted!')
   return redirect(request.META.get('HTTP_REFERER'))
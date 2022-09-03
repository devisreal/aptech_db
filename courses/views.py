from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models
from .forms import EditCourseForm


@login_required
def courses(request):
   all_courses = models.Courses.objects.all()

   if request.method == 'POST':
      course_name = request.POST['course_name']
      course_duration = request.POST['course_duration']
      course_description = request.POST['course_description']
      course_price = request.POST['course_price']

      if not course_name and course_duration and course_price:
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
   try:
      course = models.Courses.objects.get(id=id)
   except models.Courses.DoesNotExist:
      messages.error(request, f"Course does not exist")
      return redirect('courses')
   course.delete()
   messages.success(request, 'Course Deleted!')
   return redirect('courses')


@login_required
def course_detail(request, id):
   try:
      course = models.Courses.objects.get(id=id)
   except models.Courses.DoesNotExist:
      messages.error(request, f"Course does not exist")
      return redirect('courses')
   if request.method == "POST":
      edit_course_form = EditCourseForm(request.POST, instance=course)
      if edit_course_form.is_valid():
         edit_course_form.save()
         messages.success(request, 'Course updated!')
         return redirect('course_detail', id=id)
      else:
         messages.error(request, 'An error occured, please try again')
   else:
      edit_course_form = EditCourseForm(instance=course)

   context = {
      'course': course,
      'edit_course_form': edit_course_form
   }   
   return render(request, 'courses/course_detail.html', context)
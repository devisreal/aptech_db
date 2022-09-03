from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from courses import models as courses_models
from django.db.models import Q
from django.contrib import messages
from courses.models import Courses
from students.models import Student
from enquiries.models import Enquires
from staff.models import Staff

@login_required
def dashboard(request):
   courses_count = Courses.objects.all().count()
   students_count = Student.objects.all().count()
   staff_count = Staff.objects.all().count()
   month_enquiries = Enquires.objects.all().count()
   context = {
      'courses_count': courses_count,
      'students_count': students_count,
      'staff_count': staff_count,
      'month_enquiries': month_enquiries
   }
   return render(request, 'project/dashboard.html', context)


@login_required
def search(request):

   if 'key' in request.GET:
      key=request.GET['key']
      if key:
         courses = courses_models.Courses.objects.filter(
            Q(name__icontains=key),
            Q(duration__icontains=key),
            Q(price__icontains=key),            
         )
         if courses:
            return render(request, 'project/search.html', {'courses': courses})
         else:
            return render(request, 'project/search.html')
      
   messages.error(request, 'Please enter a search item!')
   return redirect('dashboard')

@login_required
def admin_settings(request):
   return render(request, 'project/settings.html')

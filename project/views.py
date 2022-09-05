from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from courses.models import Courses
from students.models import Student
from enquiries.models import Enquires
from staff.models import Staff
from datetime import date


@login_required
def dashboard(request):
    courses_count = Courses.objects.all().count()
    students_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    current_month = date.today().month
    current_year = date.today().year
    month_enquiries = Enquires.objects.filter(
        date__year=current_year,
        date__month=current_month
    ).count()

    students = Student.objects.all().order_by("date_enrolled")

    students_enrolled = [
        {'date': '01', 'num': 0, 'num_prev': 0},
        {'date': '02', 'num': 0, 'num_prev': 0},
        {'date': '03', 'num': 0, 'num_prev': 0},
        {'date': '04', 'num': 0, 'num_prev': 0},
        {'date': '05', 'num': 0, 'num_prev': 0},
        {'date': '06', 'num': 0, 'num_prev': 0},
        {'date': '07', 'num': 0, 'num_prev': 0},
        {'date': '08', 'num': 0, 'num_prev': 0},
        {'date': '09', 'num': 0, 'num_prev': 0},
        {'date': '10', 'num': 0, 'num_prev': 0},
        {'date': '11', 'num': 0, 'num_prev': 0},
        {'date': '12', 'num': 0, 'num_prev': 0}
    ]
    students_this_month = 0
    students_this_year = 0
    students_last_year = 0
    loop_index = 0

    for student in students:
        if student.date_enrolled.strftime("%Y") == datetime.now().strftime("%Y"):
            students_this_year += 1

            for student_enrolled in students_enrolled:
                if student_enrolled['date'] == student.date_enrolled.strftime("%m"):
                    student_enrolled['num'] += 1

                    if student_enrolled['date'] == datetime.now().strftime("%m"):
                        students_this_month += 1

        elif int(student.date_enrolled.strftime("%Y")) == datetime.now().year - 1:
            students_last_year += 1

            for student_enrolled in students_enrolled:
                if student_enrolled['date'] == student.date_enrolled.strftime("%m"):
                    student_enrolled['num_prev'] += 1

                    if student_enrolled['date'] == datetime.now().strftime("%m"):
                        students_this_month += 1

    context = {
        'courses_count': courses_count,
        'students_count': students_count,
        'staff_count': staff_count,
        'month_enquiries': month_enquiries,
        'students_this_month': students_this_month,
        'students_enrolled': students_enrolled,
        'students_this_year': students_this_year,
        'students_last_year': students_last_year,
    }
    return render(request, 'project/dashboard.html', context)     



@login_required
def search(request):


   if 'key' in request.GET:
      key=request.GET['key']
      if key:
         search_courses = Courses.objects.filter(
            Q(name__icontains=key) |
            Q(duration__icontains=key) |
            Q(price__icontains=key)         
         )
         search_students = Student.objects.filter(
            Q(studentId__icontains=key) |
            Q(first_name__icontains=key) |
            Q(middle_name__icontains=key) |
            Q(last_name__icontains=key) |
            Q(gender__icontains=key) |
            Q(email__icontains=key) |
            Q(contact_no__icontains=key) |
            Q(guardians_name__icontains=key) |
            Q(guardians_contact_no__icontains=key) |
            Q(address__icontains=key) |
            Q(date_enrolled__icontains=key)            
         )
         search_staffs = Staff.objects.filter(
            Q(name__icontains=key) |
            Q(contact_no__icontains=key) |
            Q(email__icontains=key) |
            Q(role__icontains=key) |
            Q(date_employed__icontains=key)
         )
         if search_courses or search_students or search_staffs:
            context = {
               'search_courses': search_courses,
               'search_students': search_students,
               'search_staffs': search_staffs
            }
            return render(request, 'project/search.html', context)
         else:
            return render(request, 'project/search.html')            
      else:
         messages.error(request, 'Please enter a search item!')
         return redirect('dashboard')
   else:
      messages.error(request, 'Please enter a search item!')
      return redirect('dashboard')

@login_required
def admin_settings(request):
    return render(request, 'project/settings.html')

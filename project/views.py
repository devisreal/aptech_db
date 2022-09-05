from datetime import datetime
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
        key = request.GET['key']
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

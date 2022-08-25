from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
   return render(request, 'project/dashboard.html')


@login_required
def courses(request):
   return render(request, 'project/courses.html')


@login_required
def students(request):
   return render(request, 'project/students.html')


@login_required
def staffs(request):
   return render(request, 'project/staffs.html')


@login_required
def enquiries(request):
   return render(request, 'project/enquiries.html')


@login_required
def search(request):
   return render(request, 'project/search.html')
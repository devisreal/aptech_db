from django.shortcuts import render


# Create your views here.
def login(request):
   return render(request, 'project/login.html')

def dashboard(request):
   return render(request, 'project/dashboard.html')

def courses(request):
   return render(request, 'project/courses.html')

def students(request):
   return render(request, 'project/students.html')

def staffs(request):
   return render(request, 'project/staffs.html')

def enquiries(request):
   return render(request, 'project/enquiries.html')

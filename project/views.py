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

def faculty(request):
   return render(request, 'project/faculty.html')



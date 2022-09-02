from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddStudentForm
from django.contrib import messages

@login_required
def students(request):
   return render(request, 'students/students.html')

@login_required
def register_student(request):
   if request.method == 'POST':
      add_student_form = AddStudentForm(request.POST)
      if add_student_form.is_valid():
         add_student_form.save()
         messages.success(request, 'Student Registered!')
         return redirect('students')
      else:
         messages.error(request, 'An error occured, please try again')
   else:
      add_student_form = AddStudentForm()
   context = {
      'add_student_form': add_student_form
   }
   return render(request, 'students/register_student.html', context)
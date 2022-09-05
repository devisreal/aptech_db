from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AddStudentForm
from django.contrib import messages
from . import models

@login_required
def students(request):
   all_students = models.Student.objects.all().order_by('last_name').values()

   context = {
      'all_students': all_students
   }
   return render(request, 'students/students.html', context)


@login_required
def student_detail(request, slug):

   try:
      student = models.Student.objects.get(slug=slug)
   except models.Student.DoesNotExist:
      messages.error(request, f"Student '{slug}' does not exist")
      return redirect('students')

   context = {
      'student': student
   }
   return render(request, 'students/student_detail.html', context)


@login_required
def update_student(request, slug):
   try:
      student = models.Student.objects.get(slug=slug)
   except models.Student.DoesNotExist:
      messages.error(request, f"Student '{slug}' does not exist")
      return redirect('students')

   if request.method == 'POST':
      edit_student_form = AddStudentForm(request.POST, instance=student)
      if edit_student_form.is_valid():
         edit_student_form.save()
         messages.success(request, 'Student Details Updated!')
         return redirect('students')
      else:
         messages.error(request, 'An error occured, please try again')
   else:
      edit_student_form = AddStudentForm(instance=student)

   context = {
      'student': student,
      'edit_student_form': edit_student_form
   }
   return render(request, 'students/update_student.html', context)

@login_required
def set_program_completed(request, slug):
   try:
      student = models.Student.objects.get(slug=slug)
   except models.Student.DoesNotExist:
      messages.error(request, f"Student '{slug}' does not exist")
      return redirect('students')

   student.completed_programs = True
   student.save()
   messages.success(request, f"Student {slug} program completed!")
   return redirect(request.META.get('HTTP_REFERER'))
      

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


@login_required
def delete_student(request, slug):
   try:
      student = models.Student.objects.get(slug=slug)
   except models.Student.DoesNotExist:
      messages.error(request, f"Student '{slug}' does not exist")
      return redirect('students')
   student.delete()
   messages.success(request, 'Student Deleted!')
   return redirect('students')
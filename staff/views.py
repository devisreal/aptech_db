from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib import messages
from .forms import EditStaffForm


@login_required
def staffs(request):

   all_staffs = models.Staff.objects.all()
   staff_count =  all_staffs.count()
   if request.method == 'POST':
      staff_name = request.POST['staff_name']
      contact_no = request.POST['contact_no']
      email = request.POST['email']
      role = request.POST['role']
      date_employed = request.POST['date_employed']      

      if not staff_name and contact_no:
         messages.error(request, 'Enter complete details !')
      else:
         new_staff = models.Staff(
            name=staff_name,
            contact_no=contact_no,
            email=email,
            role=role,
            date_employed=date_employed
         )
         new_staff.save()
         messages.success(request, 'New Staff Added!')
         return redirect(request.META.get('HTTP_REFERER'))
   context = {
      'all_staffs': all_staffs,  
      'staff_count': staff_count
   }
   return render(request, 'staff/staffs.html', context)

def staff_detail(request, slug):

   try:
      staff = models.Staff.objects.get(slug=slug)
   except models.Staff.DoesNotExist:
      messages.error(request, f"Staff '{slug}' does not exist")
      return redirect('staffs')
   
   if request.method == "POST":
      edit_staff_form = EditStaffForm(request.POST, instance=staff)
      if edit_staff_form.is_valid():
         edit_staff_form.save()
         messages.success(request, 'Staff details updated!')
         return redirect('staff_detail', slug=slug)
      else:
         messages.error(request, 'An error occured, please try again')
   else:
      edit_staff_form = EditStaffForm(instance=staff)
   context = {
      'staff': staff,
      'edit_staff_form': edit_staff_form
   }
   return render(request, 'staff/staff_detail.html', context)

def delete_staff(request, slug):
   try:
      staff = models.Staff.objects.get(slug=slug)
   except models.Staff.DoesNotExist:
      messages.error(request, f"Staff '{slug}' does not exist")
      return redirect('staffs')
   staff.delete()
   messages.success(request, 'Staff Deleted!')
   return redirect('staffs')
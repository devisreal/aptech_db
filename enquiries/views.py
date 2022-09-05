from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from . import models
from datetime import date
from .forms import AddEnquiryForm

@login_required
def enquiries(request):
   all_enquiries = models.Enquires.objects.all()
   enquiries_count = all_enquiries.count()

   context = {
      'all_enquiries': all_enquiries,
      'enquiries_count': enquiries_count,
      'current_month': date.today().year
   }
   return render(request, 'enquiries/enquiries.html', context)


def add_enquiry(request):
   if request.method == 'POST':
      add_enquiry_form = AddEnquiryForm(request.POST)
      if add_enquiry_form.is_valid():
         add_enquiry_form.save()
         messages.success(request, 'Enquiry Added!')
         return redirect('enquiries')
      else:
         messages.error(request, 'An error occured, please try again')
   else:
      add_enquiry_form = AddEnquiryForm()      
   context = {
      'add_enquiry_form': add_enquiry_form
   }
   return render(request, 'enquiries/add_enquiry.html', context)


def enquiry_detail(request, slug):
   try:
      enquiry = models.Enquires.objects.get(slug=slug)
   except models.Enquires.DoesNotExist:
      messages.error(request, f"Enquiry does not exist")
      return redirect('enquiries')
   context = {
      'enquiry': enquiry
   }
   return render(request, 'enquiries/enquiry_detail.html', context)


def update_enquiry(request, slug):
   try:
      enquiry = models.Enquires.objects.get(slug=slug)
   except models.Enquires.DoesNotExist:
      messages.error(request, f"Enquiry does not exist")
      return redirect('enquiries')

   if request.method == 'POST':
      edit_enquiry_form = AddEnquiryForm(request.POST, instance=enquiry)
      if edit_enquiry_form.is_valid():
         edit_enquiry_form.save()
         messages.success(request, 'Enquiry Details Updated!')
         return redirect('enquiries')
      else:
         messages.error(request, 'An error occured, please try again')
   else:
      edit_enquiry_form = AddEnquiryForm(instance=enquiry)
   context = {
      'enquiry': enquiry,
      'edit_enquiry_form': edit_enquiry_form
   }
   return render(request, 'enquiries/update_enquiry.html', context)

def delete_enquiry(request, slug):
   try:
      enquiry = models.Enquires.objects.get(slug=slug)
   except models.Enquires.DoesNotExist:
      messages.error(request, f"Enquiry does not exist")
      return redirect('enquiries')
   enquiry.delete()
   messages.success(request, 'Enquiry Deleted!')
   return redirect('enquiries')
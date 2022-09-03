from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from . import models
from .forms import AddEnquiryForm

@login_required
def enquiries(request):
   all_enquiries = models.Enquires.objects.all()

   context = {
      'all_enquiries': all_enquiries
   }
   return render(request, 'enquiries/enquiries.html', context)


def add_enquiry(request):
   add_enquiry_form = AddEnquiryForm()
   context = {
      'add_enquiry_form': add_enquiry_form
   }
   return render(request, 'enquiries/add_enquiry.html', context)
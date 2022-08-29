from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def enquiries(request):
   return render(request, 'enquiries/enquiries.html')


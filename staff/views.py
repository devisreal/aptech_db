from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



@login_required
def staffs(request):
   return render(request, 'staff/staffs.html')



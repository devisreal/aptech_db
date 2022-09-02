from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models

@login_required
def dashboard(request):
   return render(request, 'project/dashboard.html')


@login_required
def search(request):
   return render(request, 'project/search.html')

@login_required
def admin_settings(request):
   return render(request, 'project/settings.html')

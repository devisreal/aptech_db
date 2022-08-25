from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login(request):
   return render(request, 'account/login.html')


@login_required
def user_logout(request):
   # Logout user
   logout(request)
   # Return success message
   # messages.info(request, 'See you soon 🙂')
    # Redirect to home page
   return redirect(request.META.get('HTTP_REFERER'))
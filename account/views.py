from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def login(request):
    if request.method == 'POST':
        username_or_email = request.POST['username_or_email']
        password = request.POST['password']

        if User.objects.filter(username=username_or_email).exists():
            username = username_or_email
        elif User.objects.filter(email=username_or_email).exists():
            username = User.objects.get(email=username_or_email).username
        else:
            username = None

        if username is not None:
            try:
                user = authenticate(username=username, password=password)
                auth.login(request, user)
                messages.success(request, "You're successfully logged in.")
                return redirect('dashboard')
            except:
                messages.error(request, "Incorrect password.")
                return redirect('login')
        else:
            messages.error(request, "User does not exist.")
            return redirect('login')

    return render(request, 'account/login.html')


@login_required
def user_logout(request):
    # Logout user
    logout(request)
    # Return success message
    # messages.info(request, 'See you soon 🙂')
    # Redirect to home page
    return redirect(request.META.get('HTTP_REFERER'))

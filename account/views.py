from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in!')
        return redirect('dashboard')
    else:
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
    logout(request)
    # Return success message
    messages.success(request, 'See you soon!')    
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def edit_profile(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        user = User.objects.get(id=request.user.id)
        
        if username is not None and email is not None:
            user.username = username
            user.email = email
            user.save()
            return redirect('admin_settings')
        else:
            messages.error(request, "Please fill in all the fields provided.")
            return redirect('admin_settings')
    else:
        return redirect('admin_settings')

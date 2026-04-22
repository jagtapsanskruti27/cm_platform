from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import UserProfile


def home(request):
    if request.user.is_authenticated:
        return redirect('/feed/')
    return render(request, 'home.html')


def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        UserProfile.objects.create(user=user)

        return redirect('/login/')

    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect('/feed/')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid Username or Password'
            })

    return render(request, 'login.html')


def profile_view(request):
    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

        context = {
            'username': request.user.username,
            'email': request.user.email,
            'bio': profile.bio
        }

        return render(request, 'profile.html', context)

    return redirect('/login/')


def logout_view(request):
    logout(request)
    return redirect('/login/') 
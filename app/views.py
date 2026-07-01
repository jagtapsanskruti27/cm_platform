from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Follow
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from post.models import Post
# from django.shortcuts import render
# from .forms import ProfileForm


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

        Profile.objects.create(user=user)

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

        profile = Profile.objects.get(user=request.user)

        post_count = Post.objects.filter(
            user=request.user
        ).count()

        followers_count = Follow.objects.filter(
        following=request.user
        ).count()

        following_count = Follow.objects.filter(
        follower=request.user
        ).count()

        context = {
            'username': request.user.username,
            'email': request.user.email,
            'bio': profile.bio,
            'post_count': post_count,
            'followers_count': followers_count,
            'following_count': following_count,
            'profile': profile
            
        }

        return render(request, 'profile.html', context)

    return redirect('/login/')

def logout_view(request):
    logout(request)
    return redirect('/login/') 

@login_required
def edit_profile(request):

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('/profile/')

    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        'edit_profile.html',
        {'form': form}
    )

@login_required
def follow_user(request, user_id):

    user_to_follow = User.objects.get(id=user_id)

    if user_to_follow != request.user:
        Follow.objects.get_or_create(
            follower=request.user,
            following=user_to_follow
        )

    return redirect('/profile/')    
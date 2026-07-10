from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Profile, Follow
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from post.models import Post
from django.core.mail import send_mail
from django.core import signing
from django.urls import reverse
from django.conf import settings
# from django.shortcuts import render
# from .forms import ProfileForm


def home(request):
    return render(request, "home.html")

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if not username or not email or not password:
            return render(request, 'register.html', {
                'error': 'All fields are required'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=False
        )

        return redirect('/login/')

    return render(request, 'register.html')


def admin_register_view(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        if not username or not email or not password:
            return render(request, 'admin_register.html', {
                'error': 'All fields are required'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'admin_register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            is_staff=True,
            is_active=False
        )

        # Generate a secure cryptographic signed token containing username
        token = signing.dumps({'username': username})

        # Build absolute approval URL
        approval_url = request.build_absolute_uri(reverse('admin_approve', args=[token]))

        # Construct email parameters
        subject = f"ACTION REQUIRED: Approve Admin Registration for '{username}'"
        message = (
            f"Hello,\n\n"
            f"A new admin registration request has been submitted for Nexus:\n\n"
            f"Username: {username}\n"
            f"Email: {email}\n\n"
            f"To approve this registration and activate the administrator account, please click the link below:\n"
            f"{approval_url}\n\n"
            f"This link is valid for 24 hours.\n\n"
            f"If you did not authorize this, you can ignore this email. The account will remain inactive.\n\n"
            f"Best regards,\n"
            f"Nexus System"
        )
        
        target_email = getattr(settings, 'ADMIN_APPROVAL_EMAIL', '')
        email_sent = False
        if target_email:
            try:
                send_mail(
                    subject,
                    message,
                    settings.EMAIL_HOST_USER or 'noreply@nexus.com',
                    [target_email],
                    fail_silently=False,
                )
                email_sent = True
            except Exception as e:
                print(f"Error sending admin approval email: {e}")

        return render(request, 'admin_register.html', {
            'success': 'Registration submitted successfully! Your administrator account is currently pending activation. A verification link has been sent to the primary administrator.'
        })

    return render(request, 'admin_register.html')


def admin_approve_view(request, token):
    try:
        # Link valid for 24 hours (86400 seconds)
        data = signing.loads(token, max_age=86400)
        username = data.get('username')
        
        user = User.objects.get(username=username, is_staff=True)
        if user.is_active:
            message = f"Administrator account '{username}' is already active!"
            already_active = True
        else:
            user.is_active = True
            user.save()
            message = f"Administrator account '{username}' has been successfully activated!"
            already_active = False
            
        return render(request, 'admin_approved.html', {
            'success': True,
            'message': message,
            'username': username,
            'already_active': already_active
        })
        
    except signing.SignatureExpired:
        return render(request, 'admin_approved.html', {
            'success': False,
            'error': 'This approval link has expired (links are valid for 24 hours).'
        })
    except (signing.BadSignature, User.DoesNotExist):
        return render(request, 'admin_approved.html', {
            'success': False,
            'error': 'Invalid approval token or the user does not exist.'
        })


def login_view(request):

    if request.user.is_authenticated:
        if request.user.is_staff:
            return redirect("admin_dashboard")
        return redirect("feed")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            if user.is_staff:
                return render(
                    request,
                    "login.html",
                    {
                        "error": "Please use the Admin Login page."
                    }
                )

            login(request, user)
            return redirect("feed")

        return render(
            request,
            "login.html",
            {
                "error": "Invalid username or password."
            }
        )

    return render(request, "login.html")


def admin_login_view(request):

    if request.user.is_authenticated:

        if request.user.is_staff:
            return redirect("admin_dashboard")

        return redirect("feed")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is None:

            return render(
                request,
                "admin_login.html",
                {
                    "error": "Invalid username or password."
                }
            )

        if not user.is_staff:

            return render(
                request,
                "admin_login.html",
                {
                    "error": "You are not an administrator."
                }
            )

        login(request, user)

        return redirect("admin_dashboard")

    return render(request, "admin_login.html")

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






# @login_required
# def dashboard(request):

#     post_count = Post.objects.filter(user=request.user).count()

#     followers_count = Follow.objects.filter(
#         following=request.user
#     ).count()

#     following_count = Follow.objects.filter(
#         follower=request.user
#     ).count()

#     context = {
#         'post_count': post_count,
#         'followers_count': followers_count,
#         'following_count': following_count,
#     }

#     return render(request, 'analytics/dashboard.html', context)
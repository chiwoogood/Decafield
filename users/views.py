from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import CustomUser
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import CustomUserCreationForm


from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.oauth2.views import (
    OAuth2LoginView,
    OAuth2CallbackView,
)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = user.username
            messages.success(request, f'Account created for {username}!')
            return redirect('users:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


@csrf_exempt
def username_check(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)

        # 사용자 이름이 이미 존재하는지 확인
    if CustomUser.objects.filter(username=username).exists():
        return JsonResponse({'status': 'unavailable'})
    else:
        return JsonResponse({'status': 'available'})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('profile')
        else:
            messages.error(request, 'Login failed. Please check your username and password.')
    return render(request, 'users/login.html')

@login_required
def logout(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'profile.html')

def social_login(request):
    return render(request, 'social_login.html')

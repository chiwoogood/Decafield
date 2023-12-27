from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser
from .forms import CustomUserCreationForm

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from django.contrib.auth.views import LoginView

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
            form.save()
            return redirect('users:login')
        else:
            print(form.errors)  # 이 부분을 추가하여 콘솔에 에러 출력
            print(form.errors.as_json())

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
            auth_login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index:index')
        else:
            messages.error(request, 'Login failed. Please check your username and password.')
    return render(request, 'users/login.html')


@login_required
def logout(request):
    auth_logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'profile.html')

def social_login(request):
    return render(request, 'social_login.html')


def forgot(request):


    return render(request,'users/forgot.html')

class CustomLoginView(LoginView):
    template_name = 'users/login.html'  # 원하는 템플릿 경로로 변경

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 추가적인 컨텍스트 변수가 필요하다면 여기에 추가
        return context
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('username_check/', views.username_check, name='username_check'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('update/',views.update,name='update'),
    path('logout/', views.logout, name='logout'),
    # path('profile/', views.profile, name='profile'),
    path('social-login/', views.social_login, name='social_login'),
    path('forgot/', views.forgot, name='forgot')
]

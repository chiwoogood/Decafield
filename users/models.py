from django.contrib.auth.models import AbstractUser
from django.db import models
from allauth.socialaccount.models import SocialAccount

class CustomUser(AbstractUser):
    # 추가 필드 정의
    name = models.CharField(max_length=15, default='', null=True, verbose_name='이름')
    email = models.EmailField(max_length=50, unique=True, blank=True, null=True, default='temp@email.com')
    phone = models.CharField(max_length=11, default='', null=True, verbose_name='휴대폰번호')
    coffee_type = models.CharField(max_length=20, blank=True, null=True, verbose_name='좋아하는 커피타입')
    

    def __str__(self):
        return self.username
    

from django.db import models
from users.models import CustomUser


class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    brand = models.CharField(max_length=30, null=False)
    shop_name = models.CharField(max_length=30, null=False)
    addr = models.CharField(max_length=60, null=False)
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    brn = models.CharField(max_length=20, null=True)
    like = models.BooleanField(default=False)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.shop_name
    

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.username} on {self.shop.shop_name} at {self.created_at}"
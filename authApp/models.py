from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Custom_User(AbstractUser):
    USER=[
        ('user','User'),('blogger','Blogger'),('admin','Admin'),
        
    ]
    
    display_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    user_type=models.CharField(choices=USER, max_length=120)
    profile_image = models.ImageField(upload_to='profile_pic/', null=True)
    otp_token = models.CharField(max_length = 6, blank = True, null = True)
    
    
    
    def __str__(self):
        return self.display_name
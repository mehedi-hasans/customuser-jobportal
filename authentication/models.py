from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    USER = [
        ('recruiter', 'Recruiter'),
        ('applicant', 'Applicant'),
    ]
    user_type = models.CharField(choices = USER, max_length= 100, default = 'applicant')
    name = models.CharField(max_length=255, null = True)
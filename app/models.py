from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class RegisterUser(AbstractUser):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email_address = models.EmailField(max_length=255, unique=True, null=False)
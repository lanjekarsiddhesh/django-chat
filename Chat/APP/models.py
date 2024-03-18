from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import date
from .manager import *

# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    F_name = models.CharField(max_length=500,blank=True,null=True)
    L_name = models.CharField(max_length=500,blank=True,null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def __str__(self) -> str:
        return self.email
    
class UserProfile(models.Model):
    today = date.today()
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name= "userprofile")
    Display_name =  models.CharField(max_length=500,null=True,blank=True)
    Profile_image = models.ImageField(upload_to=str(today),blank=True,null=True)
    friends = models.ManyToManyField(CustomUser, blank=True, related_name="User_Friends")

    def __str__(self) -> str:
        return self.user.email
from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None , **extra_fields):
        """Create and save a User with the given email, and password."""
        if not email:
            raise ValueError("The email field is required...")
        
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        # user.set_password(raw_password)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create Superuser/Admin of the site"""
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)
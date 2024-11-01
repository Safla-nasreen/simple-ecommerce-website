from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('company', 'Company'),
        ('admin', 'Admin'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    # You can add more fields as needed, like profile_picture, bio, etc.

    def __str__(self):
        return f"{self.user.username} ({self.get_user_type_display()})"

class Company(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    verification_status = models.BooleanField(default=False)  # Unverified by default

    def __str__(self):
        return self.name

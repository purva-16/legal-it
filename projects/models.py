import uuid
from django.db import models
from django.contrib.auth.models import User


class Lawyer(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=200)
    # Additional lawyer-related fields
    address = models.TextField(blank=True, null=True)
    years_of_practice = models.IntegerField(blank=True, null=True)
    no_of_cases_taken = models.IntegerField(blank=True, null=True)
    no_of_cases_won = models.IntegerField(blank=True, null=True)
    specialization = models.CharField(max_length=100, blank=True, null=True)
    # Add other lawyer-related fields as needed\



 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional user profile fields as needed
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
  
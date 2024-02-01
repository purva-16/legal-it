# projects/admin.py
from django.contrib import admin
from .models import Lawyer, UserProfile

@admin.register(Lawyer)
class LawyerAdmin(admin.ModelAdmin):
    list_display = ['name', 'expertise', 'address', 'years_of_practice', 'no_of_cases_taken', 'no_of_cases_won', 'specialization']
    # Add other configurations as needed

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'full_name', 'phone_number']
    # Add other configurations as needed

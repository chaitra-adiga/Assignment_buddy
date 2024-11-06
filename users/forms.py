# users/forms.py
from django import forms
from .models import Profile

class ProfileCompletionForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'  # This will include all fields from the Profile model  

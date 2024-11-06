from django import forms

class CompleteProfileForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)
    upi_id = forms.CharField(max_length=50, required=True)
    location = forms.CharField(max_length=100, required=True)
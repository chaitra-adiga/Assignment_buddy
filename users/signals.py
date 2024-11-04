# users/signals.py
from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver
from django.shortcuts import redirect
from django.urls import reverse
from .models import Profile

@receiver(social_account_added)
def social_account_added_handler(request, sociallogin, **kwargs):
    user = sociallogin.user
    try:
        Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        # Redirect to complete registration if Profile does not exist
        return redirect(reverse('complete_registration'))

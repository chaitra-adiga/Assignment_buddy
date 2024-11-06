# Create a new file: middleware.py in your users app
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import LogoutView

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Exclude these paths from the check
            exempt_paths = [
                reverse('complete_profile'),
                reverse('logoutt'),
                '/admin/',
                '/',  # Add other exempt paths as needed
            ]
            
            if not any(request.path.startswith(path) for path in exempt_paths):
                if not hasattr(request.user, 'profile') or not request.user.profile.has_registered:
                    return redirect('complete_profile')

        response = self.get_response(request)
        return response
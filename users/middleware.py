# Create a new file: middleware.py in your users app
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.views import LogoutView

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            # Paths that don't require profile completion
            exempt_paths = [
                reverse('complete_registration'),
                reverse('logoutt'),
                '/admin/'
            ]
            
            # If user is on a protected path and profile isn't complete
            if (not request.path in exempt_paths and 
                not hasattr(request.user, 'profile')):
                return redirect('complete_registration')
                
        return self.get_response(request)
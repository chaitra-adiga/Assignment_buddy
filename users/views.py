from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from allauth.socialaccount.models import SocialAccount

# Create your views here.
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount

def home(request):
    # Default value for google_email
    google_email = None
    
    # Get the current user
    user = request.user
    
    # Check if the user is authenticated
    if user.is_authenticated:
        # Try to get the social account for the logged-in user
        try:
            google_account = SocialAccount.objects.get(user=user, provider='google')
            google_email = google_account.extra_data.get('email')  # Retrieve the Google email
        except SocialAccount.DoesNotExist:
            google_email = user.email  # Fall back to the user's primary email

    # Pass google_email to your template
    return render(request, 'home.html', {'google_email': google_email})


def login_user(request):
    return render(request, 'loginn.html')

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('login_user')


'''
from ads.models import Ad
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdListView(OwnerListView):
    model = Ad
    context_object_name = 'ads_list' # chatgpt added and worked
    # By convention:
    # template_name = "myarts/article_list.html"


class AdDetailView(OwnerDetailView):
    model = Ad


class AdCreateView(OwnerCreateView):
    model =Ad
    # List the fields to copy from the Article model to the Article form
    fields = ['title', 'text','price']


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'text','price']
    context_object_name = 'ads_list'
    # This would make more sense
    # fields_exclude = ['owner', 'created_at', 'updated_at']


class AdDeleteView(OwnerDeleteView):
    model = Ad

    
    template - 
 ad_confirm_delete.html
 ad_detail.html
 ad_form.html
 ad_list.html
'''
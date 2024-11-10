from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Profile
from .forms import CompleteProfileForm # users/views.py
# Create your views here.
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount

'''@login_required
def complete_registration(request):
    if request.method == "POST":
        form = CompleteProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("home")  # Redirect to home or another page after completion
    else:
        form = CompleteProfileForm()
    return render(request, "complete_registration.html", {"form": form})
'''

"""def register_user(request):
    if request.method == 'POST':
        try:
            fnm = request.POST.get('fnm')
            emailid = request.POST.get('emailid')
            pwd = request.POST.get('pwd')
            phn= request.POST.get('phn')
            #upi = request.POST.get('upi')
            #loc= request.POST.get('loc')
            my_user = User.objects.create_user(fnm, emailid, pwd)
            my_user.save()
            user_model = User.objects.get(username=fnm)
            new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
            new_profile.save()
            if my_user is not None:
                login(request, my_user)
                return redirect('/')
            return redirect('/')
        except:
            invalid = "User Already Exists"
            return render(request, 'register.html', {'invalid': invalid})
    else:
        return render(request, 'register.html')
    


def loginn(request):
    # Handle local login
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        print(fnm, pwd)  # Optional debug line

        # Local authentication
        userr = authenticate(request, username=fnm, password=pwd)
        
        if userr is not None:
            # Log in the user and redirect to home page
            login(request, userr)
            return redirect('/')
        
        # Show an error message if local credentials are invalid
        invalid = "Invalid Credentials"
        return render(request, 'loginn.html', {'invalid': invalid})

    # Google authentication check
    google_email = None
    user = request.user
    if user.is_authenticated:
        try:
            google_account = SocialAccount.objects.get(user=user, provider='google')
            google_email = google_account.extra_data.get('email')
        except SocialAccount.DoesNotExist:
            google_email = user.email  # Fallback to user's registered email

    # Render the login page for GET requests, with Google email if available
    return render(request, 'loginn.html', {'google_email': google_email})

"""

def register_user(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')
        phn = request.POST.get('phn')
        upi = request.POST.get('upi')
        loc = request.POST.get('loc')

        if User.objects.filter(username=fnm).exists():
            invalid = "User Already Exists"
            return render(request, 'register.html', {'invalid': invalid})

        if User.objects.filter(email=emailid).exists():
            invalid = "Email Already Exists"
            return render(request, 'register.html', {'invalid': invalid})

        my_user = User.objects.create_user(fnm, emailid, pwd)
        my_user.save()
        user_model = User.objects.get(username=fnm)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, phone=phn, upi_id=upi, location=loc)
        new_profile.save()
        login(request, my_user)
        return redirect('/')
    else:
        return render(request, 'register.html')
    
'''@login_required
def complete_registration(request):
    if request.method == 'POST':
        form = CompleteProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            
            # Create or update the profile
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'id_user': user.id,
                    'has_registered': True
                }
            )
            
            profile.phone = form.cleaned_data['phone']
            profile.upi_id = form.cleaned_data['upi_id']
            profile.location = form.cleaned_data['location']
            profile.has_registered = True
            profile.save()
            
            return redirect('/')
    else:
        # Pre-fill form if profile exists
        initial_data = {}
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            initial_data = {
                'phone': profile.phone,
                'upi_id': profile.upi_id,
                'location': profile.location,
            }
        form = CompleteProfileForm(initial=initial_data)

    return render(request, 'complete_profile.html', {'form': form})
  
@login_required
def complete_registration(request):
    if request.method == 'POST':
        form = CompleteProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'id_user': user.id,
                    'has_registered': True,
                    'bio': form.cleaned_data['bio']
                }
            )
            if not created:
                profile.bio = form.cleaned_data['bio']
                profile.has_registered = True
                profile.save()
            return redirect('/')
        return redirect('/')
    else:
        form = CompleteProfileForm()
    return render(request, 'complete_registration.html', {'form': form}) 
    


@login_required
def complete_registration(request):
    if request.method == 'POST':
        form = CompleteProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            
            # Create or update the profile
            profile, created = Profile.objects.get_or_create(
                user=user,
                defaults={
                    'id_user': user.id,
                    'has_registered': False  # Initial state
                }
            )
            
            # Update all fields from your form
            profile.bio = form.cleaned_data['bio']
            profile.phone = form.cleaned_data['phone']
            profile.upi_id = form.cleaned_data['upi_id']
            profile.location = form.cleaned_data['location']
            profile.has_registered = True  # Very important - set this to True
            profile.save()
            
            return redirect('/')  # This matches your existing redirect pattern
    else:
        # Pre-fill form if profile exists
        initial_data = {}
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            initial_data = {
                'bio': profile.bio,
                'phone': profile.phone,
                'upi_id': profile.upi_id,
                'location': profile.location,
            }
        form = CompleteProfileForm(initial=initial_data)

    return render(request, 'complete_registration.html', {'form': form})
'''

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

@login_required
def complete_registration(request):
    # First, check if profile is already complete to prevent loops
    if hasattr(request.user, 'profile') and request.user.profile.has_registered:
        messages.info(request, 'Your profile is already complete.')
        return redirect('home')  

    if request.method == 'POST':
        form = CompleteProfileForm(request.POST)
        if form.is_valid():
            try:
                profile = request.user.profile
            except Profile.DoesNotExist:
                profile = Profile.objects.create(
                    user=request.user,
                    id_user=request.user.id
                )

            # Update the profile fields
            profile.bio = form.cleaned_data.get('bio', '')
            profile.phone = form.cleaned_data.get('phone', '')
            profile.upi_id = form.cleaned_data.get('upi_id', '')
            profile.location = form.cleaned_data.get('location', '')
            profile.has_registered = True
            profile.save()

            messages.success(request, 'Profile completed successfully!')
            return HttpResponseRedirect(reverse('home'))  # Using reverse() for better URL handling
        else:
            # Add specific error messages for each field
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.title()}: {error}')
    else:
        # GET request - create new form with initial data if profile exists
        initial_data = {}
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            initial_data = {
                'bio': profile.bio or '',
                'phone': profile.phone or '',
                'upi_id': profile.upi_id or '',
                'location': profile.location or '',
            }
        form = CompleteProfileForm(initial=initial_data)
    
    return render(request, 'complete_registration.html', {'form': form})
    '''else:
        # Pre-fill form if profile exists
        initial_data = {}
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
            initial_data = {
                'bio': profile.bio or '',
                'phone': profile.phone or '',
                'upi_id': profile.upi_id or '',
                'location': profile.location or '',
            }
        form = CompleteProfileForm(initial=initial_data)

    return render(request, 'complete_registration.html', {'form': form})'''

def loginn(request):
    if request.method == 'POST':
        # Local login logic remains the same
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            # Check if profile is complete for local login
            if not hasattr(userr, 'profile') or not userr.profile.has_registered:
                return redirect('complete_registration')
            return redirect('/')
        
        invalid = "Invalid Credentials"
        return render(request, 'loginn.html', {'invalid': invalid})

    google_email = None
    user = request.user

    if user.is_authenticated:
        try:
            google_account = SocialAccount.objects.get(user=user, provider='google')
            google_email = google_account.extra_data.get('email')
            # Check if profile exists and is complete for Google login
            if not hasattr(user, 'profile') or not user.profile.has_registered:
                return redirect('complete_registration')
        except SocialAccount.DoesNotExist:
            google_email = user.email

    return render(request, 'loginn.html', {'google_email': google_email})

def logoutt(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('loginn')


@login_required(login_url='/login')
def home(request):
    # Check if profile is complete
    if not hasattr(request.user, 'profile') or not request.user.profile.has_registered:
        return redirect('complete_registration')
        
    email = None
    user = request.user
    
    if user.is_authenticated:
        try:
            google_account = SocialAccount.objects.get(user=user, provider='google')
            email = google_account.extra_data.get('email')
        except SocialAccount.DoesNotExist:
            email = user.email

    return render(request, 'home.html', {'email': email})

    
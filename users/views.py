from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import ProfileCompletionForm # users/views.py
# Create your views here.
from django.shortcuts import render
from allauth.socialaccount.models import SocialAccount

@login_required
def complete_registration(request):
    if request.method == "POST":
        form = ProfileCompletionForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("home")  # Redirect to home or another page after completion
    else:
        form = ProfileCompletionForm()
    return render(request, "complete_registration.html", {"form": form})


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
    
def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        userr = authenticate(request, username=fnm, password=pwd)
        
        if userr is not None:
            login(request, userr)
            return redirect('/')
        
        invalid = "Invalid Credentials"
        return render(request, 'loginn.html', {'invalid': invalid})

    google_email = None
    user = request.user
    if user.is_authenticated:
        try:
            google_account = SocialAccount.objects.get(user=user, provider='google')
            google_email = google_account.extra_data.get('email')
        except SocialAccount.DoesNotExist:
            google_email = user.email

    return render(request, 'loginn.html', {'google_email': google_email})
    

def logoutt(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('loginn')


@login_required(login_url='/login')
def home(request):
    # Default value for the email
    email = None
    
    # Get the current user
    user = request.user
    
    # Check if the user is authenticated through Google
    if user.is_authenticated:
        try:
            # Check for a Google social account and retrieve the Google email
            google_account = SocialAccount.objects.get(user=user, provider='google')
            email = google_account.extra_data.get('email')
        except SocialAccount.DoesNotExist:
            # If Google account doesn't exist, use the primary email (local login email)
            email = user.email

    # Pass email to the template
    return render(request, 'home.html', {'email': email})
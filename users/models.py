from django.db import models
from django.contrib.auth.models import User
import hashlib


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True, default=0)
    bio = models.TextField(blank=True)
    
    def get_gravatar_url(self, size=100):
        email = self.user.email or ''  # Fallback to empty string if email is None
        email_hash = hashlib.md5(email.strip().lower().encode('utf-8')).hexdigest()
        return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=identicon"

    def profile_image_path(instance, filename):
        return f'profile_images/{instance.user.username}/{filename}'

    profileimg = models.ImageField(upload_to=profile_image_path, blank=True)
    upi_id = models.CharField(max_length=100, blank=False, default='')
    phone = models.CharField(max_length=10, blank=False, default='')
    location = models.CharField(max_length=100, blank=False, default='')

    def save(self, *args, **kwargs):
        # Set profile image to Gravatar if not provided
        if not self.profileimg:
            self.profileimg = self.get_gravatar_url()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username

# Create your models here.
'''class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField(primary_key=True, default=0)
    bio = models.TextField(blank=False)
    def get_gravatar_url(email, size=100):
        email_hash = hashlib.md5(email.lower().encode('utf-8')).hexdigest()
        return f"https://www.gravatar.com/avatar/{email_hash}?s={size}&d=identicon"

    def profile_image_path(instance, filename):
        return f'profile_images/{instance.user.username}/{filename}'

    profileimg = models.ImageField(upload_to=profile_image_path, blank=True)
    upi_id = models.CharField(max_length=100, blank=False,default='')
    phone = models.CharField(max_length=10, blank=False,default=0)
    location = models.CharField(max_length=100, blank=False,default='')

    def save(self, *args, **kwargs):
        if not self.profileimg:
            self.profileimg = self.get_gravatar_url(self.user.email)
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.user.username
    '''

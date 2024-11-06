from django.db import models
from django.contrib.auth.models import User
import hashlib


class Profile(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_registered = models.BooleanField(default=False)
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
    phone = models.CharField(max_length=15, blank=False, default='')
    location = models.CharField(max_length=100, blank=False, default='')

    def save(self, *args, **kwargs):
        # Set profile image to Gravatar if not provided
        if not self.profileimg:
            self.profileimg = self.get_gravatar_url()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username


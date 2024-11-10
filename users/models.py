from django.db import models
from django.contrib.auth.models import User
import hashlib, uuid
from datetime import datetime, timedelta

def get_default_expiry():
    return datetime.now() + timedelta(days=21)  # Default expiry of 21 days

# users/models.py
class Profile(models.Model):
    id_user = models.IntegerField(primary_key=True)  # Make this the primary key
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    has_registered = models.BooleanField(default=False)  # Add this field with default
    
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



'''class Profile(models.Model):
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
    
class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    file = models.FileField(upload_to='task_files', null=True, blank=True)
    file_link = models.URLField(null=True, blank=True)
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    expires_at = models.DateTimeField(default=lambda: datetime.now() + timedelta(days=21))
    request_to_commit = models.ManyToManyField(User, related_name='requested_tasks', blank=True)
    is_committed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.user.username}"

    def save(self, *args, **kwargs):
        # Auto-delete task if it's expired
        if self.expires_at < datetime.now():
            self.delete()
            return
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Delete associated file if it exists
        if self.file:
            self.file.delete()
        super().delete(*args, **kwargs)'''

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

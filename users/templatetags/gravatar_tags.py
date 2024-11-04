from hashlib import md5
from django import template

# https://brobin.me/blog/2016/07/super-simple-django-gravatar/

# A "gravatar" is a globally recognized avatar that is based on email address
# People must register their email address and then upload a gravatar
# If an email address has no gravatar, a generic image is put in its place

# To use the gravatar filter in a template include
# {% load app_tags %}

register = template.Library()

'''@register.filter(name='gravatar')
def gravatar(user, size=80):
    if hasattr(user, 'email'):  # Check if user has an email attribute
        email = str(user.email.strip().lower()).encode('utf-8')
        email_hash = md5(email).hexdigest()
        url = "//www.gravatar.com/avatar/{0}?s={1}&d=identicon&r=PG"
        return url.format(email_hash, size)
    else:
        # Return a default avatar or a placeholder URL
        return "//www.gravatar.com/avatar/?s={0}&d=identicon&r=PG".format(size)
'''
@register.filter(name='gravatar')
def gravatar(email, size=35):
    if email:
        email = email.strip().lower().encode('utf-8')
        email_hash = md5(email).hexdigest()
        url = "https://www.gravatar.com/avatar/{0}?s={1}&d=identicon&r=PG"
        return url.format(email_hash, size)
    else:
        # Default Gravatar URL when email is not provided
        return "https://www.gravatar.com/avatar/?s={0}&d=identicon&r=PG".format(size)
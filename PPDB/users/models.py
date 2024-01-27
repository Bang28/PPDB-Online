from django.db import models
from django.contrib.auth.models import AbstractUser, User
import os
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUser(AbstractUser):
    def image_upload_to(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.username, ext)
        return os.path.join('users', filename)

    email       = models.EmailField(unique=True)
    image       = models.ImageField("Foto Profil", default='default/user.png', upload_to=image_upload_to)    
    is_superuser = models.BooleanField(
        _('superuser status'),
        default=False,
        null=True,
        help_text=_(
            'Designates that this user has all permissions without '
            'explicitly assigning them.'
        ),
    )

    def __str__(self):
        return self.username
    
    # preview image/file
    def profile(self):
        try:
            return mark_safe(f'<img src = "{self.image.url}" width = "55"/>')
        except:
            pass

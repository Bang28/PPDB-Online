from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.
class CustomUser(AbstractUser):
    def image_upload_to(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (instance.username, ext)
        return os.path.join('users', filename)
    
    LEVEL = (
        ('', 'Pilih level'),
        ('Admin', 'Admin'),
        ('Peserta', 'Peserta'),
    )
    
    email       = models.EmailField(unique=True)
    level       = models.CharField(max_length=7, choices=LEVEL, default="Peserta")
    image       = models.ImageField("Foto Profil", default='default/user.png', upload_to=image_upload_to)    

    def __str__(self):
        return self.username

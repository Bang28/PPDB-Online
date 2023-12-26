from django.db import models
from django.contrib.auth.models import AbstractUser
import os

# Create your models here.
class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Users", self.username, instance)
        return None
    
    LEVEL = (
        ('', 'Pilih level'),
        ('Admin', 'Admin'),
        ('Peserta', 'Peserta'),
    )
    
    email       = models.EmailField(unique=True)
    level       = models.CharField(max_length=7, choices=LEVEL, default="Peserta")
    description = models.TextField("Deskripsi", max_length=300, default="", blank=True)
    image       = models.ImageField("Foto Profil", default='default/user.png', upload_to=image_upload_to)    

    def __str__(self):
        return self.username

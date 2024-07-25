import random
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=80, unique=True)
    mobile = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=120, blank=True, null=True)
    otp = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.username

    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.save()

    def is_otp_valid(self, otp):
        if self.otp == otp :
            return True
        return False
    

from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.db.transaction import atomic
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    profile_picture = models.ImageField(upload_to='profile-pictures/', blank=True)
    email = models.EmailField(unique=True, max_length=75)
    phone = PhoneNumberField(blank=True, default=None, null=True)
    address = models.CharField(null=True, default=None, max_length=150, blank=True)
    username = models.CharField(null=True, max_length=150, default=None, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subscription = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return 'Id:{0} Name :{1} {2}, email: {3}'.format(self.id, self.first_name, self.last_name, self.email)


@receiver(pre_save, sender=User)
@atomic
def pre_save_user(sender, instance, *args, **kwargs):
    if not getattr(instance, 'pk'):
        new_user = '{}{}'.format(datetime.now().strftime("%Y%m%d%S"), User.objects.all().count())
        instance.registration_no = 'Parusa-' + str(new_user)

from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(null=True, max_length=200, blank=True)
    address = models.CharField(null=True, max_length=200, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(default='default.png', upload_to='profiles_pics')
    phone_num = models.CharField(max_length=13, default="+375")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()

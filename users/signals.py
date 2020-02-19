from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# This signal is fired each time a object is saved
# in this case, when a user is created

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

#**kwarks additional keywords arguemtn
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
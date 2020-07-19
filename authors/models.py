from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """This id class for a profile of the user"""
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )
    bio = models.TextField(
        max_length=500,
        blank=True
    )
    picture = models.ImageField(
        blank=True,
        null = True,
        default="default_fon.jpg"
    )
    avatar = models.ImageField(
        upload_to='avatars/',
        default="avatars/default_avatar.jpg",
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('account', args=[str(self.id)])


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
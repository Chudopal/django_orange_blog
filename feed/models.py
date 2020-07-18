from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver

from tinymce.models import HTMLField


class Post(models.Model):
    """The model of post
    name -- name of the post,
    body -- content of the post,
    author -- the user, who wrote the post,
    comments -- other users can comment this post
    like -- number of likes
    date -- the date of creating the post
    """
    name = models.CharField(
        max_length=100,
        help_text="Enter the name of your post"
    )

    is_pinned = models.BooleanField(default=False)

    body = HTMLField()

    author = models.ForeignKey(
        'Profile',
        on_delete=models.CASCADE
    )

    comments = models.ManyToManyField(
        'Comment',
        blank=True
    )

    likes = models.ManyToManyField(
        'Like',
        blank=True
    )

    is_pinned = models.BooleanField(default=False)

    date = models.DateField(auto_now=True)

    def get_absolute_url(self):
        return reverse(
            "post-detail", 
            kwargs={"pk": self.pk}
        )

    class Meta():
        ordering = ["date"]

    def __str__(self):
        return self.name

    
class Comment(models.Model):
    """The model for comment
    body -- the content of the comment
    author -- the user, who wrote the comment,
    date -- the date of creating the comment
    """

    likes = models.ManyToManyField(
        "Like",
        blank=True
    )

    body = models.TextField(
        max_length=500,
        help_text="Enter the content of your comment"
    )

    author = models.ForeignKey(
        'Profile',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    date = models.DateField(
        auto_now=True
    )

    def get_absolute_url(self):
        return reverse("comment-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.body   
        
    class Meta():
        ordering = ["date"]
 


class Like(models.Model):
    """The class for likes. Users can likes posts"""

    author = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.author


class Profile(models.Model):
    """This id class for a profile of the user"""
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
    )
    posts = models.ManyToManyField(
        'Post',
        blank=True
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


class ProfileFollowing(models.Model):
    """This is class for the following systeme"""
    followers_id = models.ForeignKey(
        "Prifile",
        blank=True,
        null=True
    )
    following_id = models.ForeignKey(
        "Profile",
        null=True,
        blank=True
    )
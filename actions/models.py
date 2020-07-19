from django.db import models
from authors.models import Profile
from django.urls import reverse
# Create your models here.

class Like(models.Model):
    """The class for likes. Users can likes posts"""

    author = models.ForeignKey(
        Profile,
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.author


class Follower(models.Model):
    """This is class for the following systeme"""
    user_id = models.ForeignKey(
        Profile,
        related_name="following",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    followers_id = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="followers",
        blank=True,
        null=True
    )
    following_date = models.DateField(
        auto_now_add=True
    )


class Comment(models.Model):
    """The model for comment
    body -- the content of the comment
    author -- the user, who wrote the comment,
    date -- the date of creating the comment
    """

    likes = models.ManyToManyField(
        Like,
        blank=True
    )

    body = models.TextField(
        max_length=500,
        help_text="Enter the content of your comment"
    )

    author = models.ForeignKey(
        Profile,
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


from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from authors.models import (
    Profile,
)
from actions.models import (
    Comment,
    Like,
)

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
        max_length=100
    )

    is_pinned = models.BooleanField(default=False)

    body = HTMLField()

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )

    comments = models.ManyToManyField(
        Comment,
        blank=True
    )

    likes = models.ManyToManyField(
        Like,
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
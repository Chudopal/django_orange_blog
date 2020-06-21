from django.shortcuts import render
from .models import (
    Post,
    Comment
)
from django.contrib.auth.models import User
from django.views import generic
# Create your views here.


class PostsListView(generic.ListView):
    """Generic class based list of posts view"""
    model = Post
    paginate_by = 10


class PostDetailView(generic.DetailView):
    """Generic class based detail view of post"""
    model = Post


class AuthorListView(generic.ListView):
    """This class allows to get a list of authors """
    model = User
from django.shortcuts import render
from .models import (
    Post,
    Comment
)
from django.views import generic
# Create your views here.


class PostsListView(generic.ListView):
    model = Post
    paginate_by = 10

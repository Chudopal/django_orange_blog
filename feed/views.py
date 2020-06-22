from django.shortcuts import render
from .models import (
    Post,
    Comment
)
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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


def posts_of_user(request, pk):
    posts_of_user = Post.objects.filter(author=User.objects.get(pk=pk))
    context = {
        "posts": posts_of_user,
    }
    return render(request, 'feed/posts_of_user.html', context)


class CreatePost(CreateView):
    """This class allows to create new post"""
    model = Post
    fitlds = '__all__'


class UpdatePost(UpdateView):
    """This class allows to update your post"""
    model = Post
    fields = "body"


class DeletePost(DeleteView):
    """This is a delete post view"""
    model = Post
    success_url = reverse_lazy('list-of-posts') 


def my_posts(request, pk):
    """This function is for showing your posts"""
    posts_of_user = Post.objects.filter(author=User.objects.get(pk=pk))
    context = {
        "posts": posts_of_user, 
    }
    return render(request, "feed/my_posts.html", context)
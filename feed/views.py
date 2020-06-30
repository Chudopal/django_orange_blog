from django.shortcuts import render
from .models import (
    Post,
    Comment,
    Profile
)
from django.contrib.auth.decorators import login_required
from .forms import CommentForm, LikeForm
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
# Create your views here.


class PostsListView(generic.ListView):
    """Generic class based list of posts view"""
    model = Post
    paginate_by = 10


@login_required
def post_detail_view(request, pk):
    context = {}

    form_comment = CommentForm(request.POST or None)
    form_like = LikeForm(request.POST or None)
    post = Post.objects.get(pk=pk)
    if form_comment.is_valid():
        comment = form_comment.save(commit=False)
        comment.author = request.user
        comment.save()
        post.comments.add(comment)

    if form_like.is_valid():
        like = form_like.save(commit=False)
        like.author = request.user        

        if (post.likes.filter(author=like.author).exists()):
            post.likes.filter(author=like.author).delete()
        else:
            like.save()
            post.likes.add(like)

    context['post'] = post
    context['form_comment'] = form_comment
    context['form_like'] = form_like
    return render(request, 'feed/post_detail.html', context)


def posts_of_user(request, pk):
    posts_of_user = Post.objects.filter(author=User.objects.get(pk=pk))
    context = {
        "posts": posts_of_user,
    }
    return render(request, 'feed/posts_of_user.html', context)


class AuthorListView(generic.ListView):
    """This class allows to get a list of authors """
    model = User


class CreatePost(LoginRequiredMixin, CreateView):
    """This class allows to create new post"""
    model = Post
    fields = [
        'name',
        'body',
    ]

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super(CreatePost, self).form_valid(form)


class UpdatePost(LoginRequiredMixin, UpdateView):
    """This class allows to update your post"""
    model = Post
    fields = "body"


class DeletePost(LoginRequiredMixin, DeleteView):
    """This is a delete post view"""
    model = Post
    success_url = reverse_lazy('list-of-posts') 


def my_account(request, pk):
    """This function is for showing your posts"""
    posts_of_user = Post.objects.filter(author=User.objects.get(pk=pk))
    picture = Profile.objects.get(user=User.objects.get(pk=pk)).picture
    context = {
        "posts": posts_of_user, 
        "picture": picture,
    }
    return render(request, "feed/my_account.html", context)

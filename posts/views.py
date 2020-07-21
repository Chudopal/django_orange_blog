from .models import Post
from authors.models import Profile
from actions.forms import (
    CommentForm,
    LikeForm,
)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .forms import PostForm
from django.shortcuts import redirect


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
        comment.author = Profile.objects.get(user=request.user)
        comment.save()
        post.comments.add(comment)

    if form_like.is_valid():
        like = form_like.save(commit=False)
        like.author = Profile.objects.get(user=request.user)        

        if (post.likes.filter(author=like.author).exists()):
            post.likes.filter(author=like.author).delete()
        else:
            like.save()
            post.likes.add(like)

    context['post'] = post
    context['form_comment'] = form_comment
    context['form_like'] = form_like
    return render(request, 'posts/post_detail.html', context)


class CreatePost(LoginRequiredMixin, CreateView):
    """This class allows to create new post"""
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        obj = form.save(commit=False)
        obj.author = profile
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
from django.shortcuts import render
from .models import Profile
from .forms import (
    SignUpForm,
    ProfileForm
    )
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def posts_of_user(request, pk):
    profile = Profile.objects.get(pk=pk)
    context = {
        "profile": profile,
    }
    return render(request, 'feed/posts_of_user.html', context)


def followers_of_user(request, pk):
    profile = Profile.objects.get(pk=pk)
    context = {
        "profile": profile,
    }
    return render(request, 'feed/followers_of_user.html', context)


class AuthorListView(generic.ListView):
    """This class allows to get a list of authors """
    model = Profile


@login_required
def my_account(request, pk):
    """This function is for showing your posts"""
    profile = Profile.objects.get(pk=pk)

    context = {
        "profile": profile,
        "posts": profile.posts.filter(is_pinned=True)
    }

    return render(request, "feed/my_account.html", context)


class SignUpView(generic.CreateView):
    """Class for users registration"""
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UpdateUser(LoginRequiredMixin, UpdateView):
    """This class allows to update your post"""
    model = Profile
    fields = (
        "bio",
        "picture",
        "avatar",
    )
    
    def form_valid(self, form):
        self.object.picture = self.request.FILES['picture']
        self.object.avatar = self.request.FILES['avatar']
        self.object.save()
        return super().form_valid(form)
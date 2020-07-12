
from django import forms 
from .models import (
    Comment, 
    Like, 
    Profile, 
    Post
)
from tinymce.widgets import TinyMCE 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
  
# creating a form 
class CommentForm(forms.ModelForm): 
    
    body = forms.CharField(
        widget=forms.Textarea(
            attrs={'required':False, 'cols':78, 'rows':3}
        )
    )

    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Comment 
  
        # specify fields to be used 
        fields = [ 
            'body',
        ]


class LikeForm(forms.ModelForm):

    class Meta:
        model = Like

        fields = []

    
class ProfileForm(forms.ModelForm):
    """This is class for profile form"""
    
    class Meta():
        model = Profile
        fields = [
            'picture',
            'bio'
        ]


class PostForm(forms.ModelForm):
    """This is the form for creating posts"""
    
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={"size":'20'}
        )
    )
    
    body = forms.CharField(
        widget=TinyMCE(
            attrs={'required':False, 'cols':80, 'rows':10}
        )
    )

    class Meta:
        model = Post
        fields = ('name', 'body')


class SignUpForm(UserCreationForm):
    """Form for registration user"""
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)
        widgets = {
            'username':  forms.TextInput(),
            'password2': forms.TextInput(),
            'password1': forms.TextInput(),
        }

    # This is an override of the save() method. It attaches a profile to a user when they register
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            return user
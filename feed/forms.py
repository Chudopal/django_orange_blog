
from django import forms 
from .models import (
    Comment, 
    Like, 
    Profile, 
    Post
)
from tinymce.widgets import TinyMCE 
  
# creating a form 
class CommentForm(forms.ModelForm): 
    
    body = forms.CharField(
        widget=TinyMCE(
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
    body = forms.CharField(
        widget=TinyMCE(
            attrs={'required':False, 'cols':80, 'rows':10}
        )
    )

    class Meta:
        model = Post
        fields = ('name', 'body')

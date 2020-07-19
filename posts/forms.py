
from django import forms 
from .models import (
    Post
)
from tinymce.widgets import TinyMCE 



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

    is_pinned = forms.BooleanField()

    class Meta:
        model = Post
        fields = (
            'name', 
            'body', 
            'is_pinned',
        )



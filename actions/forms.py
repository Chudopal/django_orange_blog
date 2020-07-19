from django import forms 
from .models import (
    Comment, 
    Like,
)

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

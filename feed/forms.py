
from django import forms 
from .models import Comment 
  
  
# creating a form 
class CommentForm(forms.ModelForm): 
  
    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Comment 
  
        # specify fields to be used 
        fields = [ 
            'body',  
        ] 
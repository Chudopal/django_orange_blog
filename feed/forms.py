
from django import forms 
from .models import Comment 
  
  
# creating a form 
class CommentForm(forms.ModelForm): 
  
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Comment 
  
        # specify fields to be used 
        fields = [ 
            'body',
        ] 
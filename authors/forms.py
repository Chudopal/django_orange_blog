from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
   
   
class ProfileForm(forms.ModelForm):
    """This is class for profile form"""
    
    class Meta():
        model = Profile
        fields = [
            'picture',
            'bio'
        ]


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
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, AuthenticationForm
from .models import UserProfile


class LoginForm(AuthenticationForm):
    """
    Custom login form using a plain custom CSS class (no Bootstrap)
    so the username/password fields render full-width on their own,
    independent of Bootstrap being loaded.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Username',
        })
        self.fields['password'].widget.attrs.update({
            'class': 'input-field',
            'placeholder': 'Password',
        })


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=False)
    last_name  = forms.CharField(max_length=50, required=False)

    class Meta:
        model  = UserProfile
        fields = ('phone', 'picture')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial  = user.last_name


class EmailChangeForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ('email',)
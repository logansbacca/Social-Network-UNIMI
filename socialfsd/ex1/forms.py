from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="username", max_length=200)
    password = forms.CharField(label="password", max_length=200)


class UserForm(forms.Form):
    username = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200)
    bio = forms.CharField(max_length=200, widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
  
    
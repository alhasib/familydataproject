from django import forms

# creating a form
class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-md-6 col-lg-6 bg-light p-3', 'placeholder':"Enter Username..."}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control col-md-6 col-lg-6 bg-light p-3', 'placeholder':"Enter Password..."}))
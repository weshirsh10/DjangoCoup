from django import forms

class SigninForm(forms.Form):
    name = forms.CharField(label='Enter Your Name', max_length=20)
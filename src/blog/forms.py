from django import forms

class AddForm(forms.Form):
    title           = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    content         = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Discription'}))


class LoginForm(forms.Form):
    username        = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password        = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

    

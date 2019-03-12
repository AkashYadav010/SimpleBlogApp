from django import forms
from blogapp.models import Blog
# class AddForm(forms.Form):
#     title           = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
#     content         = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Discription'}))

class LoginForm(forms.Form):
    username        = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}))
    password        = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}))

class AddForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','content','image')
    def __init__(self, *args, **kwargs):
        super(AddForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','content')
    def __init__(self, *args,**kwargs):
        super(UpdateForm, self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'

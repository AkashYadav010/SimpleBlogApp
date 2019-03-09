from django import forms

class AddForm(forms.Form):
    title           = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}))
    content         = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Discription'}))

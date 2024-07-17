from django import forms
from .models import Content

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = '__all__'

        labels = {
            'cid' : 'Content ID',
            'title': 'Content Title',
            'content': 'Content',

        }

        widgets = {
            'cid' : forms.NumberInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'})
        }
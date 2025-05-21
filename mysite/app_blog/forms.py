from django import forms
from .models import ArticleImage
from django.forms.widgets import ClearableFileInput
class MultiFileInput(ClearableFileInput):
    allow_multiple_selected = True
class ArticleImageForm(forms.ModelForm):
    image = forms.ImageField(
        widget=MultiFileInput(attrs={'multiple': True}),
        required=False
    )
    
    class Meta:
        model = ArticleImage
        fields = '__all__'

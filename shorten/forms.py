from django import forms
from .models import URL


class URLForm(forms.ModelForm):
    class Meta:
        model = URL
        fields = ('long_url',)
        widgets = {'long_url': forms.Textarea}

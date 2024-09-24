# downloader/forms.py

from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='YouTube URL', widget=forms.URLInput(attrs={'placeholder': 'Enter YouTube URL here'}))

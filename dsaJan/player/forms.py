from django import forms
from .models import Song, Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'release_date']

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['title', 'album', 'duration', 'audio_file']

from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    duration = models.DurationField()
    audio_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title

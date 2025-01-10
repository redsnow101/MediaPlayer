from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('songs/play/random/', views.play_random_song, name='play_random_song'),
    path('songs/play/<int:song_id>/', views.play_song, name='play_song'),
    path('upload-album/', views.upload_album, name='upload_album'),
    path('upload-song/', views.upload_song, name='upload_song'),
]

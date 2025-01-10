import random
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlbumForm, SongForm
from .models import Album, Song
from django.db.models import Q



def upload_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlbumForm()
    return render(request, 'player/upload_album.html', {'form': form})

def upload_song(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SongForm()
    return render(request, 'player/upload_song.html', {'form': form})


def song_list(request):
    query = request.GET.get('q', '')  # Get search query
    if query:
        songs = Song.objects.filter(
            Q(title__icontains=query) | 
            Q(album__title__icontains=query) | 
            Q(album__artist__icontains=query)
        )
    else:
        songs = Song.objects.all()  # Fetch all songs if no query
    
    return render(request, 'song_list.html', {'songs': songs, 'query': query})



def play_random_song(request):
    songs = Song.objects.all()
    if songs.exists():
        random_song = random.choice(songs)
        return redirect('play_song', song_id=random_song.id)
    return redirect('song_list')


 

# def play_song(request, song_id):

#     song = get_object_or_404(Song, id=song_id)
    
#     return render(request, 'player/play_song.html', {'song': song})


def play_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    total_songs = Song.objects.count()
    next_song_id = song_id + 1 if song_id < total_songs else 1
    prev_song_id = song_id - 1 if song_id > 1 else total_songs
    
    return render(request, 'player/play_song.html', {
        'song': song,
        'next_song_id': next_song_id,
        'prev_song_id': prev_song_id
    })


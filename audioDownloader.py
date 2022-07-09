from __future__ import unicode_literals
import youtube_dl
from youtubesearchpython import VideosSearch
searchstring=input("Enter your song search term : ")
videosSearch = VideosSearch(searchstring, limit = 5)
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    
    for i in range(5):
        link=(videosSearch.result()['result'][i]['link'])
        ydl.download([link])
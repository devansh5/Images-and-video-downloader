from pytube import Playlist 
pl=Playlist("#link of the playlist")
print('Number of videos in playlist: %s' % len(pl.video_urls))
pl.download_all()



#to download for a specific directory 

pl.download_all('/path/to/directory/')

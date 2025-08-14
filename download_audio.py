import yt_dlp
global title
#video_url = "https://www.youtube.com/watch?v=Qu_MIo1tkhw"

def download(url):


        
        

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'videos/%(title)s.%(ext)s',  # Save as video title
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',     # Change to 'm4a' or 'wav' if preferred
            'preferredquality': '192',   # Bitrate (optional)
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)  # Don't download
        title = info.get('title')
        ydl.download([url])
    return(title)
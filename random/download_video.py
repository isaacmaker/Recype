import yt_dlp

# Define the video URL
video_url = "https://www.youtube.com/watch?v=Qu_MIo1tkhw"

# Set download options
ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Best quality available
    'merge_output_format': 'mp4',          # Merge into MP4 if separate streams
    'outtmpl': 'videos/%(title)s.%(ext)s',        # Save as video title
}

# Download the video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:


    ydl.download([video_url])





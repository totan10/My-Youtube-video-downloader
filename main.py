from pytube import YouTube

link=input("Enter url: ")
yt=YouTube(link)

#print(yt.thumbnail_url)
print(yt.title)
#videos=yt.streams.all()  # All video and Audio format

#videos=yt.streams.filter(only_audio=True)  #only Audio

videos=yt.streams.filter(only_video=True)  #only Video
vid=list(enumerate(videos))
for i in vid:
  print(i)

strm = int(input("Ender the index of preferred resolution and format: "))
print("Downloading.......")
videos[strm].download()
print("Downloaded Successfully!!!")
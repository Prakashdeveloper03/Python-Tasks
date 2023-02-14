from pytube import YouTube

n = int(input("Enter the number of youtube videos to download:   "))
links = []
print("\nEnter all the links one per line:")

for _ in range(n):
    temp = input()
    links.append(temp)

for i in range(n):
    link = links[i]
    yt = YouTube(link)
    print("\nDetails for Video", i + 1, "\n")
    print(f"Title of video : {yt.title}")
    print(f"Number of views :  {yt.views}")
    print(f"Length of video : {yt.length} seconds")
    stream = str(yt.streams.filter(progressive=True))
    stream = stream[1:]
    stream = stream[:-1]
    streamlist = stream.split(", ")
    print("\nAll available options for downloads:\n")
    for i in range(len(streamlist)):
        st = streamlist[i].split(" ")
        print(i + 1, ") ", st[1], " and ", st[3], sep="")
    tag = int(input("\nEnter the itag of your preferred stream to download : "))
    ys = yt.streams.get_by_itag(tag)
    print("\nDownloading...")
    ys.download()
    print("\nDownload completed!!")
    print()

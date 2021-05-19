from tkinter import * 
from pytube import YouTube

root = Tk() # initialize tkinter
root.geometry('600x400') # set width and height for window
root.resizable(0,0) # make window stay a fixed size 
root.title("Video Downloader") # sets the title 

Label(root,text = 'Video Downloader', font ='arial 16 bold').pack() 
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 70 , y = 60)
link_enter = Entry(root, width = 50, textvariable = link).place(x = 80, y = 90)

def Downloader():     
    print(str(link.get()))
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 240 , y = 280) 
     
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)
root.mainloop()

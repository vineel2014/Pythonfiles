import pyglet
import glob
from tkinter import Tk, Button
from PIL import Image
from PIL import ImageTk
import sys
songs=glob.glob("*.mp3")
player=pyglet.media.Player()

def play_song():
    global player
    for i in range(len(songs)):
        source=pyglet.resource.media(songs[i])
        player.queue(source)
        
        
    player.play()
def pause_song():
    player.pause()
def next_song():
    player.next_source()
def quit():
    sys.exit()
    



"""root.title('Python Rocks')
root.geometry('500x500')
im = Image.open('bostan.jpg')
tkimage = ImageTk.PhotoImage(im)
myvar=tk.Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)

app = Application(root)
app.mainloop()"""

window=Tk()
window.title('Python Rocks')
window.geometry('500x500')
im = Image.open('bostan.jpg')
tkimage = ImageTk.PhotoImage(im)

play_=Button(text="play", command=play_song)
play_.pack()
pause_=Button(text="pause", command=pause_song)
pause_.pack()
next_=Button(text="next", command=next_song)
next_.pack()
quit_=Button(text="quit", command=quit)
quit_.pack()


window.mainloop()

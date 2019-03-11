from tkinter import *
#from tkinter import ttk
import os
import tkinter.filedialog as tk
import tkinter.messagebox as tk2
import pyglet
from PIL import Image

from PIL import ImageTk

#from mutagen.mp3 import MP3
#import subprocess,os,glob
#import time
#import datetime
#import threading
playlist = []


player=pyglet.media.Player()
#pygame.init()

class Application(Frame):
    
    def __init__(self,master):
        super(Application, self).__init__(master)
        #self.create_widgets()
        self.playlistbox = Listbox(self, width = 40, height = 10, selectmode = SINGLE) #TODO: ---> BROWSE, MULTIPLE, EXTENDED (p.379)
        for song in playlist:
            self.playlistbox.insert(END, song)
        self.bttn_clicks = 0
        self.bttn_clicks1 = 0    
        self.grid(rowspan=5, columnspan=4)
        self.playlistbox.grid(row = 1)
        self.playButton = Button(self, text = '>', command = self.play)
        #self.loopButton = Button(self, text = '[]', command = self.loop)
        
        self.addButton = Button(self, text = '+', command = self.add)
        self.nextButton = Button(self, text = '>>', command = self.next)
        
        self.pauseButton = Button(self, text = '.', command = self.pause)
        
        self.quitButton = Button(self, text = 'X', command = self.quit)
        
        #self.volumeupButton = Button(self, text = '^', command = self.volumeup)
        
        #self.volumedownButton = Button(self, text = '~', command = self.volumedown)
        
        self.removelistButton=Button(self, text = 'del', command = self.remove)
        #self.after(0) 
        #tix.Button(root, text="Play")
        self.playButton.grid(row=4, column = 0)
        #self.loopButton.grid(row=4, column = 1)
        self.addButton.grid(row=4, column = 2)
        self.nextButton.grid(row=4, column = 3)
        self.pauseButton.grid(row=4, column = 4)
        self.quitButton.grid(row=4, column = 5)
        #self.volumeupButton.grid(row=3, column = 1)
        #self.volumedownButton.grid(row=3, column = 2)
        
        self.removelistButton.grid(row=3, column = 3)
        self.pack()
        
        #pygame initialize
        #pygame.init()

    def play(self):
        #l=len(playlist)
        
        if(len(playlist) == 0):
            tk2.showinfo('Notice', 'No songs in your playlist!\nClick Add to add songs.')
        else:
             #path=abspath(playlist)
             global player
             for i in range(len(playlist)):
                 path=os.path.abspath(playlist[i])
                 #playit=i
                 source=pyglet.media.load(path)
                 player.queue(source)
                 player.play()
             playlist.clear()
                 
              
                    
                    

          

    def remove(self):
        items = self.playlistbox.curselection()
        pos = 0
        for i in items :
            idx = int(i) - pos
            self.playlistbox.delete( idx,idx )
            pos = pos + 1
   
        if pos==0:

            tk2.showinfo('Notice', 'No more items to delete')


            
    """def loop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1,0.0)"""

    def add(self):
        file = tk.askopenfilenames(parent=root,title='Choose a file')#initialdir='/home/vineel/workspace/vin/src/Practice/mp3/')  
        #songsTuple = root.splitlist(file)   #turn user's opened filenames into tuple
        songsList = list(file)        #convert to list
        #Add the full filename of songto playlist list, and a shortened version to the listBox

        for song in songsList:              

            if song.endswith('.mp3'):

                playlist.append(song);          
                tempArray = song.split('/')     
                songShort = tempArray[len(tempArray)-1]
                self.playlistbox.insert(END, songShort)
            else:
                tk2.showinfo('Notice', 'Selected files are not mp3 files')
    
    """def volumedown(self):
        self.bttn_clicks += 1
        while True:
            if self.bttn_clicks==1:
                pygame.mixer.music.set_volume(0.9)
            elif self.bttn_clicks==2:
                pygame.mixer.music.set_volume(0.8)
            elif self.bttn_clicks==3:
                pygame.mixer.music.set_volume(0.7)
            elif self.bttn_clicks==4:
                pygame.mixer.music.set_volume(0.6)
            elif self.bttn_clicks==5:
                pygame.mixer.music.set_volume(0.5) 
            elif self.bttn_clicks==6:
                pygame.mixer.music.set_volume(0.4)
            elif self.bttn_clicks==7:
                pygame.mixer.music.set_volume(0.3)
            elif self.bttn_clicks==8:
                pygame.mixer.music.set_volume(0.2)
            elif self.bttn_clicks==9:
                pygame.mixer.music.set_volume(0.1)
            elif self.bttn_clicks==10:
                pygame.mixer.music.set_volume(0.0)
            else:
                tk2.showinfo('Notice', 'Volume Muted!Further Reduction of volume is not possible')       
                self.bttn_clicks=0
            break
            #print("Total Clicks: " + str(self.bttn_clicks))
         
    def volumeup(self):
        self.bttn_clicks1 += 1
        while True:  
            if self.bttn_clicks1==1:
                pygame.mixer.music.set_volume(0.1)
            elif self.bttn_clicks1==2:
                pygame.mixer.music.set_volume(0.2)
            elif self.bttn_clicks1==3:
                pygame.mixer.music.set_volume(0.3)
            elif self.bttn_clicks1==4:
                pygame.mixer.music.set_volume(0.4)
            elif self.bttn_clicks1==5:
                pygame.mixer.music.set_volume(0.5) 
            elif self.bttn_clicks1==6:
                pygame.mixer.music.set_volume(0.6)
            elif self.bttn_clicks1==7:
                pygame.mixer.music.set_volume(0.7)
            elif self.bttn_clicks1==8:
                pygame.mixer.music.set_volume(0.8)
            elif self.bttn_clicks1==9:
                pygame.mixer.music.set_volume(0.9)
            elif self.bttn_clicks1==10:
                pygame.mixer.music.set_volume(1.0)
            else:
                tk2.showinfo('Notice', 'You set Maximum Volume!Further Increase of volume is not possible')       
                self.bttn_clicks1=0        
            #print("Total Clicks: " + str(self.bttn_clicks))
            break"""
    def pause(self):
             
        player.pause()
        tk2.showinfo('Notice', 'Press > button to play again')
    



    def next(self):
        player.next_source()

        
            
    def quit(self):
        
        sys.exit()
        
root = Tk()
#root = ImageTk.PhotoImage("images.jpeg")
#background_image=PhotoImage("images.jpg")
root.title('Python Rocks')
root.geometry('500x500')
im = Image.open('bostan.jpg')
tkimage = ImageTk.PhotoImage(im)
myvar=tk.Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)

app = Application(root)
app.mainloop()

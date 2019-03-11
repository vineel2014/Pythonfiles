from tkinter import *
#from tkinter import ttk
import os
import tkinter.filedialog as tk
import tkinter.messagebox as tk2
import pyglet,time, threading
import pyglet.media as media
from PIL import Image

from PIL import ImageTk
import datetime

#from mutagen.mp3 import MP3
#import subprocess,os,glob
#import time
#import datetime
#import threading
global playlist
global player
playlist = []
global playing

player=pyglet.media.Player()

#pygame.init()

class Application(Frame):
    
    def __init__(self,master):
        super(Application, self).__init__(master)
        #self.create_widgets()
        self.playlistbox = Listbox(self, width = 35, height = 10, selectmode = SINGLE) #TODO: ---> BROWSE, MULTIPLE, EXTENDED (p.379)
        for song in playlist:
            self.playlistbox.insert(END, song)
        self.bttn_clicks = 0
        self.bttn_clicks1 = 0    
        self.grid(rowspan=5, columnspan=4)
        self.playlistbox.grid(row = 1)
        

        
       
        # playButton.setToolTip("You have moused over Button1")

        self.playButton = Button(self, text = '>',command = self.play)
        
        self.stopButton = Button(self, text = '[]', command = self.stop)
        
        self.addButton = Button(self, text = '+', command = self.add)
        
        self.nextButton = Button(self, text = '>>', command = self.next)
        
        self.pauseButton = Button(self, text = '.', command = self.pause)
        
        self.quitButton = Button(self, text = 'X', command = self.quit)
        
        self.volumeupButton = Button(self, text = '^', command = self.volumeup)
        
        self.volumedownButton = Button(self, text = '~', command = self.volumedown)
        
        self.removelistButton=Button(self, text = 'del', command = self.remove)

        self.previousButton=Button(self, text = '<<', command = self.previous)

     
        self.playButton.grid(row=4, column = 0)
        self.stopButton.grid(row=4, column = 1)
        self.addButton.grid(row=4, column = 2)
        self.nextButton.grid(row=4, column = 3)
        self.pauseButton.grid(row=4, column = 4)
        self.quitButton.grid(row=4, column = 5)
        self.volumeupButton.grid(row=3, column = 1)
        self.volumedownButton.grid(row=3, column = 2)       
        self.removelistButton.grid(row=3, column = 3)
        self.previousButton.grid(row=3, column = 4)
        self.pack()
        
        #pygame initialize
        #pygame.init()

    def play(self):
        #l=len(playlist)
        
        if(len(playlist) == 0):
            tk2.showinfo('Notice', 'No songs in your playlist!\nClick Add to add songs.')
        else:
           

            for i in range(len(playlist)):
                path=os.path.abspath(playlist[i])
                source=pyglet.media.load(path)
                player.queue(source)
                player.play()

            if player.on_eos():
                player.EOS_STOP
                playlist.clear()
                print(playlist)
                #self.playlistbox.delete(0,self.playlistbox.size())
   


    def remove(self):
        items = self.playlistbox.curselection()
        pos = 0
        #print(items)
        for i in items :
            idx = int(i) - pos
            self.playlistbox.delete( idx,idx )
            pos = pos + 1
   
        
        """if items!=():

                tk2.showinfo('Notice', 'No more items to delete')"""

        if items==():
   
            tk2.showinfo('Notice', 'No item is selected to  delete or \n Playlist is Empty')

        else: 
            pass


            


    def add(self):
        playlist.clear()
        file = tk.askopenfilenames(parent=root,title='Choose a file') #initialdir='/home/vineel/workspace/vin/src/Practice/mp3/')  
        #songsTuple = root.splitlist(file)   #turn user's opened filenames into tuple
        songsList = list(file)        #convert to list
        #Add the full filename of songto playlist list, and a shortened version to the listBox

        for song in songsList:              
            if song.endswith('.mp3' or '.MP3'):

                playlist.append(song);          
                tempArray = song.split('/')     
                songShort = tempArray[len(tempArray)-1]
                self.playlistbox.insert(END, songShort)
            else:
                tk2.showinfo('Notice', 'Selected files are not mp3 files')
    
    def volumedown(self):
        self.bttn_clicks += 1
        while True:
            if self.bttn_clicks==1:
                player.volume=1.0
            elif self.bttn_clicks==2:
                player.volume=0.9
            elif self.bttn_clicks==3:
                player.volume=0.8
            elif self.bttn_clicks==4:
                player.volume=0.7
            elif self.bttn_clicks==5:
                player.volume=0.6
            elif self.bttn_clicks==6:
                player.volume=0.5 
            elif self.bttn_clicks==7:
                player.volume=0.4
            elif self.bttn_clicks==8:
                player.volume=0.3
            elif self.bttn_clicks==9:
                player.volume=0.2
            elif self.bttn_clicks==10:
                player.volume=0.1
            elif self.bttn_clicks==11:
                player.volume=0.0
            else:
                tk2.showinfo('Notice', 'Volume Muted!Further Reduction of volume is not possible')       
                self.bttn_clicks=0
            break
            #print("Total Clicks: " + str(self.bttn_clicks))
         
    def volumeup(self):
        self.bttn_clicks1 += 1
        while True:  
            if self.bttn_clicks1==1:
                player.volume=0.0
            elif self.bttn_clicks1==2:
                player.volume=0.1
            elif self.bttn_clicks1==3:
                player.volume=0.2
            elif self.bttn_clicks1==4:
                player.volume=0.3
            elif self.bttn_clicks1==5:
                player.volume=0.4
            elif self.bttn_clicks1==6:
                player.volume=0.5
            elif self.bttn_clicks1==7:
                player.volume=0.6
            elif self.bttn_clicks1==8:
                player.volume=0.7
            elif self.bttn_clicks1==9:
                player.volume=0.8
            elif self.bttn_clicks1==10:
                player.volume=0.9
            elif self.bttn_clicks1==11:
                player.volume=1.0  

            else:
                tk2.showinfo('Notice', 'You cann`t set Maximum Volume!Further Increase of volume is not possible')       
                self.bttn_clicks1=0        
            #print("Total Clicks: " + str(self.bttn_clicks))
            break

    def pause(self):
             
        player.pause()
        tk2.showinfo('Notice', 'Music is paused! Press > button to continue')
    
    """def time_thread(self):
        threading.Thread(target=self.update_time_).start()
        return"""



    def next(self):
        player.next_source()
       

        
            
    def quit(self):
        
        sys.exit()

    def reset_player(self):
        player.pause()
        player.delete()
        

    def stop(self):

        self.reset_player()


    def previous(self):
        try:
            dirbase=os.path.dirname(self.playing.get())
            dirt=os.listdir(dirbase)
            base=os.path.basename(self.playing.get())
            k=dirt.index(base)-1
            path=os.path.join(dirbase, dirt[k])
            print (path)
            self.playing.set(path)
            pass
        except:
            pass

    



root = Tk()
#root = ImageTk.PhotoImage("images.jpeg")
#background_image=PhotoImage("images.jpg")
root.title('Python Rocks')
root.geometry('500x500')
im = Image.open('bostan.jpg')
root.resizable(0,0)
tkimage = ImageTk.PhotoImage(im)
myvar=tk.Label(root,image = tkimage)
myvar.place(x=0, y=0, relwidth=1, relheight=1)
playlist.clear()
app = Application(root)
app.mainloop()

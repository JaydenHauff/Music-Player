from tkinter import *
from tkinter import ttk, filedialog
from pygame import mixer
import os
from pafy import new
from pywhatkit import playonyt
import vlc



root=Tk()
root.title("Healer")
root.geometry("920x670+290+85")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

mixer.init()

#label
music=Label(root, text="", font=("arial",12), bg = "#2591c4")
music.place(x=500, y=50, anchor="center")

player = vlc.MediaPlayer()

class MusicPlayer :


    @classmethod
    def open_folder(cls): #defining a function to open a folder that will allow you to choose songs when clicked on the open folder button
        start_button.config(state=NORMAL)
        path=filedialog.askdirectory()
        if path:
            os.chdir(path)
            mp3=os.listdir(path)
           ## print(songs)
        for song in mp3:
            if song.endswith(".mp3") or song.endswith(".webm"):
              playlist.insert(END, song)

    @classmethod
    def play_song(cls): #defining a command play_song to play the desired song

        # MusicPlayer.play_Music_From_Web()
        music_name=playlist.get(ACTIVE)#to get the list of songs
        player.stop()
        mixer.music.load(playlist.get(ACTIVE))#to load the songs
        mixer.music.play()# to play the song
        music.config(text=music_name[0:-4])#declare the song playing



    @classmethod
    def click(cls, *args):
        search.delete(0, 'end')

    @classmethod
    def play_Music_From_Web(cls):
        start_button.config(state = DISABLED)
        mixer.music.stop()
        songName = search.get()
        if not songName.isspace():
            url = playonyt(songName, open_video=False)
            obj = new(url)
            audio = obj.getbestaudio()
            stream_url = audio.url
            title = obj.title
            music.config(text=title)
            media = vlc.Media(stream_url)
            player.set_media(media)
            player.play()



    @classmethod
    def pause(cls):
        mixer.music.pause()
        player.set_pause(1)

    @classmethod
    def resume(cls):
        mixer.music.unpause()
        player.set_pause(0)

    @classmethod
    def stop(cls):
        mixer.music.stop()
        player.stop()



#icon
image_icon=PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

Top=PhotoImage(file="top.png")
Label(root, image=Top, bg="#0f1a2b").pack()


#logo
Logo=PhotoImage(file="logo.png")
Label(root, image=Logo, bg="#0f1a2b").place(x=65, y=115)

#button
# global start_button
play_button=PhotoImage(file="play.png") #creating play button
start_button =Button(root, image=play_button, bg="#0f1a2b", bd=0, command=MusicPlayer.play_song)
start_button.place(x=150, y=400)
# start_button.pack()
print(type(start_button))#defining the location and place of the button and other details

stop_button=PhotoImage(file="stop.png")#creating stop button
Button(root, image=stop_button, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=30, y=500)#defining the location and place of the button and other details

resume_button=PhotoImage(file="resume.png")#creating resume button
Button(root, image=resume_button, bg="#0f1a2b", bd=0, command=MusicPlayer.resume).place(x=115, y=500)#defining the location and place of the button and other details

pause_button=PhotoImage(file="pause.png")#creating pause button
Button(root, image=pause_button, bg="#0f1a2b", bd=0, command=MusicPlayer.pause).place(x=200, y=500)#defining the location and place of the button and other details

open_file = PhotoImage(file="open.png")
Button(root, image=open_file,bd=0, width= 85, height=85, bg="#0f1a2b", command=MusicPlayer.open_folder).place(x=53, y=410) #button for adding more songs from folder

# Button(root, )

search=Entry(root, font = ("Helvetica"))
search.place(x=600, y=250, width=400, height=40)
search.insert(0,'Search : ')
search_button = PhotoImage(file="search.png")
Button(root, image=search_button, bg="white", bd = 0, command = MusicPlayer.play_Music_From_Web).place(x=555, y=238, width=35, height=35)
search.pack()
search.bind("<Button-1>", MusicPlayer.click)
# search.bind("<Return>", MusicPlayer.play_Music_From_Web())



# #music
Menu=PhotoImage(file="menu.png")#creating a menu for the music
Label(root, image=Menu, bg="#0f1a2b").pack( padx=10, pady = 5, side=RIGHT)#defining its details

music_frame=Frame(root, bd=2, relief=RIDGE)#making a musci frame where the playlist will be showed
music_frame.place(x=350,y=300, width=550, height=330)#defining its details



scroll= Scrollbar(music_frame) #making a scroll barr
playlist=Listbox(music_frame, width=100, font=("arial",14),bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=scroll.set)#listbox for the list of music to be displayed on  music frame
scroll.config(command=playlist.yview)#making the scroll bar active
scroll.pack(side=RIGHT, fill=Y)#packing the scroll in its position
playlist.pack(side=LEFT, fill=BOTH)#packking the playlist


root.mainloop()#an unlimited loop to keep the programming running till you want to close the window

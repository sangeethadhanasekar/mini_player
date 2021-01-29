from pathlib import *
from tkinter import *
import pygame
pygame.init()
pygame.mixer.init()
root=Tk()
root.title("MINI PLAYER")
root.geometry('600x500')

name_var=StringVar()



def music_names_load():
    entries=Path('sounds/')
    for entry in entries.iterdir():
            a.insert(1,entry)
def pause_pressed():
    pygame.mixer.music.pause()
    
def unpause_pressed():
    pygame.mixer.music.unpause()
    
def stop_pressed():
     # if (button2["text"]=="stop"):
         pygame.mixer.music.stop() 
         button2.configure(text="stopped!")
         button.configure(state=DISABLED)
  
            
def music_name_out(event):
             name_entry.delete(1,END)
             button.configure(text="pause")
             w=event.widget
             idx=int(w.curselection()[0])
             value=w.get(idx)
             name_entry.insert(0,value)
             button.configure(state=NORMAL)
             button2.configure(state=NORMAL)
             button2.configure(text="stop")
             pygame.mixer.music.load(value)
             pygame.mixer.music.play()
             
             #if pygame.mixer.music.get_busy():
               # print( pygame.time.Clock().tick(2))
            

               #  print("value 0")
                 #pygame.mixer.music.load(values)
                 #pygame.mixer.music.play()
                          
                   
                 
def update_fn():
    if (button["text"]=="pause") :
        button2.configure(text="stop")
        pause_pressed()
        button2.configure(state=DISABLED)
        button.configure(text="unpause")
        
    elif (button["text"]=="unpause") :
            unpause_pressed()
            button.configure(text="pause")
            button2.configure(state=NORMAL)
   
    
#assigning the layout of mini player    
label1=Label(root,text="Music track:",font=("arieal",13)).grid(row=1,column=0,padx=5,pady=5)
name_entry=Entry(root,width=50,textvariable=name_var,cursor='hand2')
name_entry.grid(row=1,column=1,padx=0,pady=0)
label2=Label(root,text="select the music from the below list:",font=("Helvetica",12)).grid(row=2,column=1,padx=5,pady=4)
a=Listbox(root,height=10,width=30,font=("Helvetica",16),cursor='dot',selectmode='SINGLE')
a.grid(row=3,column=1)
a. bind('<<ListboxSelect>>',music_name_out)

#assigning buttons
button=Button(root,text="pause",height=2,width=20,bg="pink",fg="blue",command=update_fn,state=NORMAL)
button2=Button(root,text="stop",height=2,width=20,bg="pink",fg="blue",command=stop_pressed)
button.grid(row=4,column=0,padx=20,pady=30)
button2.grid(row=4,column=2,padx=20,pady=30)


#when we resize the screen the rows and columns also get expand or shrinked with this code
root.columnconfigure(0,weight=1,minsize=75)
root.columnconfigure(1,weight=1,minsize=75)
root.columnconfigure(2,weight=1,minsize=75)
root.rowconfigure(0,weight=1,minsize=50)
root.rowconfigure(1,weight=1,minsize=50)
root.rowconfigure(2,weight=1,minsize=50)
root.rowconfigure(3,weight=1,minsize=50)
root.rowconfigure(4,weight=1,minsize=50)



music_names_load()
root.mainloop()

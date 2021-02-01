import json
#import Pillow as PIL
from tkinter import *
from difflib import *
#import Image,ImageTK
#from PIL import Image
#from PIL import ImageTK
from tkinter import messagebox
data=json.load(open("data.json"))
root=Tk()
root.title("dict")
root.geometry('500x600')

#canv=Canvas(root,width=500,height=600,bg='black')
#canv.pack(expand=YES,fill=BOTH)
#image1=PhotoImage(Image.open('dicts_img.jpg'))
#canv.create_image(50,50,image=image1,anchor=NW)


global b
b=0
def get_meaning(word):
    if word in data:
         if len(data[word])>1:
             for i in data[word]:
                 #print(i)
                 return i 
         else:
              #print(data[word][0])
              return data[word][0]


    elif word.lower() in data:
         if len(data[word.lower()])>1:
             for i in data[word.lower()]:
                 #print(i)
                 return i
         else:
             # print(data[word][0])
             return data[word][0]


    elif word.upper() in data:
        if len(data[word.upper()])>1:
            for i in data[word.upper()]:
                 return i 
                #print(i)
            else:
                #print(data[word][0])
                return data[word][0]
     
    elif word.title() in data:
        if len(data[word.title()])>1:
            for i in data[word.title()]:
               # print(i)
                return i
            else:
                #print(data[word][0])
                return data[word][0]

    else:
      close_match=get_close_matches(word,data.keys())
      if len(close_match)>0:
          decide=messagebox.askquestion("askquestion","want closest word?")
          #decide=input("enter yes or no to move forward: ")
          if decide=='yes':
              #print( "the closest word ",close_match[0])
              for i in data[close_match[0]]:
                  #print(i)
                  global b
                  b=close_match[0]
                  return i
          else:
               a="word not found"
               return a 
      else:
          a="cant find this word"
          return a 
          

          
def get_bt():
   inputvalue=word.get()
   words=get_meaning(inputvalue)
   #for i in range(len(words )):
   if b!=0:
        a.insert(END, "THE CLOSEST WORD IS : "+"'"+b+"'"+"\n")
        a.insert(END,words)
        if bt1["text"]=='search':
           bt1.configure(state=DISABLED)

   elif b==0:     
       a.insert(END,words)
       if bt1["text"]=='search':
           bt1.configure(state=DISABLED)
           a.configure(state=DISABLED)
   

def clr_bt():
    a.configure(state=NORMAL)
    word.delete(0,'end')
    a.delete('1.0','end')
    bt1.configure(state=NORMAL)
    

    
text1=Label(root,text="Enter a word :",font=("Arial",10)).grid(row=1,column=0)
word=Entry(root,width=30,font=("Arial",15),textvariable="entry_word",cursor='hand2')
word.grid(row=1,column=1,padx=10,pady=20)
bt1=Button(root,text='search',width=10,height=1,font=("helvetica",10),command=get_bt,state=NORMAL)
bt1.grid(row=1,column=2,padx=5,pady=20)
a=Text(root,width=40,height=20,font=("Arial",15),cursor='dot',wrap='word')
a.grid(row=3,column=1)
clr_button=Button(root,text="clear_all",width=18,height=3,command=clr_bt).grid(row=4,column=1,padx=10,pady=20)
 

#when we resize the screen the rows and columns also get expand or shrinked with this code
root.columnconfigure(0,weight=0,minsize=50)
root.columnconfigure(1,weight=1,minsize=50)

root.rowconfigure(0,weight=1,minsize=50)
#root.rowconfigure(1,weight=1,minsize=50)
root.rowconfigure(2,weight=1,minsize=50)
root.rowconfigure(3,weight=1,minsize=50)

root.mainloop()

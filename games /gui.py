#graphical user interface 
from tkinter import *

window = Tk() #initiate window 
window.geometry("420x420")# changre window size 
window.title(" GUI programme") # change the title of window
window.config(background = "red")

label = Label(window,text=" hello mathafaks" ,#text on window
              font = ('Arial',40,'bold'),#font
              fg='green',#background color
              relief=RAISED,
              bd=10,# border
              padx=20,#padding
              pady=20,
              )
label.pack()

#button 
def click():
    print("you clicked me dawg!")
button = Button(window,
                text="click me !", # button text 
                command = click, # call back so no parentheses 
                font= ("Comic Sans",30),
                fg="#00FF00",#text color in buttons 
                bg="black" #backgroundcolor
                )
button.pack()

#a simple entry box 
def submit():#function for submit button
    username=entry.get()
    print("Hello" +username)

def delete(): #delete button
    entry.delete(0,END)

entry = Entry(window,
              font=("Arial",50),
              fg="#00FF00",
              bg="black"
              )
entry.insert(0,'input text') #default text
entry.pack(side=LEFT) #displays the input space on the window 
submit_button = Button(window,text="submit",command= submit)
submit_button.pack(side=LEFT)

delete_button = Button(window,text="delete",command= delete)
delete_button.pack(side=LEFT)


window.mainloop() #display window on screen,listen to events 
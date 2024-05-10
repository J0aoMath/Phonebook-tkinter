from tkinter import *
from tkinter import ttk

#colors
white1 = "#ffffff"
black1 = "#000000"
blue1 = "#4456F0"
#Window Configuration
window = Tk()
window.title("")
ResW = window.winfo_screenwidth()
ResH = window.winfo_screenheight()
width_W = 485
height_W = 450
Posx = ResW/2 - width_W/2
Posy = ResH/2 - height_W/2
window.configure(background=white1)
window.resizable(width=FALSE,height=FALSE)
window.geometry('%dx%d+%d+%d'%(width_W,height_W,Posx,Posy))
#Frames
frame_up = Frame(window,width=500,height=50,bg=blue1)
frame_up.grid(row=0,column=0,padx=0,pady=1)
frame_down = Frame(window,width=500,height=150,bg=white1)
frame_down.grid(row=1,column=0,padx=0,pady=1)
frame_table = Frame(window,width=500,height=100,bg=white1)
frame_table.grid(row=2,column=0,padx=0,pady=1)
#Frame_up Widgets
app_name = Label(frame_up, text="Phonebook", height = 1, font=('Verdana 17 bold'),bg=blue1,fg=white1)
app_name.place(x=5,y=5)
#Frame_Down Widgets
l_name = Label(frame_down, text='Name *', width=20, height=1, font=('Ivy 10'), bg=white1, anchor=NW)
l_name.place(x=10,y=20)
e_name = Entry(frame_down, width=25,justify='left',highlightthickness=1,relief='solid')
e_name.place(x=80,y=20)

l_gender = Label(frame_down, text='gender *', width=20, height=1, font=('Ivy 10'), bg=white1, anchor=NW)
l_gender.place(x=10,y=50)
c_gender = ttk.Combobox(frame_down, width=27)
c_gender['values'] = ['','F','M']
c_gender.place(x=80,y=50)

l_telephone = Label(frame_down, text='Telephone *', width=20, height=1, font=('Ivy 10'), bg=white1, anchor=NW)
l_telephone.place(x=10,y=80)
e_telephone = Entry(frame_down, width=25,justify='left',highlightthickness=1,relief='solid')
e_telephone.place(x=80,y=80)

l_email = Label(frame_down, text='E-mail *', width=20, height=1, font=('Ivy 10'), bg=white1, anchor=NW)
l_email.place(x=10,y=110)
e_email = Entry(frame_down, width=25,justify='left',highlightthickness=1,relief='solid')
e_email.place(x=80,y=110)

window.mainloop()
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
frame_table.grid(row=2,column=0,columnspan=2,padx=0,pady=1,sticky=NW)
#Functions
def show():
    global tree
    listheader=['Name', 'Gender', 'Telephone', 'Email']
    tree = ttk.Treeview(frame_table, selectmode='extended', columns=listheader,show='headings')
    vsb = Scrollbar(frame_table,orient='vertical',command=tree.yview)
    hsb = Scrollbar(frame_table,orient='horizontal',command=tree.xview)
    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
    tree.grid(column=0,row=0,sticky='nsew')
    vsb.grid(column=1,row=0,sticky='ns')
    hsb.grid(column=0,row=1,sticky='ew')
    #tree head
    tree.heading(0,text='Name',anchor=NW)
    tree.heading(1,text='Gender',anchor=NW)
    tree.heading(2,text='Telephone',anchor=NW)
    tree.heading(3,text='Email',anchor=NW)
    #tree columns
    tree.column(0,width=150,anchor='nw')
    tree.column(1,width=70,anchor='nw')
    tree.column(2,width=120,anchor='nw')
    tree.column(3,width=120,anchor='nw')
    
show()
#Frame_up Widgets
app_name = Label(frame_up, text="Phonebook", height = 1, font=('Verdana 17 bold'),bg=blue1,fg=white1)
app_name.place(x=5,y=5)
#Frame_Down Widgets
l_name = Label(frame_down, text='Name *', width=20, height=1, font=('Ivy 10'), bg=white1, anchor=NW)
l_name.place(x=10,y=20)
e_name = Entry(frame_down, width=25,justify='left',highlightthickness=1,relief='solid')
e_name.place(x=80,y=20)

l_gender = Label(frame_down, text='Gender *', width=20, height=1, font=('Ivy 10'), bg=white1, anchor=NW)
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

b_search = Button(frame_down,text='Search', height=1,bg=blue1,fg=white1,font=('Ivy 8 bold'))
b_search.place(x=290,y=20)
e_search = Entry(frame_down,width=16,justify='left',font=('ivy',11),highlightthickness=1,relief='solid')
e_search.place(x=347,y=20)

b_view = Button(frame_down,text='View', width=10,height=1,bg=blue1,fg=white1,font=('Ivy 8 bold'))
b_view.place(x=290,y=50)

b_add = Button(frame_down,text='Add', width=10,height=1,bg=blue1,fg=white1,font=('Ivy 8 bold'))
b_add.place(x=400,y=50)

b_update = Button(frame_down,text='Update', width=10,height=1,bg=blue1,fg=white1,font=('Ivy 8 bold'))
b_update.place(x=400,y=80)

b_delete = Button(frame_down,text='Delete', width=10,height=1,bg=blue1,fg=white1,font=('Ivy 8 bold'))
b_delete.place(x=400,y=110)



window.mainloop()
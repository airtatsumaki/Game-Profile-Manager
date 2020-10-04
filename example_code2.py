from tkinter import *
from functools import partial
  
def raise_frame(frame):
    frame.tkraise()
  
main_win = Tk()
main_win.geometry('500x500')
main_win.title("Registration Form")
 
second_frame = Frame(main_win)
second_frame.place(x=0, y=0, width=500, height=500)
 
first_frame = Frame(main_win)
first_frame.place(x=0, y=0, width=500, height=500)
 
 
label_0 = Label(first_frame, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
  
  
label_1 = Label(first_frame, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
  
entry_1 = Entry(first_frame)
entry_1.place(x=240,y=130)
  
label_2 = Label(first_frame, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)
  
entry_2 = Entry(first_frame)
entry_2.place(x=240,y=180)
  
label_3 = Label(first_frame, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(first_frame, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(first_frame, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)
  
label_4 = Label(first_frame, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)
  
list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
c=StringVar()
droplist=OptionMenu(first_frame,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)
  
label_4 = Label(first_frame, text="Programming",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var1 = IntVar()
Checkbutton(first_frame, text="java", variable=var1).place(x=235,y=330)
var2 = IntVar()
Checkbutton(first_frame, text="python", variable=var2).place(x=290,y=330)
  
Button(first_frame, text='Submit',width=20,bg='brown',fg='white', command=lambda:raise_frame(second_frame)).place(x=180,y=380)
 
label_8 = Label(second_frame, text="Welcome to page 2",width=20,font=("bold", 10))
label_8.place(x=70,y=230)
 
Button(second_frame, text="Switch back to page 1",width=20,bg='brown',fg='white', command=lambda:raise_frame(first_frame)).place(x=180,y=380) 
 
main_win.mainloop()
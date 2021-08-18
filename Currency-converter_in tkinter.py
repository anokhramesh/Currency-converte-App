#Create an application to convert Dollar to Rupees in python tkinter

from tkinter import *
from tkinter import messagebox

def convert():
    rupee = data.get()*77
    messagebox.showinfo('Converted---','the Rupee is:'+str(rupee))
window =Tk()
window.title("Frame window")
window.geometry('500x200')
frame1=Frame(window,width=100,highlightbackground='red',highlightthickness=3)
frame1.grid(row=0,column=0,padx=20,pady=20,ipadx=20,ipady=20)
l1= Label(frame1,text="Enter the doller",fg='blue',font=(16))
l1.grid(row=0,column=0)
data=IntVar()
textbox=Entry(frame1,textvariable=data,fg='blue',font=(16))
textbox.grid(row=0,column=1)
button1=Button(frame1,command=convert,text='Convert to Rupee',fg='blue',font=(16))
button1.grid(row=1,column=1,sticky=W)
window.mainloop()
#Create an application to convert Dollar to Rupees in python tkinter

from tkinter import *
from tkinter import messagebox

def convert():
    rupee = data.get()*20.23# Enter the Exchange rate here
   # messagebox.showinfo('Converted---','the Rupee is:'+str(rupee))
    l2_Showrupee.config(text="IND Rpees   "+str(rupee))
    #l2_Showrupee.config(text="Amount is "+ str(rupee)+" Rupees")
window =Tk()
window.title("Anokhautomation Currency Converter")
window.geometry('500x260')
window_name=Label(text=" Currency Converter",fg='red',font=('Arial',14,'bold'))
window_name.grid(row=0,column=0)
frame1=Frame(window,width=460,highlightbackground='red',highlightthickness=3)
frame1.grid(row=1,column=0,padx=10,pady=20,ipadx=20,ipady=20)
l1= Label(frame1,text="Enter UAE DHS",fg='blue',font=('Arial',14,'bold'))
l1.grid(row=0,column=0)
l2_Showrupee= Label(frame1,text="IND RS",pady=10,fg='blue',font=('Arial' ,14 ,'bold'))
l2_Showrupee.grid(row=3,column=0)

data=IntVar()
textbox=Entry(frame1,textvariable=data,fg='blue',bg='yellow',font=('Helvetica',14))
textbox.grid(row=0,column=1,padx=10,pady=5)
button1=Button(frame1,command=convert,text='Click to Convert ',bg='green',fg='blue',font=('Arial',16,'bold'))
button1.grid(row=1,column=1,pady=10,sticky=W)
window.mainloop()
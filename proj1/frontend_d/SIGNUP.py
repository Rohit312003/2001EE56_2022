from tkinter import *
from tkinter.ttk import *
from functools import partial
import client

def create_account(newuser,newpassword):
    client.user=newuser.get()
    client.pswd=newpassword.get()
    client.request=0
    client.signup_req()

def signuping():
    signup= Tk()
    signup.title('Tkinter Login Form - pythonexamples.org')
    signup.geometry('800x800')
    Newuserlabel = Label(signup, text="User Name").place(x=680,y=100)
    Newuser = StringVar()
    usernameEntry = Entry(signup, textvariable= Newuser, width=20).place(x=680,y=140)   

	#password label and password entry box
    newpasswordLabel = Label(signup,text="Password").place(x=680,y=180)  
    newpassword = StringVar() 
    passwordEntry = Entry(signup, textvariable=newpassword, show='*').place(x=680,y=220)   
    
    create=partial(create_account,Newuser,newpassword)
	#login button
    loginButton = Button(signup, text="CREAT ACCOUNT",command=create).place(x=700,y=260) 
	
    btn2 = Button(signup, text = 'QUIT', command = signup.destroy)
    btn2.place(x=1200,y=300)  
   


    signup.mainloop()
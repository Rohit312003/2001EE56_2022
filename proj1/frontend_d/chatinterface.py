
from tkinter import *
from tkinter.ttk import *
from functools import partial
import SIGNUP as sign
import client
client.start_connection()
# Create Root Object


tkWindow = Tk()  

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	qwe=username.get().upper()
	if(qwe=="ROHIT" and password.get()=="123"):
			tkWindow.destroy()
			tkWindow2 = Tk()
			tkWindow2.title('Tkinter Login Form - pythonexamples.org')
			tkWindow2.geometry('800x800')  
			Label(tkWindow2,text="WelcomE").grid(row = 0 ,column = 0)
			tkWindow2.mainloop()
	else:
			tkWindow.destroy()
			tkWindow2 = Tk()
			tkWindow2.geometry('800x800')
			tkWindow2.title('Tkinter Login Form - pythonexamples.org')
			Label(tkWindow2,text="Invalid username or password",font=("Helvetica", "10") ).grid(row = 0 ,column = 0)
			tkWindow2.mainloop()
		   
#window
 
	# Create style Object
def start_interface():

	style = Style()
	
	style.configure('TButton', font =('calibri', 16, 'bold'), borderwidth = '4')
	
	# Changes will be reflected
	# by the movement of mouse.
	style.map('TButton', foreground = [('active', '!disabled', 'green')], background = [('active', 'black')])
	

	tkWindow.geometry('400x150')  
	tkWindow.title('Tkinter Login Form - pythonexamples.org')

	#username label and text entry box

	usernameLabel = Label(tkWindow, text="User Name").place(x=680,y=100)  
	username = StringVar()
	usernameEntry = Entry(tkWindow, textvariable=username, width=20).place(x=680,y=140)   

	#password label and password entry box
	passwordLabel = Label(tkWindow,text="Password").place(x=680,y=180)  
	password = StringVar() 
	passwordEntry = Entry(tkWindow, textvariable=password, show='*').place(x=680,y=220)   
	validate = partial(validateLogin, username, password)

	#login button
	loginButton = Button(tkWindow, text="Login", command=validate).place(x=700,y=260) 
	
	btn2 = Button(tkWindow, text = 'QUIT', command = tkWindow.destroy)
	btn2.place(x=1200,y=300)  
	btn2 = Button(tkWindow, text = 'SIGNUP ', command =sign.signuping )
	btn2.place(x=1200,y=20)  
	tkWindow.mainloop()

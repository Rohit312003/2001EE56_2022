import sys
import threading
import time
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
FORMAT = "utf-8"
flag=1
def chat(client,name,initiate):

    def recvMsg(client):
        global flag
        # global chat_msg
        while True and flag:
            try:
                # client.recv(chat_msg.decode(FORMAT))
                print("waiting for msg")
                chat_msg=client.recv(1024).decode(FORMAT)
                print("recieved msg ",chat_msg)
                if chat_msg[:3]=="msg":
                    # entry1.delete(0,END)
                    msg_decode=chat_msg.split("#")
                    recieved_name=msg_decode[1]
                    recieved_msg=msg_decode[2]

                    textCons.config(state=NORMAL)
                    recieved_name=recieved_name[:recieved_name.find(" ")]
                    textCons.insert(END,
                        "{:<15} : {} \n\n".format(recieved_name,recieved_msg))
                        
                    textCons.config(state=DISABLED)
                    textCons.see(END)
                if chat_msg[:chat_msg.find("#")]=="client" and chat_msg[chat_msg.find("#"):]!=name:
                    print(chat_msg[chat_msg.find("#"):],"Joined the chat")
                    showinfo(
                        title='New member joined',
                        message=chat_msg[chat_msg.find("#"):]+" Joined the Chat"
                    )
                if(chat_msg[:chat_msg.find("#")])=="type":
                    typing(chat_msg[chat_msg.find("#"):])
            
            except:
                pass
        return 

    recv_thread=threading.Thread(target=recvMsg,args=(client,))
    recv_thread.start()

    def btn_clicked():
        window.destroy()
        global flag
        flag=0
        client.send("exit".encode(FORMAT))
        print("Button Clicked")
        return


    window = Tk()

    window.geometry("1000x600")
    window.title("CHATROOM")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 600,
        width = 1000,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)


    labelHead = Label(window,
                                bg="white",
                                fg="black",
                                # take username from singup or singin
                                text=name,
                                font="Helvetica 13 bold",
                                pady=5)
    labelHead.place(relwidth=1)

    entry0_img = PhotoImage(file = f"frontend\chatWindow\img_textBox0.png")
    entry0_bg = canvas.create_image(
        384.0, 561.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#a4f089",
        highlightthickness = 0,font="Helvetica 13")

    entry0.place(
        x = 109.0, y = 539,
        width = 550.0,
        height = 43)
    def getthemassage():
        k=entry0.get()
        msg_encode="msg#"+name+"#"+k
        client.send(msg_encode.encode(FORMAT))

        entry0.delete(0,END)

    img0 = PhotoImage(file = f"frontend\\chatWindow\\img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:getthemassage(),
        relief = "flat")

    print(entry0.get())
    b0.place(
        x = 811, y = 526,
        width = 142,
        height = 58)

    def select_file():
        filetypes = (
            ('text files', '*.txt'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=filename
        )

        print(filename)


        import os
        import socket
        client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        PORT = 5000
        SERVER = "172.16.181.29"
        ADDRESS = (SERVER, PORT)
        client.connect(ADDRESS)
        file=open(filename,"rb")
        file_size=os.path.getsize(filename)
        typo=filename.split(".",1)
        kk=typo[1]
        textCons.config(state=NORMAL)
    
        textCons.insert(END,
                        "NAME=> "+ filename+"\n\n")

        textCons.config(state=DISABLED)
        textCons.see(END)
        client.send(("recived."+kk).encode())
        client.send(str(file_size).encode())


        data=file.read()
        client.sendall(data)
        client.send(b"<END>")
        file.close()
        client.close()

    img1 = PhotoImage(file = f"frontend\\chatWindow\\img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda:select_file(),
        relief = "flat")

    b1.place(
        x = 848, y = 427,
        width = 84,
        height = 80)

    img2 = PhotoImage(file = f"frontend\\chatWindow\\img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b2.place(
        x = 848, y = 55,
        width = 92,
        height = 39)

    # entry1_img = PhotoImage(file = f"frontend\\chatWindow\\img_textBox1.png")
    # entry1_bg = canvas.create_image(
    #     474.0, 74.5,
    #     image = entry1_img)

    entry1 = Label(window,
                        bg="white",
                        fg="black",
                        # take username from singup or singin
                        text="",
                        font="Helvetica 10 italic",
                        pady=5)

    entry1.place(
        x = 80, y = 80,
        width = 150,
        height = 14)

    textCons = Text(window,
                                width=18,
                                height=2,
                                bg="#12de22",
                                fg="black",
                                font="Helvetica 10",
                                padx=5,
                                pady=5)

    textCons.place(
        x = 89, y = 128,
        width = 703,
        height = 389)

    # scrolbar
    scrollbar = Scrollbar(textCons)

            # place the scroll bar
            # into the gui window
    scrollbar.place(relheight=1,
                            relx=0.974)
    def threadTyping(client):
        print("typing initiated")
        prevlen=0
        while True and flag:
            # print("Entry is",entry0.get())
            currlen=len(entry0.get())
            if prevlen!=currlen:
                # print(name ,"is typing")
                client.send(str("type#"+str(name)).encode(FORMAT))
                prevlen=currlen
            time.sleep(0.7)

    def typing(typer):
        print(typer,"is typing")
        entry1.config(text=str(typer[1:]+" is typing"))
        time.sleep(1)
        entry1.config(text="")

    thread_typing=threading.Thread(target=threadTyping,args=(client,))
    thread_typing.start()

    scrollbar.config(command=textCons.yview)
    textCons.config(state=DISABLED)
    window.resizable(False, False)
    window.mainloop()
    print("exitted")
    global flag
    flag=0
    client.send("exit".encode(FORMAT))
    exit()
    return
    # sys.exit()

from tkinter import *
import regex as re
returning_value=["exit"]
response=0
def signup():
    global response
    response=0
    # returning_value=["exit"]
    def btn_signup():
        
        # canvas.itemconfig(5,state='normal')
        global response
        response=1
        if len(entry0.get())==0:
            canvas.itemconfig(6,state='normal')
            return
        else:
            canvas.itemconfig(6,state='hidden')

        if validateEmail(getEmail()) and validatePassword(getPassword()):
            global returning_value
            returning_value=[getName(),getEmail(),getPassword()]
            window.destroy()

    def btn_exit():
        global response
        global returning_value
        returning_value=['exit']
        response=1
        window.destroy()
    
    def btn_login():
        global response
        global returning_value
        response=1
        print("login ccc")
        returning_value=["","","login"]
        window.destroy()

    def validateEmail(str):
        pattern=re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b')
        if not re.fullmatch(pattern,str):
            # canvas.itemconfig(5,state='normal')
            print("matched",str)
            canvas.itemconfig(5,state='normal')
            return 0
        else:
            canvas.itemconfig(5,state='hidden')
            return 1

    def validatePassword(str):
        pattern1=re.compile(r'[a-zA-Z]+')
        pattern2=re.compile(r'[0-9]+')
        if(len(str)<6) or  re.fullmatch(pattern1,str) or re.fullmatch(pattern2,str):
            canvas.itemconfig(7,state='normal')
            canvas.itemconfig(8,state='normal')
            return 0
        else:
            canvas.itemconfig(7,state='hidden')
            canvas.itemconfig(8,state='hidden')
            return 1


    def getName():
        return entry0.get()

    def getEmail():
        return entry2.get()

    def getPassword():
        return entry3.get()



    window = Tk()

    window.geometry("1000x600")
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

    background_img = PhotoImage(file = f"frontend\\signup\\background.png")
    background = canvas.create_image(
        502.0, 292.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"frontend\\signup\\img_textBox0.png")
    entry0_bg = canvas.create_image(
        559.5, 193.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#eeecec",
        highlightthickness = 0,font=('Ubuntu 16'))

    entry0.place(
        x = 367.0, y = 171,
        width = 385.0,
        height = 43)
    entry0.focus_set()

    entry2_img = PhotoImage(file = f"frontend\\signup\\img_textBox2.png")
    entry2_bg = canvas.create_image(
        559.5, 263.5,
        image = entry2_img)

    entry2 = Entry(
        bd = 0,
        bg = "#eeecec",
        highlightthickness = 0,font=('Ubuntu 16'))

    entry2.place(
        x = 367.0, y = 241,
        width = 385.0,
        height = 43)

    entry3_img = PhotoImage(file = f"frontend\\signup\\img_textBox2.png")
    entry3_bg = canvas.create_image(
        566.5, 333.5,
        image = entry3_img)

    entry3 = Entry(
        bd = 0,
        bg = "#eeecec",
        highlightthickness = 0,show="\u25CF",font=('Ubuntu 16'))

    entry3.place(
        x = 374.0, y = 311,
        width = 385.0,
        height = 43)

    img0 = PhotoImage(file = f"frontend\\signup\\img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_signup,
        relief = "flat")

    b0.place(
        x = 398, y = 416,
        width = 162,
        height = 39)

    img1 = PhotoImage(file = f"frontend\\signup\\img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_login,
        relief = "flat")

    b1.place(
        x = 579, y = 416,
        width = 162,
        height = 39)

    img2 = PhotoImage(file = f"frontend\\signup\\img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_exit,
        relief = "flat")

    b2.place(
        x = 803, y = 49,
        width = 92,
        height = 39)

    canvas.create_text(
        883.5, 261.0,
        text = "Invalid Email ID !",
        fill = "#df1818",
        font = ("None", int(12.0)),
        state="hidden")

    canvas.create_text(
        843.5, 194.0,
        text = "Enter your Name !",
        fill = "#df1818",
        font = ("None", int(12.0)),
        state="hidden")

    canvas.create_text(
        883.5, 341.0,
        text = "Weak password !",
        fill = "#df1818",
        font = ("None", int(12.0)),
        state="hidden")

    canvas.create_text(
        497.5, 367.0,
        text = "Use combination of atleast 6 albhabets, numbers",
        fill = "#18df5c",
        font = ("None", int(12.0)),
        state="hidden")

    window.resizable(False, False)

    window.mainloop()
    if response==0:
        return ["exit"]
    return returning_value

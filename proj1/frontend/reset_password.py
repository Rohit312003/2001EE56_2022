from tkinter import *


def btn_clicked():
    print("Button Clicked")


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

background_img = PhotoImage(file = f"frontend\\resetPassword\\background.png")
background = canvas.create_image(
    502.0, 294.0,
    image=background_img)

entry0_img = PhotoImage(file = f"frontend\\resetPassword\\img_textBox0.png")
entry0_bg = canvas.create_image(
    558.5, 214.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#eeecec",
    highlightthickness = 0)

entry0.place(
    x = 366.0, y = 192,
    width = 385.0,
    height = 43)

entry1_img = PhotoImage(file = f"frontend\\resetPassword\\img_textBox1.png")
entry1_bg = canvas.create_image(
    558.5, 214.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#eeecec",
    highlightthickness = 0)

entry1.place(
    x = 366.0, y = 192,
    width = 385.0,
    height = 43)

entry2_img = PhotoImage(file = f"frontend\\resetPassword\\img_textBox2.png")
entry2_bg = canvas.create_image(
    466.0, 368.5,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#eeecec",
    highlightthickness = 0)

entry2.place(
    x = 371.0, y = 346,
    width = 190.0,
    height = 43)

img0 = PhotoImage(file = f"frontend\\resetPassword\\img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 351, y = 259,
    width = 151,
    height = 53)

img1 = PhotoImage(file = f"frontend\\resetPassword\\img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 627, y = 338,
    width = 151,
    height = 53)

window.resizable(False, False)
window.mainloop()

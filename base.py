from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("base.py")
root.iconbitmap("images/mellon.ico")


def open():
    global my_img  # è importante mettere questo "global" nell'immagine
    top = Toplevel()
    top.title("Second title")
    top.iconbitmap("images/beach_umbrella.ico")
    my_img = ImageTk.PhotoImage(Image.open("images/eli_resized.jpg"))

    my_label = Label(top, image=my_img).pack()
    btn2 = Button(top, text="close window", command=top.destroy).pack()


btn = Button(root, text="Open second window", command=open).pack()

mainloop()

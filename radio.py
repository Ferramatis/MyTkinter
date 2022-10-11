from msilib.schema import RadioButton
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("radio.py")
root.iconbitmap("images/mellon.ico")

#r = IntVar()
# r.set("2")
# r = StrVar()

MODES = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushroom", "Mushroom"),
    ("Onion", "Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def click(value):
    myLabel = Label(root, text=value)
    myLabel.pack(anchor=W)


# Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: click(r.get())).pack()
# Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: click(r.get())).pack()


myButton = Button(root, text="Click me!",
                  command=lambda: click(pizza.get()))

myButton.pack()

root.mainloop()

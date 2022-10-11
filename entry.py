from tkinter import *

root = Tk()

e = Entry(root, width=50, bg="blue", fg="pink", borderwidt=5)
e.pack()
e.insert(0, "Enter Your Name: ")


def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


#myButton = Button(root, text = "Click me", state = DISABLED)
#myButton = Button(root, text = "Click me", padx = 50, pady = 50 )
myButton = Button(root, text="Enter your name",
                  command=myClick, fg="blue", bg="red")

myButton.pack()

root.mainloop()

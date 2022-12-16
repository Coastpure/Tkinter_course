from tkinter import *

root = Tk()

def myclick():
    myLabel = Label(root, text="Look! I clicked a button",fg="violet")
    myLabel.pack()

myButton = Button(root, text="Click Me", command=myclick, fg="blue",bg="violet")
myButton.pack()



root.mainloop()
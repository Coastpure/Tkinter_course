from tkinter import*
from PIL import ImageTk, Image

root = Tk()
root.title("Frame")
root.iconbitmap('C:/Users/hp/PycharmProjects/Tkinter_tutorial/Nvidia.ico')


frame = LabelFrame(root,  padx=50, pady=50)
frame.pack(padx=10, pady=10)

# we want the button in the root, not the frame
b = Button(frame, text="Don't Click Here!")
b2 = Button(frame, text="...or Here!")
# b.pack()
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()
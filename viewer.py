from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Simael')
root.iconbitmap('C:/Users/hp/PycharmProjects/Tkinter_tutorial/Nvidia.ico')

my_img1 = ImageTk.PhotoImage(Image.open("images/lena.png"))
my_img2 = ImageTk.PhotoImage(Image.open("images/camera1.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/bag1.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("images/city2.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("images/headphone1.jpg"))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

my_label = Label(image=my_img1)

# below image, we're going to have 3 buttons, next back and exit'
my_label.grid(row=0, column=0, columnspan=3)

# buttons
button_back = Button(root, text="<<")
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>")

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2)

root.mainloop()

from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Simael')
root.iconbitmap('C:/Users/hp/PycharmProjects/Tkinter_course/Nvidia.ico')


my_img = ImageTk.PhotoImage(Image.open("images/lena.png"))
my_label = Label(image=my_img)
my_label.pack()

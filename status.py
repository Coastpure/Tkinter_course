# add the counter that shows image x of x
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

# we created all our images into a python list
image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

# status that shows number of images
# use anchor to move status button to right E means east
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
# below image, we're going to have 3 buttons, next back and exit'
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    # what is happening in this function
    # we create a counter, to reference the next item in that list, forget the previous one using my_label.grid_forget()
    # and everytime we click the buttons we just need to update the buttons, which is why we created the globals,
    # so that the updated buttons will work outside the function

    # make the image disappear after we click next
    my_label.grid_forget()

    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 5:
        button_forward = Button(root, text=">>", state=DISABLED)

    # display buttons on screen
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # update status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number ==1:
        button_back = Button(root, text="<<", state=DISABLED)

    # display buttons on screen
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # update status bar
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


# buttons
button_back = Button(root, text="<<", command=back, state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))

# button positioning
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)

# status button
# use sticky to stretch status button west and east means left to right i.e W + E
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()


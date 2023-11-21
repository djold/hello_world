from tkinter import *

root = Tk()

btn = Button(root, text='Click Me!',padx="37", pady="73", bg="red", fg="black", bd="7", state="disabled")
btn.
def tynsd():
    # btn = Button(root, text='Click Me!', state="active")
    setattr(btn, 'state', "active") 
    # btn.grid(row=3, column=13)

qwe = Button(root, text="sandred!", command=tynsd)


qwe.grid(row=3, column=3)
btn.grid(row=3, column=13)
my_label = Label(root, text="Hello World")

my_labelqwer = Label(root, text="Hello cat")
 
my_label.grid(row=1, column=3)
my_labelqwer.grid(row=4, column=6)
































root.mainloop()













































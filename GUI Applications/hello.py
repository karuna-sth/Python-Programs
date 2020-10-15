from tkinter import *

root = Tk()

# window format
root.title("Hello World")
root.configure(background="#D7CACA")
root.geometry("600x500")
root.resizable(height=False, width=False)

# Creating widgets
myLabel = Label(root, text="Hello World")
myLabel.pack()

root.mainloop()

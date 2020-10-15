from tkinter import *

root = Tk()

root.title("Feet to Centimeter Convertor")
root.geometry("350x280")
root.resizable(height=False, width=False)


def convert_to_cm():
    ft_input = float(ft_entry.get())
    centi = ft_input * 30.48
    cm_value.set("%.4f" % centi)


def convert_to_ft():
    cm_input = float(cm_entry.get())
    feet = cm_input / 30.48
    ft_value.set("%.4f" % feet)


def clear():
    cm_value.set("")
    ft_value.set("")


# Widgets for feet
ft_label = Label(root, text="Feet", bg="#D7CACA", width=14)
ft_label.grid(row=0, column=2)

ft_value = DoubleVar()
ft_entry = Entry(root, textvariable=ft_value, width=14)
ft_entry.grid(row=0, column=0, padx=35, pady=40)
ft_entry.delete(0, 'end')

# Widgets for cm
cm_label = Label(root, text="Centimeter", width=14, bg="#D7CACA")
cm_label.grid(row=1, column=2)

cm_value = DoubleVar()
cm_entry = Entry(root, textvariable=cm_value, width=14)
cm_entry.grid(row=1, column=0)
cm_entry.delete(0, 'end')

# Widget for convert and clear
to_convert_ft = Button(root, text="Convert to CM", bg="blue", command=convert_to_cm)
to_convert_ft.grid(row=3, column=0, padx=25, pady=30)

to_convert_cm = Button(root, text="Convert to Feet", bg="blue", command=convert_to_ft)
to_convert_cm.grid(row=3, column=2)

to_clear = Button(root, text="Clear", bg="blue", command=clear)
to_clear.grid(row=4, column=0)

unit_value = Label(root, text="1 feet = 30.48 Cm")
unit_value.grid(row=4, column=2)

root.mainloop()

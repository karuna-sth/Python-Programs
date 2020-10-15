from tkinter import *


class CurrencyConvertor(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("Currency Convertor")
        self.root.geometry("400x400")
        self.root.resizable(height=False, width=False)

        self.amount = StringVar()
        self.rate = StringVar()
        self.converted = StringVar()

        self.create_widgets()
        self.create_buttons()
        self.root.mainloop()

    def create_widgets(self):
        Label(self.root, text="Amount to Convert").grid(row=0, column=0, padx=30, pady=40)
        Entry(self.root, textvariable=self.amount).grid(row=0, column=1)
        Label(self.root, text="Conversion Rate").grid(row=1, column=0)
        Entry(self.root, textvariable=self.rate).grid(row=1, column=1)
        Label(self.root, text="Converted Amount").grid(row=2, column=0, padx=30, pady=40)
        Label(self.root, textvariable=self.converted).grid(row=2, column=1)

    def create_buttons(self):
        Button(self.root, text="Convert", command=self.convert, bg="tomato").grid(row=3, column=0)
        Button(self.root, text="Clear", command=self.clear, bg="tomato").grid(row=3, column=1)

    def convert(self):
        amount = float(self.amount.get())
        rate = float(self.rate.get())
        converted_amt = rate * amount
        self.converted.set(converted_amt)

    def clear(self):
        self.amount.set("")
        self.rate.set("")
        self.converted.set("")


CurrencyConvertor()

from tkinter import *


class TipCalculator(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("Tip Calculator")
        self.root.geometry("400x400")

        self.meal_cost = StringVar()
        self.tip_percent = IntVar()
        self.tip = StringVar()
        self.total_amount = StringVar()

        self.create_widgets()
        self.create_radiobutton()
        self.root.mainloop()

    def create_widgets(self):
        Label(self.root, text="Bill Amount").grid(row=0, column=0, padx=50, pady=30)
        Entry(self.root, textvariable=self.meal_cost).grid(row=0, column=1, columnspan=5)
        Label(self.root, text="Select Tip \nPercentage").grid(row=1, column=0, pady=30, rowspan=2)
        Label(self.root, text="Tip Amount").grid(row=3, column=0, padx=30, pady=30)
        Entry(self.root, textvariable=self.tip).grid(row=3, column=1, columnspan=5)
        Label(self.root, text="Total Amount").grid(row=4, column=0, padx=30, pady=30)
        Entry(self.root, textvariable=self.total_amount).grid(row=4, column=1, columnspan=5)
        Button(self.root, text="Calculate", bg="tomato", command=self.calculate).grid(row=5, column=0)
        Button(self.root, text="Clear", bg="tomato", command=self.clear).grid(row=5, column=2)

    def create_radiobutton(self):
        Radiobutton(self.root, text="1%", variable=self.tip_percent, value=1).grid(row=1, column=1)
        Radiobutton(self.root, text="5%", variable=self.tip_percent, value=5).grid(row=1, column=2)
        Radiobutton(self.root, text="10%", variable=self.tip_percent, value=10).grid(row=1, column=3)
        Radiobutton(self.root, text="15%", variable=self.tip_percent, value=15).grid(row=2, column=1)
        Radiobutton(self.root, text="20%", variable=self.tip_percent, value=20).grid(row=2, column=2)
        Radiobutton(self.root, text="30%", variable=self.tip_percent, value=30).grid(row=2, column=3)

    def calculate(self):
        cost_input = float(self.meal_cost.get())
        percentage = self.tip_percent.get()/100
        tip_amount = percentage*cost_input
        total = cost_input + tip_amount
        self.tip.set(tip_amount)
        self.total_amount.set(total)

    def clear(self):
        self.meal_cost.set("")
        self.tip.set("")
        self.total_amount.set("")


TipCalculator()

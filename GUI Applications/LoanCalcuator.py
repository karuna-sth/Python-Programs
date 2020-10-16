from tkinter import *


class LoanCalculator(object):
    def __init__(self):
        self.root = Tk()
        self.root.title("Loan Calculator")
        self.root.geometry("400x400")
        self.root.resizable(height=False, width=False)

        self.loan_amt = StringVar()
        self.rate = StringVar()
        self.time = StringVar()
        self.total_pay = StringVar()
        self.monthly_pay = StringVar()
        self.interest_amt = StringVar()

        self.create_widgets()
        self.create_buttons()
        self.root.mainloop()

    def create_widgets(self):
        Label(self.root, text="Loan Amount").grid(row=0, column=0, sticky="W", padx=20, pady=15)
        Label(self.root, text="Interest Rate").grid(row=1, column=0, sticky="W", padx=20, pady=15)
        Label(self.root, text="Time(in years)").grid(row=2, column=0, sticky="W", padx=20, pady=15)
        Label(self.root, text="Interest amount").grid(row=3, column=0, sticky="W", padx=20, pady=15)
        Label(self.root, text="Total Payment").grid(row=4, column=0, sticky="W", padx=20, pady=15)
        Label(self.root, text="Monthly Payment").grid(row=5, column=0, sticky="W", padx=20, pady=15)

        Entry(self.root, textvariable=self.loan_amt, justify=RIGHT).grid(row=0, column=1, padx=20, pady=15)
        Entry(self.root, textvariable=self.rate, justify=RIGHT).grid(row=1, column=1, padx=20, pady=15)
        Entry(self.root, textvariable=self.time, justify=RIGHT).grid(row=2, column=1, padx=20, pady=15)

        Label(self.root, textvariable=self.interest_amt, justify=RIGHT).grid(row=3, column=1, padx=20, pady=15)
        Label(self.root, textvariable=self.total_pay, justify=RIGHT).grid(row=4, column=1, padx=20, pady=15)
        Label(self.root, textvariable=self.monthly_pay, justify=RIGHT).grid(row=5, column=1, padx=20, pady=15)

    def create_buttons(self):
        Button(self.root, text="Clear", bg="tomato", command=self.clear).grid(row=6, column=0)
        Button(self.root, text="Calculate", bg="tomato", command=self.calculate).grid(row=6, column=1)

    def calculate(self):
        amt = float(self.loan_amt.get())
        rate = float(self.rate.get())
        time = float(self.time.get())
        int_amt = (amt * rate * time) / 100
        total = int_amt + amt
        monthly = total / (12*time)
        self.interest_amt.set(int_amt)
        self.total_pay.set(total)
        self.monthly_pay.set("%.2f" % monthly)

    def clear(self):
        self.interest_amt.set("")
        self.loan_amt.set("")
        self.rate.set("")
        self.total_pay.set("")
        self.monthly_pay.set("")
        self.time.set("")


LoanCalculator()

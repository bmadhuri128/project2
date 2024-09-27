from tkinter import *
from tkinter import messagebox

class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

class Account:
    def __init__(self):
        self.number = 0
        self.name = ""
        self.acct_no = 0
        self.mobile_no = 0.0
        self.street = ""
        self.city = ""
        self.acct_type = ""
        self.oldbalance = 0.0
        self.newbalance = 0.0
        self.payment = 0.0
        self.lastpayment = Date(0, 0, 0)
10
def input_data():
    global customer
    customer.number += 1
    customer.acct_no = int(account_no_entry.get())
    customer.name = name_entry.get()
    customer.mobile_no = float(mobile_no_entry.get())
    customer.street = street_entry.get()
    customer.city = city_entry.get()
    customer.oldbalance = float(oldbalance_entry.get())
    customer.payment = float(payment_entry.get())
    customer.lastpayment = Date(*map(int, lastpayment_entry.get().split('/')))
    if customer.payment > 0:
        customer.acct_type = 'O' if customer.payment < 0.1 * customer.oldbalance else 'D'
    else:
        customer.acct_type = 'D' if customer.oldbalance > 0 else 'C'
    customer.newbalance = customer.oldbalance - customer.payment
    write_file()
def write_file():
    global customer
    with open("bidur.dat", "a") as file:
file.write(f"{customer.number},{customer.name},{customer.acct_no},{customer.mobile_no},{customer.street},{customer.city},{customer.acct_type},{customer.oldbalance},{customer.newbalance},{customer.payment},{customer.lastpayment.month},{customer.lastpayment.day},{customer.lastpayment.year}\n")
    messagebox.showinfo("Success", "Customer account added successfully.")
def search_data():
11
    global customer
    search_option = search_option_var.get()
    search_value = search_entry.get()

    with open("bidur.dat", "r") as file:
        for line in file:
            values = line.strip().split(',')
            if (search_option == 1 and values[2] == search_value) or (search_option == 2 and values[1] == search_value):
                customer.number, customer.name, customer.acct_no, customer.mobile_no, customer.street, customer.city, customer.acct_type, customer.oldbalance, customer.newbalance, customer.payment, customer.lastpayment.month, customer.lastpayment.day, customer.lastpayment.year = map(eval, values)
                show_output()
                return

    messagebox.showerror("Error", "Customer not found.")

def show_output():
    global customer
    output = f"Customer no: {customer.number}\n"
    output += f"Name: {customer.name}\n"
    output += f"Mobile no: {customer.mobile_no}\n"
    output += f"Account number: {customer.acct_no}\n"
    output += f"Street: {customer.street}\n"
    output += f"City: {customer.city}\n"
12
    output += f"Old balance: {customer.oldbalance}\n"
    output += f"Current payment: {customer.payment}\n"
    output += f"New balance: {customer.newbalance}\n"
    output += f"Payment date: {customer.lastpayment.month}/{customer.lastpayment.day}/{customer.lastpayment.year}\n"
    output += "Account status: "
    if customer.acct_type == 'C':
        output += "CURRENT"
    elif customer.acct_type == 'O':
        output += "OVERDUE"
    elif customer.acct_type == 'D':
        output += "DELINQUENT"
    else:
        output += "ERROR"
    messagebox.showinfo("Customer Details", output)
# Create GUI
root = Tk()
root.title("Customer Billing System")
root.geometry("500x400")
# Labels
Label(root, text="CUSTOMER BILLING SYSTEM").pack(pady=10)
Label(root, text="1: Add Account to List").pack()
Label(root, text="2: Search Customer Account").pack()
Label(root, text="3: Exit").pack()
Label(root, text="Select an option:").pack(pady=10)
13
# Option menu
search_option_var = IntVar()
search_option_var.set(1)
search_option_menu = OptionMenu(root, search_option_var, 1, 2)
search_option_menu.pack()

# Entry fields
account_no_entry = Entry(root)
account_no_entry.pack()
name_entry = Entry(root)
name_entry.pack()
mobile_no_entry = Entry(root)
mobile_no_entry.pack()
street_entry = Entry(root)
street_entry.pack()
city_entry = Entry(root)
city_entry.pack()
oldbalance_entry = Entry(root)
oldbalance_entry.pack()
payment_entry = Entry(root)
payment_entry.pack()
lastpayment_entry = Entry(root)
lastpayment_entry.pack()
search_entry = Entry(root)
search_entry.pack(pady=10)
14
# Buttons
Button(root, text="Add Account", command=input_data).pack(pady=5)
Button(root, text="Search Account", command=search_data).pack(pady=5)
Button(root, text="Exit", command=root.quit).pack(pady=5)

# Initialize the customer object
customer = Account()

root.mainloop()














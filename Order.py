from tkinter import *
import tkinter.ttk as ttk
from datetime import datetime
import random
import string

import Order_tables
import OrderManager


class Order:
    def __init__(self, dish, time, o_id):
        self.__dish = []  # Inputting tuples as elements
        self.__dish = dish
        self.__time = time
        self.__id = o_id

    def get_dishes(self):
        return self.__dish

    def get_time(self):
        return self.__time

    def get_id(self):
        return self.__id

    def show_order(self):
        for x in self.__dish:
            print(x)


# Get the values from the table to put into the order
def get_order_values(table: ttk.Treeview):
    list_of_entries = table.get_children()
    ordered = []
    for each in list_of_entries:
        name = table.item(each)['values'][0]
        quan = table.item(each)['values'][1]
        dish = (name, quan)
        ordered.append(dish)
    return ordered


def submit_order(win: Toplevel, table, e: Entry, num):
    if e.get() != '':
        return
    # id
    letter = string.ascii_letters
    result_id = str(num).join(random.choice(letter) for i in range(4))
    # Order time
    current_time = datetime.now()
    dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")

    new_order = Order(get_order_values(table), dt_string, result_id)

    new_order.show_order()

    OrderManager.add_into_order_list(new_order)

    win.destroy()


def submit_edition(eff, e: Entry, t: Toplevel, table: ttk.Treeview):
    cur_item = table.focus()
    or_name = table.item(cur_item)['values'][0]
    edited_data = [or_name, e.get()]
    selected_item = table.selection()[0]
    table.item(selected_item, text="blub", values=edited_data)
    t.destroy()


def edit_order(eff, root: Toplevel, table: ttk.Treeview):
    if len(table.selection()) == 0:
        err = Toplevel(root)
        err.title("ERROR")
        message = Label(err, text="You did not select the dish to edit!", font=("Arial", 50))
        message.pack()
        return
    pop = Toplevel()
    pop.resizable(False, False)
    pop.title("Edit quantity")

    edit_text = Label(pop, text="Edit quantity:", font=("Arial", 10))
    edit_text.grid(column=0, row=0, padx=10, pady=10)

    edit_entry = Entry(pop, font=("Arial", 10))
    edit_entry.grid(column=1, row=0, padx=10, pady=10)
    edit_entry.bind('<Return>', lambda eff: submit_edition(eff, edit_entry, pop, table))


def add(eff, quantity: Entry, table: ttk.Treeview, data):
    if Order_tables.get_name_data() == "":
        Order_tables.set_name_data(data)
    # Extract quantity data from entry set
    quantity_data = quantity.get()
    name_data = Order_tables.get_name_data()
    new_data = [name_data, quantity_data]
    table.insert('', END, values=new_data)
    print("Adding---->" + Order_tables.get_name_data())         # Debug
    quantity.delete(0, 'end')


def option_menu_select(val, display_text, var, choices, Menu):
    display_text.set(val)
    choice = var.get()
    for i in range(len(choices)):
        if choices[i] == choice:
            # Extract name of the selected option
            Order_tables.set_name_data(Menu[i][0])
            print(Order_tables.get_name_data())
            return


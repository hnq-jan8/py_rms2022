from tkinter import *
import tkinter.ttk as ttk
import Admin


class Menu:
    def __init__(self):
        self.__dishes = []

    def get_dishes(self):
        return self.__dishes

    def add_dish(self, name, price):
        new_dish = [name, price]
        self.__dishes.append(new_dish)

        for d in self.__dishes:
            print(d)

    def edit_dish(self, edited_name, edited_price, or_name, or_price):
        if edited_name == or_name and edited_price == or_price:
            return
        else:
            for i in range(len(self.__dishes)):
                if self.__dishes[i][0] == or_name:
                    self.__dishes[i][0] = edited_name
                    self.__dishes[i][1] = edited_price
                    break
        for d in self.__dishes:
            print(d)

    def delete_dish(self, name):
        for d in self.__dishes:
            if d[0] == name:
                self.__dishes.remove(d)
                break

        for d in self.__dishes:
            print(d)


def get_data_from_file():
    with open('Menu.txt', 'r') as rf:
        for line in rf:
            line_split = line.partition(':')
            dish_name = line_split[0]
            line_split2 = line_split[2]
            line_split2_split = line_split2.partition('\n')
            dish_price = line_split2_split[0]
            new_menu.add_dish(dish_name, dish_price)


def show_data_from_file(table: ttk.Treeview):
    with open('Menu.txt', 'r') as rf:
        for line in rf:
            line_split = line.partition(':')
            dish_name = line_split[0]
            dish_price = line_split[2]
            data = [dish_name, dish_price]
            table.insert('', END, values=data)


def edit_data_in_file(dish_name, edited_name, edited_price):
    i = 0
    with open('Menu.txt', 'r') as rf:           # Open the file to find the line of the wanted dish name
        for num, line in enumerate(rf):
            if dish_name in line:
                i = num
                break
    print(i)
    with open('Menu.txt', 'r') as f:            # Open the file to get the whole string list
        string_list = f.readlines()
        print(string_list)

    with open('Menu.txt', 'w') as wf:           # Open the file to rewrite the edited string list
        string_list[i] = edited_name + ':' + edited_price + '\n'
        new_file_contents = ''.join(string_list)
        wf.write(new_file_contents)


def add_data_into_file(name, price):
    # Write new data into Menu.txt file
    with open('Menu.txt', 'a') as af:
        af.write(name + ':' + price + '\n')


def delete_data_from_file(name):
    i = 0
    with open('Menu.txt', 'r') as rf:  # Open the file to find the line of the wanted dish name
        for num, line in enumerate(rf):
            if name in line:
                i = num
                break
    with open('Menu.txt', 'r') as f:  # Open the file to get the whole string list
        string_list = f.readlines()
        print(string_list)

    with open('Menu.txt', 'w') as wf:  # Open the file to rewrite the edited string list
        string_list[i] = ''
        new_file_contents = ''.join(string_list)
        wf.write(new_file_contents)


# ----------Create new admin instance---------
new_menu = Menu()
# --------------------------------------------


def submit_addition(dish: Entry, price: Entry, p: Toplevel, table: ttk.Treeview):
    if dish.get() == '' or price.get() == '':
        return
    for i in range(len(new_menu.get_dishes())):
        if dish.get() == new_menu.get_dishes()[i][0]:
            return
    data = [dish.get(), price.get()]
    table.insert('', END, values=data)

    new_menu.add_dish(dish.get(), price.get())

    add_data_into_file(dish.get(), price.get())

    p.destroy()


def submit_edition(dish: Entry, price: Entry, p: Toplevel, table: ttk.Treeview):
    selected_item = table.selection()[0]  # Get selected item

    cur_item = table.focus()
    or_name = table.item(cur_item)['values'][0]
    or_price = table.item(cur_item)['values'][1]
    edited_data = [dish.get(), price.get()]
    edited_name = dish.get()
    edited_price = price.get()

    new_menu.edit_dish(edited_name, edited_price, or_name, or_price)

    edit_data_in_file(or_name, edited_name, edited_price)

    table.item(selected_item, text="blub", values=edited_data)
    p.destroy()


def add(win: Tk, table: ttk.Treeview):
    pop = Toplevel(win)
    pop.resizable(False, False)
    pop.title("Adding new dish")

    # Add dish name
    add_text = Label(pop, text='Add dish:', font=("Arial", 15))
    add_text.grid(column=0, row=0, padx=10, pady=10, sticky=W)

    stuff_entry = Entry(pop, font=("Arial", 15))
    stuff_entry.grid(column=1, row=0, padx=10)

    # Add dish price
    add_price_text = Label(pop, text='Price:', font=("Arial", 15))
    add_price_text.grid(column=0, row=1, padx=10, pady=10, sticky=W)

    price_entry = Entry(pop, font=("Arial", 15))
    price_entry.grid(column=1, row=1, padx=10)

    # Submit addition
    submit_add = Button(pop, text='Enter', command=lambda: submit_addition(stuff_entry, price_entry, pop, table))
    submit_add.grid(columnspan=2, column=0, row=2, padx=10, pady=10)


def edit(win: Tk, table: ttk.Treeview):
    if len(table.selection()) == 0:
        err = Toplevel(win)
        err.title("ERROR")
        message = Label(err, text="You did not select the dish to edit!", font=("Arial", 50))
        message.pack()
        return

    pop = Toplevel(win)
    pop.resizable(False, False)
    pop.title("Edit dishes")

    # Add dish name
    edit_text = Label(pop, text='Edit dish:', font=("Arial", 15))
    edit_text.grid(column=0, row=0, padx=10, pady=10, sticky=W)

    edit_entry = Entry(pop, font=("Arial", 15))
    edit_entry.grid(column=1, row=0, padx=10)

    # Add dish price
    edit_price_text = Label(pop, text='Edit price:', font=("Arial", 15))
    edit_price_text.grid(column=0, row=1, padx=10, pady=10, sticky=W)

    price_entry = Entry(pop, font=("Arial", 15))
    price_entry.grid(column=1, row=1, padx=10)

    # Submit addition
    submit_edit = Button(pop, text='Enter', command=lambda: submit_edition(edit_entry, price_entry, pop, table))
    submit_edit.grid(columnspan=2, column=0, row=2, padx=10, pady=10)


def delete(win: Tk, table: ttk.Treeview):
    if len(table.selection()) == 0:
        err = Toplevel(win)
        err.title("ERROR")
        message = Label(err, text="You did not select the dish to delete!", font=("Arial", 50))
        message.pack()
        return

    cur_item = table.focus()
    name = table.item(cur_item)['values'][0]

    new_menu.delete_dish(name)

    delete_data_from_file(name)

    selected_item = table.selection()[0]  # Get selected item
    table.delete(selected_item)


def main():
    win = Tk()
    win.title("Menu manager")
    win.resizable(False, False)

    # Manager options
    fr = Frame(win)
    fr.grid(rowspan=2, column=0, row=0)
    mng_menu_label = Label(fr, text='Manager menu', font=("Arial Bold", 10))
    mng_menu_label.pack(pady=10)
    bill_mng_butt = Button(fr, text="Bill", font=("Arial", 10), width=10, command=lambda: Admin.open_bill_mng(win))
    bill_mng_butt.pack(padx=5, pady=30)
    employee_mng_butt = Button(fr, text="Employee", font=("Arial", 10), width=10, command=lambda: Admin.open_employee_mng(win))
    employee_mng_butt.pack(padx=5, pady=30)

    # Treeview(table)
    columns = ('name', 'price')
    table = ttk.Treeview(win, columns=columns, show='headings')
    table.heading('name', text="Name")
    table.heading('price', text="Price")
    table.grid(columnspan=3, column=1, row=0)

    add_butt = Button(win, text="Add", padx=50, pady=20, command=lambda: add(win, table))
    add_butt.grid(column=1, row=1, padx=10, pady=20)

    edit_butt = Button(win, text="Edit", padx=50, pady=20, command=lambda: edit(win, table))
    edit_butt.grid(column=2, row=1, padx=10, pady=20)

    del_butt = Button(win, text="Delete", padx=50, pady=20, command=lambda: delete(win, table))
    del_butt.grid(column=3, row=1, padx=10, pady=20)

    win.after(100, get_data_from_file)
    win.after(200, show_data_from_file(table))
    win.mainloop()


if __name__ == "__main__":
    main()

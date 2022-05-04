from tkinter import *
import tkinter.ttk as ttk

import Admin


def print_bill(win: Tk, table: ttk.Treeview):
    eff = ''
    if len(table.selection()) == 0:
        err = Toplevel(win)
        err.title("ERROR")
        message = Label(err, text="You did not select the dish to delete!", font=("Arial", 50))
        message.pack()
        return

    '''#####  Show bill  #####'''
    show_bill(eff, win, table)

    '''#####  Delete bill  #####'''
    delete_bill(win, table)


def delete_bill(win: Tk, table: ttk.Treeview):
    import OrderManager
    OrderManager.fill_list()
    if len(table.selection()) == 0:
        err = Toplevel(win)
        err.title("ERROR")
        message = Label(err, text="You did not select a bill to delete!", font=("Arial", 50))
        message.pack()
        return

    cur_item = table.focus()
    o_id = table.item(cur_item)['values'][1]

    OrderManager.delete_from_order_list(o_id)
    selected_item = table.selection()[0]  # Get selected item
    table.delete(selected_item)


menu = []
orders = []


def get_data_from_menu():
    with open('Menu.txt', 'r') as rf:
        for line in rf:
            line_split = line.partition(':')  # Split the string by ':'
            dish_name = line_split[0]  # dish_name = the string before ':'
            line_split2 = line_split[2]  # Create new string variable line_split2 = the string after ':'
            line_split2_split = line_split2.partition('\n')  # Split the new string variable line_split2 by '\n'
            dish_price = line_split2_split[0]  # dish_price = the string before '\n'

            new_dish = [dish_name, dish_price]
            menu.append(new_dish)


def show_data_from_file(table: ttk.Treeview):
    global orders
    import OrderManager
    orders = OrderManager.load_from_file()
    if orders == -1:
        return
    else:
        for o in orders:
            dishes = o.get_dishes()

            time = o.get_time()
            o_id = o.get_id()
            total_price = cal_total_price(dishes)
            table_num = get_table_from_id(o_id)

            new_data = [table_num, o_id, total_price, time]
            table.insert('', END, values=new_data)


def get_price_of_dish(name):
    for x in menu:
        if name == x[0]:
            return int(x[1])


def cal_total_price(dishes):
    total = 0
    for i in range(len(dishes)):
        name = dishes[i][0]
        amount = dishes[i][1]
        total += amount * get_price_of_dish(name)
    return total


def get_table_from_id(o_id):

    for m in str(o_id):
        if m.isdigit():
            return int(m)


def show_bill(eff, win: Tk, table: ttk.Treeview):
    if len(table.selection()) == 0:
        err = Toplevel(win)
        err.title("ERROR")
        message = Label(err, text="You did not select the dish to delete!", font=("Arial", 50))
        message.pack()
        return
    cur_item = table.focus()
    o_id = table.item(cur_item)['values'][1]
    time = ''
    dishes = []
    total_price = 0
    table_num = get_table_from_id(o_id)

    pop = Toplevel(win)
    pop.resizable(False, False)
    title = "Bill for table " + str(table_num)
    pop.title(title)

    for o in orders:
        if o_id == o.get_id():
            dishes = o.get_dishes()
            time = o.get_time()
            total_price = cal_total_price(dishes)

    time_text = 'Time: ' + time
    time_label = Label(pop, text=time_text, font=("Arial", 15))
    time_label.grid(columnspan=2, column=0, row=0, padx=20, pady=10)

    table_text = 'Table: ' + str(table_num)
    table_label = Label(pop, text=table_text, font=("Arial", 15))
    table_label.grid(column=0, row=1, padx=40, pady=10)

    id_text = 'Bill ID: ' + str(o_id)
    id_label = Label(pop, text=id_text, font=("Arial", 15))
    id_label.grid(column=1, row=1, padx=40, pady=10)

    grid_ = Label(pop, text="****************     BILL     ****************", font=("Arial", 15))
    grid_.grid(columnspan=2, column=0, row=2, padx=40, pady=10)

    next_line = 0
    for i in range(len(dishes)):
        dish_text = str(dishes[i][0]) + "  x" + str(dishes[i][1])
        dish_label = Label(pop, text=dish_text, font=("Arial", 15))
        dish_label.grid(column=0, row=i+3, sticky='w', padx=30)
        next_line = i+4

    for i in range(len(dishes)):
        dish_name = str(dishes[i][0])
        dish_price = str(get_price_of_dish(dish_name))
        price_text1 = dish_price[-3:]       # The last 3 characters
        price_text2 = dish_price[:-3]       # The characters before those last 3 characters
        price_text = price_text2 + '.' + price_text1 + ' đ'
        price_label = Label(pop, text=price_text, font=("Arial", 15))
        price_label.grid(column=1, row=i+3, sticky='w', padx=30)

    text = str(total_price)
    text1 = text[-3:]           # The last 3 characters
    text2 = text[:-3]           # The characters before those last 3 characters
    total_price_text = '********** Total: ' + text2 + '.' + text1 + ' VNĐ ***********'
    total_price_text = Label(pop, text=total_price_text, font=("Arial", 15))
    total_price_text.grid(columnspan=2, column=0, row=next_line, padx=40, pady=10)


def main():
    get_data_from_menu()

    win = Tk()
    win.resizable(False, False)
    win.title("Bill manager")

    # Manager options
    fr = Frame(win)
    fr.grid(rowspan=2, column=0, row=0)
    mng_menu_label = Label(fr, text='Manager menu', font=("Arial Bold", 10))
    mng_menu_label.pack(pady=10)
    bill_mng_butt = Button(fr, text="Employee", font=("Arial", 10), width=10, command=lambda: Admin.open_employee_mng(win))
    bill_mng_butt.pack(padx=5, pady=30)
    employee_mng_butt = Button(fr, text="Menu", font=("Arial", 10), width=10, command=lambda: Admin.open_menu_mng(win))
    employee_mng_butt.pack(padx=5, pady=30)

    # Treeview(table)
    columns = ('table', 'id', 'price', 'time')
    table = ttk.Treeview(win, columns=columns, show='headings')
    table.heading('table', text="Table")
    table.heading('id', text="ID")
    table.heading('price', text="Price")
    table.heading('time', text="Time")
    table.bind('<Double-1>', lambda eff: show_bill(eff, win, table))  # execute edit_order() on 'double click'
    table.grid(columnspan=2, column=1, row=0, padx=5, pady=5)

    edit_butt = Button(win, text="Print", padx=50, pady=20, command=lambda: print_bill(win, table))
    edit_butt.grid(column=1, row=1, padx=10, pady=20)

    del_butt = Button(win, text="Delete", padx=50, pady=20, command=lambda: delete_bill(win, table))
    del_butt.grid(column=2, row=1, padx=10, pady=20)

    win.after(200, show_data_from_file(table))
    win.mainloop()


if __name__ == "__main__":
    main()

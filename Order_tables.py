from tkinter import *
import tkinter.ttk as ttk
import Order

name_data = ""
quantity_data = ""


def get_name_data():
    global name_data
    return name_data


def get_quan_data():
    global quantity_data
    return quantity_data


def set_name_data(data):
    global name_data
    name_data = data


def set_quan_data(data):
    global quantity_data
    quantity_data = data


def debug():
    import OrderManager
    l = OrderManager.load_from_file()
    print(l)


def order_for_table(num):
    menu = []
    # Read Menu.txt file
    with open('Menu.txt', 'r') as rf:
        for line in rf:
            line_split = line.partition(':')  # Split the string by ':'
            dish_name = line_split[0]  # dish_name = the string before ':'
            line_split2 = line_split[2]  # Create new string variable line_split2 = the string after ':'
            line_split2_split = line_split2.partition('\n')  # Split the new string variable line_split2 by '\n'
            dish_price = line_split2_split[0]  # dish_price = the string before '\n'

            new_dish = [dish_name, dish_price]
            menu.append(new_dish)

    choices = [menu[i][0] + "  " + menu[i][1] for i in range(len(menu))]

    root = Toplevel()
    root.resizable(False, False)
    title = "Order for table " + str(num)
    root.title(title)

    display_text = StringVar()
    e1 = Label(root, textvariable=display_text)
    e1.grid(row=0, column=0)

    # Table
    global name_data
    global quantity_data

    columns = ('name', 'quantity')
    table = ttk.Treeview(root, columns=columns, show='headings', height=5)
    table.heading('name', text="Name")
    table.heading('quantity', text="Quantity")
    table.bind('<Double-1>', lambda eff: Order.edit_order(eff, root, table))  # execute edit_order() on 'double click'
    table.grid(column=1, row=0, padx=10)

    var = StringVar()
    var.set(choices[0])
    selected = var.get()
    set_name_data(menu[0][0])
    '''for i in range(len(choices)):
        if choices[i] == selected:
            # Extract name of the selected option
            set_name_data(menu[i][0])'''
    display_text.set(choices[0])
    print(get_name_data())
    popup_menu = OptionMenu(root, var, *choices, command=lambda val: Order.option_menu_select(val, display_text, var, choices, menu))
    popup_menu.grid(row=1, column=0)

    quantity = Entry(root)
    quantity.grid(row=1, column=1, sticky=W)
    quantity.bind("<Return>", lambda eff: Order.add(eff, quantity, table, get_name_data()))  # execute say_hello() on Enter

    # Submit button
    submit = Button(root, text="Submit", padx=30, pady=5, command=lambda: Order.submit_order(root, table, quantity, num))
    submit.grid(columnspan=2, row=2, column=0)


    root.mainloop()


def main():
    import OrderManager
    OrderManager.fill_list()

    win = Tk()
    win.resizable(False, False)
    win.title('Order')

    label = Label(win, text='Choose table to order:', font=("Arial Bold", 15))
    label.grid(columnspan=3, column=0, row=0)

    k = 1
    for i in range(1, 4):
        for j in range(0, 3):
            table_name = "Table " + str(k)
            new_table = Button(win, text=table_name, font=("Arial Bold", 10), padx=10, pady=10,
                               command=lambda num=k: order_for_table(num))
            new_table.grid(column=j, row=i, padx=10, pady=10)
            k += 1

    win.mainloop()


if __name__ == "__main__":
    main()
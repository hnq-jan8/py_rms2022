import os
from input import compress_data, decompress_data, print_tables, print_admin_action
from domains.Table import *
from domains.M_order import *
from domains.M_dish import *
from domains.M_employee import *

d_manager = Dish_Manager()
e_manager = Employee_Manager()
o_manager = Order_Manager()
b_manager = Bill_Manager()

table_list = []  # list of tables
for _ in range(0, 9):
    table_list.append(Table())

if __name__ == '__main__':
    open(f'employees.txt', 'wb')        # to solve problem when program is closed without any employee added
    open(f'dishes.txt', 'wb')           # used when program is closed without any employee added    (rarely happens)
    open(f'bills.txt', 'wb')            # used when program is closed without any bills added       (rarely happens)
    if os.path.exists('res_data.zip'):
        try:
            decompress_data()
            d_manager.load_dishes()
            e_manager.load_employees()
            b_manager.load_bills()
        except Exception as e:
            print(f'(!) Error: {e}')

    while True:
        clr_scr()
        password = input('\nEnter password (type \'0\' to save and exit): ')
        while password != 'admin' and password != 'staff':
            if password == '0':  # Type '0' to save data and exit
                compress_data()
                os.remove('dishes.txt')
                os.remove('employees.txt')
                os.remove('bills.txt')
                print('Data saved.')
                exit()
            clr_scr()
            print('(!) Wrong password')
            password = input('Enter password (type \'0\' to save and exit): ')
        if password == 'admin':
            # Administrator section: food menu, employees, and bills
            while True:
                clr_scr()
                print_admin_action()
                choice = input('\nChoice (1230): ')
                if choice == '0':
                    break
                elif choice == '1':
                    d_manager.start()
                elif choice == '2':
                    e_manager.start()
                elif choice == '3':
                    b_manager.start()

        elif password == 'staff':
            # Staff section: ordering and billing
            while True:
                orders = o_manager.get_orders()
                clr_scr()
                print_tables(table_list)
                choice = input('\nChoice (1-9, 0): ').strip()
                if choice.isdigit() and int(choice) in range(1, 10):    # select table
                    table = table_list[int(choice) - 1]
                    if str(table) == '0':           # if table is empty, start ordering for this table
                        o = o_manager.add_order(int(choice), d_manager)
                        if o != 0:  # if order is added, update table status
                            table.update()
                    elif str(table) == '1':         # if table is occupied, choose to edit order or bill
                        for o in orders:
                            if o.get_table_id() == int(choice):
                                o = o_manager.update_order(o, d_manager, b_manager)
                                if o == -1:             # if bill exported, update table status to empty
                                    table.update()

                elif choice == '0':
                    break
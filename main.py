import os
from input import compress_data, decompress_data, print_admin_action, clean_up
from domains.M_order import *
from domains.M_dish import *
from domains.M_employee import *

d_manager = Dish_Manager()
e_manager = Employee_Manager()
o_manager = Order_Manager()
b_manager = Bill_Manager()

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

    is_unfinished = False       # to check if there is any unfinished order
    while True:
        clr_scr()
        password = input('\nEnter password (type \'0\' to save and exit): ')
        while password != 'admin' and password != 'staff':
            if password == '0':  # Type '0' to save data and exit
                compress_data()
                print('Data saved.')
                if is_unfinished == True:
                    confirm = input('You have unfinished order(s). Please enter \'quit\' to confirm exit: ').strip().lower()
                    if confirm == 'exit':
                        clean_up()
                        exit()
                    else: break
                clean_up()
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
            # Staff section: ordering, and billing
            is_unfinished = o_manager.start(o_manager, d_manager, b_manager)
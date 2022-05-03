from domains.Table import *
from domains.M_bill import *
from domains.Order import Order
from input import write_bill, print_tables, clr_scr

def print_cart(table, cart):
    print(f'''\n---------- Ordering for Table {table} ----------\n
            \rCart:''')
    if len(cart) == 0:
        print('     - empty')
    else:
        for i, (d, q) in enumerate(cart.items()):
            print(f'{i+1:4}. {d:25}\t x {q}')  # print the cart including name, price and quantity
    print('\n------------------------------------------')

def print_menu(dish_list, table):
    print(f'''\n---------- Ordering for Table {table} ----------\n
            \r                  ** Menu **\n
            \r      Name\t\t\t   Price (VND)''')
    for i, d in enumerate(dish_list):
        print(f'{i+1:4}. {d}')    # print the menu
    print('\n                   ** ** **\n')

def order_modify(dish, cart, table_id):
    while True:    # while there are dishes in the menu
        clr_scr()
        print_cart(table_id, cart)
        print('''\na.\t\t | ADD |\n''')
        if len(cart) == 0:
            print('0. <- Cancel')
            choice = input('\nChoice (a, 0): ').strip().lower()
        else:
            print('0. <- Cancel\t    |\t      s. -> Submit')
            choice = input(f'\nChoice (a, 1-{len(cart)}, s, 0): ').strip().lower()
        if choice == '0': return 0      # return 0 if user cancels the ordering process
        elif choice == 'a':   # choose a dish from menu to cart
            while True:
                clr_scr()
                print_menu(dish, table_id)
                select_dish = input(f'''0. <- Back
                                    \r\nAdd (1-{len(dish)}, 0): ''').strip()
                if select_dish == '0': break
                elif select_dish.isdigit() and int(select_dish) <= len(dish):   # select a dish on the menu
                    dish_name = dish[int(select_dish)-1].get_name()
                    if dish_name in cart:       # if the dish is already in the cart
                        cart[dish_name] += 1    # automatically increase the quantity
                        break
                    else:
                        cart[dish_name] = 1     # add selected dish to the cart
                        break
        elif choice.isdigit() and int(choice) <= len(cart):   # choose a dish from the cart
            chosen_item = list(cart.keys())[int(choice)-1]  # get the dish(object) from the cart
            while True:
                clr_scr()
                print(f'''\n---------- Ordering for Table {table_id} ----------\n
                        \rCart:
                        \r  ->  {chosen_item:25}(+) {cart[chosen_item]} (-)
                        \r\n------------------------------------------\n
                        \r0. <- Back                    r. -> Remove''')
                choice = input(f'''\nChoice (+, -, r, 0): ''').strip()
                if choice == '0': break
                elif choice == '+': cart[chosen_item] += 1
                elif choice == '-': 
                    cart[chosen_item] -= 1
                    if cart[chosen_item] == 0:
                        del cart[chosen_item]       # delete the dish from the cart
                        break
                elif choice == 'r':
                    del cart[chosen_item]
                    break
        elif choice == 's':             # submit the order
            if len(cart) == 0:
                continue
            return cart

class Order_Manager:
    def __init__(self):
        self.__orders = []
        self.table_list = []    # list of tables
        for _ in range(0, 9):   # create 9 tables (edit number of tables here)
            self.table_list.append(Table())

    def get_orders(self):
        return self.__orders

    def add_order(self, table_id, dish_manager):
        cart = {}   # {dish0: quantity, dish1: quantity, ...}
        dishes = dish_manager.get_dishes()
        if len(dishes) == 0: return 0
        cart = order_modify(dishes, cart, table_id)
        if cart == 0: return 0
        order = Order(table_id, cart)
        self.__orders.append(order)
        return order     # return the id of the order

    def update_order(self, order, dish_manager, bill_manager):
        cart = order.get_cart()     # load the previous cart
        dishes = dish_manager.get_dishes()
        clr_scr()
        print_cart(order.get_table_id(), cart)
        print('\nDo you want to export bill now?')
        confirm = input('Type \'y\' to confirm: ').strip().lower()
        if confirm == 'y':  # export the bill
            clr_scr()
            num_bills = len(bill_manager.get_bills())   # used to generate the bill id
            prices = []     # list of prices of the dishes in the cart
            for dish in dishes:
                if dish.get_name() in cart:
                    prices.append(dish.get_price())
            bill = Bill(num_bills, order.get_table_id(), cart, prices)
            print(f'\n        >>>   Bill Created   <<<')
            bill_manager.add_bill(bill)
            bill.details()
            write_bill(bill_manager.get_bills())
            input('\nPress Enter to continue...')
            self.__orders.remove(order)
            return -1

        tem_cart = cart.copy()
        tem_cart = order_modify(dishes, tem_cart, order.get_table_id())
        if tem_cart == 0: return order
        order.set_cart(tem_cart)
        return order

    def start(self, order_manager, dish_manager, bill_manager):
        while True:
            orders = order_manager.get_orders()
            clr_scr()
            print_tables(self.table_list)
            choice = input('\nChoice (1-9, 0): ').strip()
            if choice.isdigit() and int(choice) in range(1, 10):    # select table
                table = self.table_list[int(choice) - 1]
                if str(table) == '0':           # if table is empty, start ordering for this table
                    o = order_manager.add_order(int(choice), dish_manager)
                    if o != 0:  # if order is added, update table status
                        table.update()
                elif str(table) == '1':         # if table is occupied, choose to edit order or bill
                    for o in orders:
                        if o.get_table_id() == int(choice):
                            o = order_manager.update_order(o, dish_manager, bill_manager)
                            if o == -1:             # if bill exported, update table status to empty
                                table.update()

            elif choice == '0':
                if len(orders) == 0:
                    return False
                return True
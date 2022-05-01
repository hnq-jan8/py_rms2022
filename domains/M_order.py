import os
from domains.Order import Order
from domains.M_bill import *

def print_cart(table, cart):
    print(f'''\n---------- Ordering for table {table} ----------\n
            \rCart:''')
    if len(cart) == 0:
        print('     - empty')
    else:
        for i, (d, q) in enumerate(cart.items()):
            print(f'{i+1}. {d:25}\tx {q}')  # print the cart including name, price and quantity
    print('\n------------------------------------------')

def print_menu(dish_list, table):
    print(f'''\n---------- Ordering for Table {table} ----------\n
            \r               ** Menu **\n
            \r   Name\t\t\t\tPrice (VND)''')
    for i, d in enumerate(dish_list):
        print(str(i+1) + '.', d)    # print the menu
    print('\n                ** ** **\n')

def total_price(cart, dish_list):
    total = 0
    # from keys of the cart, get the dish(object) from the dish_list
    for dish in dish_list:
        if dish.get_name() in cart:
            total += dish.get_price() * cart[dish.get_name()]
    return total

def order_modify(dish, cart, table_id):
    while True:    # while there are dishes in the menu
        os.system('clear')
        print_cart(table_id, cart)
        print('''\na.\t\t | ADD |\n''')
        if len(cart) == 0:
            print('0. <- Cancel')
            choice = input('\nChoice (a, 0): ').strip().lower()
        else:
            print('0. <- Cancel\t    |\t     s. -> Submit')
            choice = input(f'\nChoice (a, 1-{len(cart)}, 0): ').strip().lower()
        if choice == '0': return 0      # return 0 if user cancels the ordering process
        elif choice == 'a':   # choose a dish from menu to cart
            while True:
                os.system('clear')
                print_menu(dish, table_id)
                select_dish = input(f'''0. <- Back
                                    \r\nChoice (1-{len(dish)}, 0): ''').strip()
                if select_dish == '0': break
                elif select_dish.isdigit() and int(select_dish) in range(1, len(dish)+1):   # select a dish on the menu
                    dish_name = dish[int(select_dish)-1].get_name()
                    if dish_name in cart:       # if the dish is already in the cart
                        cart[dish_name] += 1    # automatically increase the quantity
                        break
                    else:
                        cart[dish_name] = 1     # add selected dish to the cart
                        break
        elif choice.isdigit() and int(choice) in range(1, len(cart)+1):   # choose a dish from the cart
            chosen_item = list(cart.keys())[int(choice)-1]  # get the dish(object) from the cart
            while True:
                os.system('clear')
                print(f'''\n---------- Ordering for table {table_id} ----------\n
                        \rCart:
                        \r-> {chosen_item:25}  (+) {cart[chosen_item]} (-)
                        \r\n------------------------------------------\n
                        \r0. <- Back''')
                choice = input(f'''\nChoice (+, -, 0): ''').strip()
                if choice == '0': break
                elif choice == '+': cart[chosen_item] += 1
                elif choice == '-': 
                    cart[chosen_item] -= 1
                    if cart[chosen_item] == 0:
                        del cart[chosen_item]       # delete the dish from the cart
                        break
        elif choice == 's':
            if len(cart) == 0:
                continue
            return cart

class Order_Manager:
    def __init__(self):
        self.__orders = []

    def get_orders(self):
        return self.__orders

    def add_order(self, table_id, dish_manager):
        print(f'\nOrdering for table {table_id}')
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
        while True:
            os.system('clear')
            print_cart(order.get_table_id(), cart)
            print('\nDo you want to export bill now?')
            confirm = input('Type \'y\' to confirm: ').strip().lower()
            if confirm == 'y':
                num_bills = len(bill_manager.get_bills())   # used to generate the bill id
                bill = Bill(num_bills, order.get_table_id(), cart, total_price(cart, dishes))
                bill_manager.add_bill(bill)
                print(bill.detail(dishes))
                input('\nBill exported. Press Enter to continue...')
                self.__orders.remove(order)
                return -1

            cart = order_modify(dishes, cart, order.get_table_id())
            if cart == 0: return order
            order.set_cart(cart)
            return order
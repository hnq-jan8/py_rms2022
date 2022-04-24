import random

list_chui_khach = ['Cai deo gi day?', 'Dit me may', 'BA10-002 is that u?', '???', 'Occhos', 'hay mày là lê phan tuấn vũ?']
list_food = ['mj tom chua cay vai lon laij truowtj signal', 'xoi pate trong nhu mau bang diem cua ban', 'lonf', 'ăn năn hối lỗi']
list_drink = ['xoài dầm nát bảng điểm nhìn trông như lo duyt của bạn', 'sinh tố bơ bố mày 2 ngày đéo rep ib', 'cà phê cốt dừa loz', 'squirt']

cart = []

def display_menu(any_list):
    for i, item in enumerate(any_list):
        print(f'\t{i + 1}. {item}')
    print(f'''\t{len(any_list) + 1}. "Sao cũm đượt"
            \r\t0. Quit menu''')

def chui_khach():
    print(random.choice(list_chui_khach))

def select_item_on_de_menu(item_menu):
    while True:
        c = input('Your choice: ')
        if not c.isdigit() or int(c) not in range(0, len(item_menu)+2):
            chui_khach()
        else:
            c = int(c)
            if c == 0:
                return 'Chê ://'
            elif c == len(item_menu) + 1:
                return random.choice(item_menu)
            else:
                return item_menu[c-1]

def food():
    print('Welcome to the food menu')
    display_menu(list_food)
    selected_food = select_item_on_de_menu(list_food)
    cart.append(selected_food)
    print(f'Selected {selected_food}')

def drinks():
    print('Welcome to the drink menu')
    display_menu(list_drink)
    selected_drink = select_item_on_de_menu(list_drink)
    cart.append(selected_drink)
    print(f'Selected {selected_drink}')

def who_are_u():
    while True:
        print('''------------------------------
                \r\nWho are you?:
                \r\t1. Customer
                \r\t2. Staff
                \r\t0. Quit''')
        c = input('Your choice (1, 2): ')
        if c == '1':
            menu()
        elif c == '2':
            admin()
        elif c == '0':
            print('Fuck off...')
            break
        else:
            chui_khach()

def admin():
    password = input('Enter your password: ')
    if password == 'admin':
        while True:
            print('Welcome to the admin menu')
            print('''------------------------------
                    \r\nChoose which menu:
                    \r\t1. Storage
                    \r\t2. Staff
                    \r\t3. Loyal customer
                    \r\t0. Quit''')
            c = input('Your choice (1,2,0): ')
            print('\n------------------------------\n')
            if c == '0':
                print('Done ordering!')
                print(cart)
                break
            elif c == '1':
                print('Tình trạng kho')
            elif c == '2':
                print('Danh sách nhân viên')
            elif c == '3':
                print('Khách hàng thân thiết')
            else:
                chui_khach()

def menu():
    while True:
        print('''------------------------------
        \r\nChoose which menu:
        \r\t1. Food menu
        \r\t2. Drinks menu
        \r\t0. Quit''')
        c = input('Your choice (1,2): ')
        print('\n------------------------------\n')
        if c == '0':
            print('Done ordering!')
            print(cart)
            break
        elif c == '1':
            food()
        elif c == '2':
            drinks()
        else:
            print('Invalid option')

# if _name_ == '_main_':
you = who_are_u()
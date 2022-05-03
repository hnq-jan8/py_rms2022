from input import read_data, write_data, input_name_dish, clr_scr
from domains.Dish import Dish

class Dish_Manager:
    names = []  # List of used names

    def __init__(self):
        self.__dishes = []

    def __str__(self):
        for i in self.__dishes:
            print(i)

    def refresh_name(self):
        self.names = []
        for i in self.__dishes:
            self.names.append(i.get_name())

    def get_dishes(self):   # Return a list of dishes(objects)
        return self.__dishes

    def load_dishes(self):
        self.__dishes, self.names = read_data('dishes')

    def add_dish(self):
        clr_scr()
        print('''\n----- Admin / Dishes Manager ------\n
                \rAdding a dish''')
        name = input_name_dish(self.names)
        self.names.append(name)
        price = input('. Enter price: ').strip()
        while not price.isdigit() or int(price) < 1:
            price = input('''(!) Invalid price
                            \rTry again: ''').strip()
        price = int(price)
        self.__dishes.append(Dish(name, price))

    def edit_dish(self, dish):
        while True:
            clr_scr()
            print('\n---------- Admin / D_Manager / Edit -----------\n')
            print(f'''      Name\t\t\t   Price (VND)
                    \r  ->  {dish}\n
                    \r-----------------------------------------------\n
                    \r          1. Name     |     2. Price
                    \r\n0. <- Back''')
            choice = input('\nChoice (120): ').strip()
            if choice == '0':
                return
            elif choice == '1':
                self.names.remove(dish.get_name())
                name = input_name_dish(self.names)
                dish.set_name(name)
                self.names.append(name)
            elif choice == '2':
                price = input('. Enter price: ').strip()
                try:
                    while not price.isdigit() or int(price) < 1:
                        price = input('''(!) Invalid price
                                        \rTry again: ''').strip()
                    price = int(price)
                except ValueError:
                    print('(!) Invalid input')
                dish.set_price(price)

    def delete_dish(self, dish):
        confirm = input(f'''\n(!) '{dish.get_name()}' will be removed.
                        \rType 'y' to confirm: ''').strip()
        if confirm == 'y':
            self.names.remove(dish.get_name())
            self.__dishes.remove(dish)
            return 1
        else: return 0

    def select_dish(self, dish):
        while True:
            clr_scr()
            print(f'''\n----------- Admin / Dishes Manager ------------\n
                    \r      Name\t\t\t   Price (VND)
                    \r  ->  {dish}\n
                    \r-----------------------------------------------\n
                    \r          1. Edit     |     2. Delete
                    \r\n0. <- Back''')
            choice = input('\nChoice (120): ').strip()
            if choice == '0':
                return 0
            elif choice == '1':
                self.edit_dish(dish)
            elif choice == '2':
                d = self.delete_dish(dish)
                if d == 1:
                    return 0

    def list_dishes(self):
        # print(self.__dishes)
        if len(self.__dishes) == 0:
            print('(!) No dish')
        else:
            print('      Name\t\t\t   Price (VND)')
            for i, dish in enumerate(self.__dishes):
                print(f'{i+1:4}. {dish}')

    def start(self):
        self.refresh_name()    # Solve the problem of the name conflict
        while True:
            write_data('dishes', self.__dishes, self.names)
            clr_scr()
            print('\n----------- Admin / Dishes Manager ------------\n')
            self.list_dishes()
            print(f'''\n-----------------------------------------------
                    \r\na.                 | ADD |
                    \r\n0. <- Back''')
            if len(self.__dishes) == 0:
                choice = input('\nChoice (a, 0): ').strip().lower()
            else:
                choice = input(f'\nChoice (a, 1-{len(self.__dishes)}, 0): ').strip().lower()
            if choice == '0':
                return
            elif choice == 'a':
                self.add_dish()
            elif choice.isdigit() and int(choice) <= len(self.__dishes):
                self.select_dish(self.__dishes[int(choice)-1])

if __name__ == '__main__':
    dish_manager = Dish_Manager()
    dish_manager.start()
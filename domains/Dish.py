class Dish:
    def __init__(self, name, price):
            self.__name = name
            self.__price = price

    def __str__(self):
        return f'{self.__name:25} {self.__price:10}'

    def __repr__(self):
        return f'Dish({self.__name}, {self.__price})'

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def set_name(self, name):
        self.__name = name

    def set_price(self, price):
        self.__price = price
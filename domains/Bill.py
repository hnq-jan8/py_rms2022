import datetime

def total(cart, price_list):
    total = 0
    for i, dish in enumerate(cart):
        total += price_list[i] * cart[dish]
    return total

class Bill:
    def __init__(self, id, table_id, cart, prices):
        self.__id = id
        self.__table_id = table_id
        self.__cart = cart
        self.__prices = prices
        self.__date = datetime.datetime.now()
        self.__total_price = total(cart, prices)

    def get_id(self):
        return self.__id

    def get_table_id(self):
        return self.__table_id

    def get_cart(self):
        return self.__cart

    def get_prices(self):
        return self.__prices

    def get_date(self):
        return self.__date

    def __str__(self):
        return f'{self.__id:4}\t\t{self.__date:%d/%m/%Y}\t{self.__total_price:10}'

    def details(self):
        bill = f'''\n----------------- Bill -----------------\n
        \rTime: {self.__date:%H:%M:%S}         Date: {self.__date:%d/%m/%Y}
        \rTable: {self.__table_id}\t\t  Bill ID: {self.__id:4}\n\n'''
        for p, (d, q) in zip(self.__prices, self.__cart.items()):
            bill += f' . {d:25} {p} x {q}\n'       # print the cart including name, price and quantity

        bill += f'''\n\t*** Total: {self.__total_price} ***
                \n----------------------------------------'''
        print(bill)
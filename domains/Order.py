class Order:
    def __init__(self, table_id, cart):
        self.__table_id = table_id
        self.__cart = cart  # list of {dish_name: quantity}

    def get_table_id(self):
        return self.__table_id

    def get_cart(self):
        return self.__cart

    def set_cart(self, cart):
        self.__cart = cart
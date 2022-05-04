import pickle


# import Order


order_list = []
'''if load_from_file() == -1:
    self.__order_list = []
else:
    self.__order_list = orders'''


def fill_list():
    global order_list
    if load_from_file() == -1:
        order_list = []
    else:
        order_list = load_from_file()


def add_into_order_list(order):
    order_list.append(order)
    save_into_file()
    # self.__order_list.append(Order.Order(dish, time, o_id))
    # print(str(len(self.__order_list)))


def delete_from_order_list(o_id):
    for o in order_list:
        if o_id == o.get_id():
            order_list.remove(o)
            # print(str(len(self.__order_list)))
            save_into_file()


def get_order_list():
    return order_list


def save_into_file():
    with open("Bill", 'wb') as f:
        pickle.dump(order_list, f)


def load_from_file():
    import os
    if os.stat("Bill").st_size == 0:
        return -1
    else:
        with open("Bill", 'rb') as f:
            result = pickle.load(f)
            return result


def main():
    pass


if __name__ == "__main__":
    main()

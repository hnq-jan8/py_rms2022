from input import read_bill, clr_scr
from domains.Bill import Bill

class Bill_Manager:
    def __init__(self):
        self.__bills = []

    def add_bill(self, bill):
        self.__bills.append(bill)

    def get_bills(self):
        return self.__bills

    def load_bills(self):
        self.__bills = read_bill()

    def list_bills(self):
        if len(self.__bills) == 0:
            print('(!) No bill')
        else:
            print('     ID\t\tTime\t\t   Total (VND)')     # caption
            for i, bill in enumerate(self.__bills):
                print(f'{i + 1}. {bill}')

    # def clear_bills(self):        # clear all bills
    #     self.__bills = []         # only used for debugging

    def start(self):
        while True:
            # self.clear_bills()    # only used for debugging
            clr_scr()
            print('\n-------------- Admin / Bills ---------------\n')
            self.list_bills()
            print(f'\n--------------------------------------------\n')
            if len(self.__bills) == 0:
                print('0. <- Back')
                choice = input('\nChoice (0): ').strip()
            else:
                print(f'''Select a bill to view more details
                        \r\n0. <- Back''')
                choice = input(f'\nChoice (1-{len(self.__bills)}, 0): ').strip()
            if choice == '0':
                return
            elif choice.isdigit() and int(choice) <= len(self.__bills):
                clr_scr()
                print(f'''\n-------------- Admin / Bills ---------------\n
                        \r     ID\t\tTime\t\t   Total (VND)
                        \r-> {self.__bills[int(choice) - 1]}''')
                self.__bills[int(choice) - 1].details()
                input('\nPress Enter to continue...')
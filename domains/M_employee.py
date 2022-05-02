from input import read_data, write_data, input_name_employee, clr_scr
from domains.Employee import Employee

class Employee_Manager:
    ids = []    # List of used IDs

    roles = {'1': 'Manager', '2': 'Chef', '3': 'Waiter',
                '4': 'Receptionist', '5': 'Security Guard'}
    salaries = {'Manager': 7000000, 'Chef': 5000000, 'Waiter': 3000000,
                'Receptionist': 3000000, 'Security Guard': 3000000} 
    shifts = {'1': 'Morning', '2': 'Afternoon', '3': 'Evening'}

    def __init__(self):
        self.__employees = []

    def __str__(self):
        for i in self.__employees:
            print(i)

    def refresh_ids(self):  # Used for debugging
        self.ids = []
        for employee in self.__employees:
            self.ids.append(employee.get_id())

    def load_employees(self):
        self.__employees, self.ids = read_data('employees')

    def choose_role(self):
        role = input('''. Choose role:
                        \r      1. Manager    2. Chef     3. Waiter
                        \r      4. Receptionist   5. Security Guard
                        \r  Choice (12345): ''').strip()
        while role not in self.roles.keys():
            role = input('(!) Bad choice\n  Try again (12345): ').strip()
        return self.roles[role]          # Convert from key (12345) to its value

    def choose_shift(self):
        shift = input('''. Choose shift:
                        \r     1. Morning   2. Afternoon   3. Evening
                        \r  Choice (123): ''').strip()
        while shift not in self.shifts.keys():
            shift = input('(!) Bad choice\n  Try again (123): ').strip()
        return self.shifts[shift]       # Convert from key (123) to its value

    def add_employee(self):
        clr_scr()
        print('''\n---------------------------------- Admin / Employee Manager ----------------------------------\n
                \rAdding an employee''')
        fst, lst = input_name_employee()
        id = input('. Enter ID: ').strip()
        while id in self.ids:
            id = input('(!) This ID is already taken\n Try again: ').strip()
        self.ids.append(id)
        adr = input('. Enter address: ').strip()
        r = self.choose_role()
        salary = self.salaries[r]   # Get the salary of the role
        shift = self.choose_shift()
        self.__employees.append(Employee(fst, lst, id, adr, r, salary, shift))

    def edit_employee(self, employee):
        while True:
            clr_scr()
            print('\n---------------------------------- Admin / E_Manager / Edit ----------------------------------\n')
            print(f'''   Name\t\t\t     ID\t\t     Address\t     Role\t\t Salary  Shift
                    \r-> {employee}\n
                    \r----------------------------------------------------------------------------------------------\n
                    \r                      1. Name      |       2. ID       |       3. Address\n
                    \r                                 4. Role      |       5. Shift
                    \r\n0. <- Back''')
            choice = input('\nChoice (123450): ').strip()
            if choice == '0':
                return
            elif choice == '1':
                fst, lst = input_name_employee()
                employee.set_name(fst, lst)
            elif choice == '2':
                self.ids.remove(employee.get_id())
                id = input('. Enter ID: ').strip()
                while id in self.ids:
                    id = input('(!) This ID is already taken\n Try again: ').strip()
                employee.set_id(id)
                self.ids.append(id)
            elif choice == '3':
                adr = input('. Enter address: ').strip()
                employee.set_address(adr)
            elif choice == '4':
                r = self.choose_role()
                employee.set_role(r)
                employee.set_salary(self.salaries[r])
            elif choice == '5':
                shift = self.choose_shift()
                employee.set_shift(shift)

    def delete_employee(self, employee):
        confirm = input(f'''\n(!) '{employee.get_name()}' will be removed.
                        \rType 'y' to confirm: ''').strip()
        if confirm == 'y':
            self.ids.remove(employee.get_id())
            self.__employees.remove(employee)
            return 1
        else: return 0

    def select_employee(self, employee):
        while True:
            clr_scr()
            print(f'''\n---------------------------------- Admin / Employee Manager ----------------------------------\n
                    \r   Name\t\t\t     ID\t\t     Address\t     Role\t\t Salary  Shift
                    \r-> {employee}\n
                    \r----------------------------------------------------------------------------------------------\n
                    \r                                1. Edit       |       2. Delete
                    \r\n0. <- Back''')
            choice = input('\nChoice (120): ').strip()
            if choice == '0':
                return 0
            elif choice == '1':
                self.edit_employee(employee)
            elif choice == '2':
                d = self.delete_employee(employee)
                if d == 1:
                    return 0

    def list_employees(self):
        # print(self.__employees)
        if len(self.__employees) == 0:
            print('(!) No employee')
        else:
            print('   Name\t\t\t     ID\t\t     Address\t     Role\t\t Salary  Shift')
            for i, employee in enumerate(self.__employees):
                print(str(i+1) + '.', employee)

    def list_by_shift(self):
        shift = self.choose_shift()
        print()
        for employee in self.__employees:
            if employee.get_shift() == shift:
                print(employee)

    def start(self):
        self.refresh_ids()  # Refresh the list of IDs
        while True:
            write_data('employees', self.__employees, self.ids)
            clr_scr()
            print('\n---------------------------------- Admin / Employee Manager ----------------------------------\n')
            self.list_employees()
            print(f'''\n----------------------------------------------------------------------------------------------
                    \r\na.                                         | ADD |
                    \r\n0. <- Back''')
            if len(self.__employees) == 0:
                choice = input('\nChoice (a, 0): ').strip().lower()
            else:
                choice = input(f'\nChoice (a, 1-{len(self.__employees)}, 0): ').strip().lower()
            if choice == '0':
                return
            elif choice == 'a':
                self.add_employee()
            elif choice.isdigit() and int(choice) <= len(self.__employees):
                self.select_employee(self.__employees[int(choice)-1])

if __name__ == '__main__':
    e_manager = Employee_Manager()
    e_manager.start()
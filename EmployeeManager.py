from tkinter import *
import tkinter.ttk as ttk
import Admin


class Employee:
    def __init__(self):
        self.__employees = []

    def get_employees(self):
        return self.__employees

    def add_emp(self, e_id, name, dob, phone):
        new_emp = [e_id, name, dob, phone]
        self.__employees.append(new_emp)

        for d in self.__employees:
            print(d)

    def edit_emp(self, edited_id, edited_name, edited_dob, edited_phone, or_id, or_name, or_dob, or_phone):
        if edited_name == or_name and edited_id == or_id and edited_dob == or_dob and edited_phone == or_phone:
            return
        else:
            for i in range(len(self.__employees)):
                if self.__employees[i][0] == or_id:
                    self.__employees[i][0] = edited_id
                    self.__employees[i][1] = edited_name
                    self.__employees[i][2] = edited_dob
                    self.__employees[i][3] = edited_phone
                    break
        for d in self.__employees:
            print(d)

    def delete_emp(self, e_id):
        for d in self.__employees:
            if d[0] == e_id:
                self.__employees.remove(d)
                break

        for d in self.__employees:
            print(d)


def get_data_from_file():
    with open('Employees.txt', 'r') as rf:
        for line in rf:
            line_split = line.split(':')
            e_id = line_split[0]
            name = line_split[1]
            dob = line_split[2]
            phone = line_split[3]
            new_employee_mng.add_emp(e_id, name, dob, phone)


def show_data_from_file(table: ttk.Treeview):
    with open('Employees.txt', 'r') as rf:
        for line in rf:
            line_split = line.split(':')
            e_id = line_split[0]
            name = line_split[1]
            dob = line_split[2]
            phone = line_split[3]
            data = [e_id, name, dob, phone]
            table.insert('', END, values=data)


def edit_data_in_file(e_id, edited_id, edited_name, edited_dob, edited_phone):
    i = 0
    with open('Employees.txt', 'r') as rf:           # Open the file to find the line of the wanted dish name
        for num, line in enumerate(rf):
            if str(e_id) in line:
                i = num
                break
    print(i)
    with open('Employees.txt', 'r') as f:            # Open the file to get the whole string list
        string_list = f.readlines()
        print(string_list)

    with open('Employees.txt', 'w') as wf:           # Open the file to rewrite the edited string list
        string_list[i] = edited_id + ':' + edited_name + ':' + edited_dob + ':' + edited_phone + '\n'
        new_file_contents = ''.join(string_list)
        wf.write(new_file_contents)


def add_data_into_file(e_id, name, dob, phone):
    # Write new data into Menu.txt file
    with open('Employees.txt', 'a') as af:
        af.write(e_id + ':' + name + ':' + dob + ':' + phone + '\n')


def delete_data_from_file(e_id):
    i = 0
    with open('Employees.txt', 'r') as rf:  # Open the file to find the line of the wanted dish name
        for num, line in enumerate(rf):
            if str(e_id) in line:
                i = num
                break
    with open('Employees.txt', 'r') as f:  # Open the file to get the whole string list
        string_list = f.readlines()
        print(string_list)

    with open('Employees.txt', 'w') as wf:  # Open the file to rewrite the edited string list
        string_list[i] = ''
        new_file_contents = ''.join(string_list)
        wf.write(new_file_contents)


# ----------Create new employee_mng instance---------
new_employee_mng = Employee()
# --------------------------------------------


def submit_addition(e_id: Entry, name: Entry, dob: Entry, phone: Entry, p: Toplevel, table: ttk.Treeview):
    if e_id.get() == '' or name.get() == '' or dob.get() == '' or phone.get() == '':
        return
    for i in range(len(new_employee_mng.get_employees())):
        if e_id.get() == new_employee_mng.get_employees()[i][0]:
            return
    data = [e_id.get(), name.get(), dob.get(), phone.get()]
    table.insert('', END, values=data)

    new_employee_mng.add_emp(e_id.get(), name.get(), dob.get(), phone.get())

    add_data_into_file(e_id.get(), name.get(), dob.get(), phone.get())

    p.destroy()


def submit_edition(e_id: Entry, name: Entry, dob: Entry, phone: Entry, p: Toplevel, table: ttk.Treeview):
    selected_item = table.selection()[0]  # Get selected item

    cur_item = table.focus()
    or_id = table.item(cur_item)['values'][0]
    or_name = table.item(cur_item)['values'][1]
    or_dob = table.item(cur_item)['values'][2]
    or_phone = table.item(cur_item)['values'][3]
    edited_data = [e_id.get(), name.get(), dob.get(), phone.get()]
    edited_id = e_id.get()
    edited_name = name.get()
    edited_dob = dob.get()
    edited_phone = phone.get()

    new_employee_mng.edit_emp(edited_id, edited_name, edited_dob, edited_phone, or_id, or_name, or_dob, or_phone)

    edit_data_in_file(or_id, edited_id, edited_name, edited_dob, edited_phone)

    table.item(selected_item, text="blub", values=edited_data)
    p.destroy()


def add(win: Tk, table: ttk.Treeview):
    pop = Toplevel(win)
    pop.resizable(False, False)
    pop.title("Adding new employee")

    # Add emp ID
    add_id_text = Label(pop, text='ID:', font=("Arial", 15))
    add_id_text.grid(column=0, row=0, padx=10, pady=10, sticky=W)

    id_entry = Entry(pop, font=("Arial", 15))
    id_entry.grid(column=1, row=0, padx=10)

    # Add emp name
    add_text = Label(pop, text='Name:', font=("Arial", 15))
    add_text.grid(column=0, row=1, padx=10, pady=10, sticky=W)

    name_entry = Entry(pop, font=("Arial", 15))
    name_entry.grid(column=1, row=1, padx=10)

    # Add emp dob
    add_dob_text = Label(pop, text='DOB:', font=("Arial", 15))
    add_dob_text.grid(column=0, row=2, padx=10, pady=10, sticky=W)

    dob_entry = Entry(pop, font=("Arial", 15))
    dob_entry.grid(column=1, row=2, padx=10)

    # Add emp phone
    add_phone_text = Label(pop, text='Phone:', font=("Arial", 15))
    add_phone_text.grid(column=0, row=3, padx=10, pady=10, sticky=W)

    phone_entry = Entry(pop, font=("Arial", 15))
    phone_entry.grid(column=1, row=3, padx=10)

    # Submit addition
    submit_add = Button(pop, text='Enter', command=lambda: submit_addition(id_entry, name_entry, dob_entry, phone_entry, pop, table))
    submit_add.grid(columnspan=2, column=0, row=4, padx=10, pady=10)


def edit(win: Tk, table: ttk.Treeview):
    if len(table.selection()) == 0:
        err = Toplevel(win)
        err.title("ERROR")
        message = Label(err, text="You did not select the dish to edit!", font=("Arial", 50))
        message.pack()
        return

    pop = Toplevel(win)
    pop.resizable(False, False)
    pop.title("Edit employees")

    # Edit emp ID
    edit_id_text = Label(pop, text='ID:', font=("Arial", 15))
    edit_id_text.grid(column=0, row=0, padx=10, pady=10, sticky=W)

    id_entry = Entry(pop, font=("Arial", 15))
    id_entry.grid(column=1, row=0, padx=10)

    # Add emp name
    edit_text = Label(pop, text='Name:', font=("Arial", 15))
    edit_text.grid(column=0, row=1, padx=10, pady=10, sticky=W)

    name_entry = Entry(pop, font=("Arial", 15))
    name_entry.grid(column=1, row=1, padx=10)

    # Add emp dob
    edit_dob_text = Label(pop, text='DOB:', font=("Arial", 15))
    edit_dob_text.grid(column=0, row=2, padx=10, pady=10, sticky=W)

    dob_entry = Entry(pop, font=("Arial", 15))
    dob_entry.grid(column=1, row=2, padx=10)

    # Edit emp phone
    edit_phone_text = Label(pop, text='Phone:', font=("Arial", 15))
    edit_phone_text.grid(column=0, row=3, padx=10, pady=10, sticky=W)

    phone_entry = Entry(pop, font=("Arial", 15))
    phone_entry.grid(column=1, row=3, padx=10)

    # Submit addition
    submit_edit = Button(pop, text='Enter', command=lambda: submit_edition(id_entry, name_entry, dob_entry, phone_entry, pop, table))
    submit_edit.grid(columnspan=2, column=0, row=4, padx=10, pady=10)


def delete(win: Tk, table: ttk.Treeview):
    if len(table.selection()) == 0:
        err = Toplevel(win)
        err.title("ERROR")
        message = Label(err, text="You did not select the dish to delete!", font=("Arial", 50))
        message.pack()
        return

    cur_item = table.focus()
    e_id = table.item(cur_item)['values'][0]

    new_employee_mng.delete_emp(e_id)

    delete_data_from_file(e_id)

    selected_item = table.selection()[0]  # Get selected item
    table.delete(selected_item)


def main():
    win = Tk()
    win.title("Employee manager")
    win.resizable(False, False)

    # Manager options
    fr = Frame(win)
    fr.grid(rowspan=2, column=0, row=0)
    mng_menu_label = Label(fr, text='Manager menu', font=("Arial Bold", 10))
    mng_menu_label.pack(pady=10)
    bill_mng_butt = Button(fr, text="Bill", font=("Arial", 10), width=10, command=lambda: Admin.open_bill_mng(win))
    bill_mng_butt.pack(padx=5, pady=30)
    employee_mng_butt = Button(fr, text="Menu", font=("Arial", 10), width=10, command=lambda: Admin.open_menu_mng(win))
    employee_mng_butt.pack(padx=5, pady=30)

    # Treeview(table)
    columns = ('id', 'name', 'dob', 'phone')
    table = ttk.Treeview(win, columns=columns, show='headings')
    table.heading('id', text="ID")
    table.heading('name', text="Name")
    table.heading('dob', text="Date of birth")
    table.heading('phone', text="Phone number")
    table.grid(columnspan=3, column=1, row=0, padx=5, pady=5)

    add_butt = Button(win, text="Add", padx=50, pady=20, command=lambda: add(win, table))
    add_butt.grid(column=1, row=1, padx=10, pady=20)

    edit_butt = Button(win, text="Edit", padx=50, pady=20, command=lambda: edit(win, table))
    edit_butt.grid(column=2, row=1, padx=10, pady=20)

    del_butt = Button(win, text="Delete", padx=50, pady=20, command=lambda: delete(win, table))
    del_butt.grid(column=3, row=1, padx=10, pady=20)

    win.after(100, get_data_from_file)
    win.after(200, show_data_from_file(table))
    win.mainloop()


if __name__ == "__main__":
    main()

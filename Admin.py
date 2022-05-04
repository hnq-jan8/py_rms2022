from tkinter import *


def open_menu_mng(w: Tk):
    w.destroy()
    import MenuManager
    MenuManager.main()


def open_employee_mng(w: Tk):
    w.destroy()
    import EmployeeManager
    EmployeeManager.main()


def open_bill_mng(w: Tk):
    w.destroy()
    import BillManager
    BillManager.main()


def main():
    win = Tk()
    win.resizable(False, False)
    win.title("ADMINISTRATOR")

    label = Label(win, text="MANAGER", font=("Arial Bold", 15))
    label.pack(padx=10, pady=10)

    bill_mng_butt = Button(win, text="Bill manager", font=("Arial Bold", 10), padx=100, pady=10,
                           command=lambda: open_bill_mng(win))
    bill_mng_butt.pack(padx=10, pady=10)

    menu_mng_butt = Button(win, text="Menu manager", font=("Arial Bold", 10), padx=95, pady=10,
                           command=lambda: open_menu_mng(win))
    menu_mng_butt.pack(padx=10, pady=10)

    employee_mng_butt = Button(win, text="Employee manager", font=("Arial Bold", 10), padx=80, pady=10,
                               command=lambda: open_employee_mng(win))
    employee_mng_butt.pack(padx=10, pady=10)

    win.mainloop()


if __name__ == "__main__":
    main()

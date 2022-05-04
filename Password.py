from tkinter import *
import tkinter.ttk as ttk


pass_word_list = ["st21", "ad21"]


def open_order_window(w: Tk):
    w.destroy()
    import Order_tables
    Order_tables.main()


def open_admin_window(w: Tk):
    w.destroy()
    import Admin
    Admin.main()


# login validation
def login_validate(password, w: Tk):
    if password == "st21":
        open_order_window(w)
        # Open order window
        pass
    elif password == "ad21":
        # Open admin window
        open_admin_window(w)
        pass
    else:
        print("Wrong password")


def exit_program(w: Tk):
    w.destroy()


win = Tk()
win.title('WELCOME')
win.resizable(False, False)

label = Label(win, text="Password ", font=("Arial Bold", 20))
label.grid(column=0, row=0, padx=10, pady=10)

pass_label = Label(win, text="Enter the password: ", font=("Arial Bold", 12))
pass_label.grid(column=0, row=1)

pass_entry = Entry(win, width=30, show="*")
pass_entry.grid(column=0, row=2, padx=5, pady=5)

login_button = Button(win, text="Login", font=("Arial Bold", 10), command=lambda: login_validate(pass_entry.get(), win), padx=20, pady=10)
login_button.grid(column=0, row=3, pady=5)

exit_button = Button(win, text="Exit", command=lambda: exit_program(win))
exit_button.grid(column=0, row=4, pady=5)


win.mainloop()









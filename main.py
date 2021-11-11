from tkinter import *

win = Tk()
win.geometry()


def button_add(number):
    global expression
    expression = expression + str(number)
    input_text.set(expression)


def button_clear():
    global expression
    expression = ""
    input_text.set("")


def button_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression = ""


expression = ""

input_text = StringVar()

w = Entry(win, textvariable=input_text, width=35, borderwidth=5).grid(row=0, column=0, columnspan=4, padx=10, pady=10)

Button(win, text="0", padx=40, pady=20, command=lambda: button_add(0)).grid(row=1, column=0)
Button(win, text="C", padx=39, pady=20, command=lambda: button_clear()).grid(row=1, column=1)
Button(win, text="=", padx=39, pady=20, command=lambda: button_equal()).grid(row=1, column=2)
Button(win, text="/", padx=39, pady=20, command=lambda: button_add("/")).grid(row=1, column=3)

Button(win, text="1", padx=40, pady=20, command=lambda: button_add(1)).grid(row=2, column=0)
Button(win, text="2", padx=40, pady=20, command=lambda: button_add(2)).grid(row=2, column=1)
Button(win, text="3", padx=40, pady=20, command=lambda: button_add(3)).grid(row=2, column=2)
Button(win, text="+", padx=38, pady=20, command=lambda: button_add("+")).grid(row=2, column=3)

Button(win, text="4", padx=40, pady=20, command=lambda: button_add(4)).grid(row=3, column=0)
Button(win, text="5", padx=40, pady=20, command=lambda: button_add(5)).grid(row=3, column=1)
Button(win, text="6", padx=40, pady=20, command=lambda: button_add(6)).grid(row=3, column=2)
Button(win, text="-", padx=39, pady=20, command=lambda: button_add("-")).grid(row=3, column=3)

Button(win, text="7", padx=40, pady=20, command=lambda: button_add(7)).grid(row=4, column=0)
Button(win, text="8", padx=40, pady=20, command=lambda: button_add(8)).grid(row=4, column=1)
Button(win, text="9", padx=40, pady=20, command=lambda: button_add(9)).grid(row=4, column=2)
Button(win, text="*", padx=39, pady=20, command=lambda: button_add("*")).grid(row=4, column=3)

win.mainloop()

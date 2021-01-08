from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from math import *

root = Tk()

check = False

# Functions
def sqrt_button() :
    global check
    if not check:
        insert("sqrt(0)")
    else :
        insert("cube_sqrt(0)")
        check = False


def cube_sqrt(num) :
    return num ** (1/3)

# the shift button function
def checking():
    global check
    if not check:
        check = True
    else :
        check = False

# main entry for the calculator
entry = ttk.Entry(root, font = ("Arial", 12))
entry.grid(row = 0, column = 0, columnspan = 8, ipadx = 150, ipady = 20, pady = 2, sticky = "wens")

button_shift = ttk.Button(root, text = "shift", command = lambda:checking())
button_shift.grid(row = 1, column = 4, ipady = 0, ipadx = 0)


# buttons
# row 0
button1 = ttk.Button(root, text='1', command = lambda:insert("1"))
button1.grid(row = 1, column = 0, ipadx = 8, ipady = 8)

button2 = ttk.Button(root, text='2', command = lambda:insert("2"))
button2.grid(row = 1, column = 1, ipadx = 8, ipady = 8)

button3 = ttk.Button(root, text='3', command = lambda:insert("3"))
button3.grid(row = 1, column = 2, ipadx = 8, ipady = 8)

# the first row
button4 = ttk.Button(root, text='4', command = lambda:insert("4"))
button4.grid(row = 2, column = 0, ipadx = 8, ipady = 8)

button5 = ttk.Button(root, text='5', command = lambda:insert("5"))
button5.grid(row = 2, column = 1, ipadx = 8, ipady = 8)

button6 = ttk.Button(root, text='6', command = lambda:insert("6"))
button6.grid(row = 2, column = 2, ipadx = 8, ipady = 8)

# the second row
button7 = ttk.Button(root, text='7', command = lambda:insert("7"))
button7.grid(row = 3, column = 0, ipadx = 8, ipady = 8)

button8 = ttk.Button(root, text='8', command = lambda:insert("8"))
button8.grid(row = 3, column = 1, ipadx = 8, ipady = 8)

button9 = ttk.Button(root, text='9', command = lambda:insert("9"))
button9.grid(row = 3, column = 2, ipadx = 8, ipady = 8)

# the third row
button_plus = ttk.Button(root, text='+', command = lambda:insert("+"))
button_plus.grid(row = 4, column = 0, ipadx = 8, ipady = 8)

button0 = ttk.Button(root, text='0', command = lambda:insert("0"))
button0.grid(row = 4, column = 1, ipadx = 8, ipady = 8)

button_minus = ttk.Button(root, text='-', command = lambda:insert("-"))
button_minus.grid(row = 4, column = 2, ipadx = 8, ipady = 8)

# the fourth row
button_times = ttk.Button(root, text='*', command = lambda:insert("*"))
button_times.grid(row = 5, column = 0, ipady = 8, ipadx = 8)

button_point = ttk.Button(root, text='.', command = lambda:insert("."))
button_point.grid(row = 5, column = 1, ipadx = 8, ipady = 8)

button_divide = ttk.Button(root, text='/', command = lambda:insert("/"))
button_divide.grid(row = 5, column = 2, ipady = 8, ipadx = 8)

# the fifth row
button_sqrt = ttk.Button(root, text = "√ / 3√", command = lambda:sqrt_button())
button_sqrt.grid(row = 6, column = 0, ipady = 8, ipadx = 8)

button_result = ttk.Button(root, text = "=", command = lambda:calculate())
button_result.grid(row = 6, column = 1, ipady = 8, ipadx = 8)

button_power = ttk.Button(root, text = "power", command = lambda:insert("**"))
button_power.grid(row = 6, column = 2, ipady = 8, ipadx = 8)

# the sixth row
button_leftRoundBracket = ttk.Button(root, text = "(", command = lambda:insert("("))
button_leftRoundBracket.grid(row = 7, column = 0, ipady = 8, ipadx = 8)

button_rightRoundBracket = ttk.Button(root, text = ")", command = lambda:insert(")"))
button_rightRoundBracket.grid(row = 7, column = 1, ipady = 8, ipadx = 8)

button_delete = ttk.Button(root, text = "CE", command = lambda:entry.delete(len(entry.get()) - 1))
button_delete.grid(row = 7, column = 2, ipady = 8, ipadx = 8)

# the seventh row
button_leftBoxBracket = ttk.Button(root, text = "[", command = lambda:insert("["))
button_leftBoxBracket.grid(row = 8, column = 0, ipady = 8, ipadx = 8)

button_rightBoxBracket = ttk.Button(root, text = "]", command = lambda:insert("]"))
button_rightBoxBracket.grid(row = 8, column = 1, ipady = 8, ipadx = 8)

button_clear = ttk.Button(root, text = "C", command = lambda:entry.delete(0, END))
button_clear.grid(row = 8, column = 2, ipady = 8, ipadx = 8)

# the eighth row
button_leftCurlyBracket = ttk.Button(root, text = "{", command = lambda:insert("{"))
button_leftCurlyBracket.grid(row = 9, column = 0, ipady = 8, ipadx = 8)

button_rightCurlyBracket = ttk.Button(root, text = "}", command = lambda:insert("}"))
button_rightCurlyBracket.grid(row = 9, column = 1, ipady = 8, ipadx = 8)

button_abs = ttk.Button(root, text = "abs", command = lambda:insert("abs()"))
button_abs.grid(row = 9, column = 2, ipady = 8, ipadx = 8)

# the ninth row
button_comma = ttk.Button(root, text = ",", command = lambda:insert(","))
button_comma.grid(row = 10, column = 0, ipady = 8, ipadx = 8)


def calculate():
    ans = str(eval(entry.get()))
    messagebox.showinfo(message = ans)
    entry.delete(0, END)


def insert(text) :
    entry.insert(END, text)


root.mainloop()

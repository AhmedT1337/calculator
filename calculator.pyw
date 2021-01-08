from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from math import *

root = Tk()

check = False
π = pi

def sqrt_button() :
    global check
    if not check:
        insert("sqrt(")
    else :
        insert("cube_sqrt(")
        check = False


def cube_sqrt(num) :
    return num ** (1/3)


def checking():
    global check 
    if not check:
        check = True
    else :
        check = False

entry = ttk.Entry(root, font = ("Arial", 12))
entry.grid(row = 0, column = 0, columnspan = 8, ipadx = 70, ipady = 20, padx = 15, pady = 15)

button_shift = ttk.Button(root, text = "shift", command = lambda:checking())
button_shift.grid(row = 1, column = 4, ipady = 0, ipadx = 0)

######################################################################################

buttons_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, "+", 0, "-", "*", ".", "/"]

rows = 1
columns = 0

for i in buttons_list :
    if i == "+" : name = "plus"
    elif i == "-" : name = "minus"
    elif i == "*" : name = "times"
    elif i == "." : name = "point"
    elif i == "/" : name = "divide"
    else : name = i
        
    exec(f"button_{name} = ttk.Button(root, text = '{i}', command = lambda:insert('{i}'))")
    exec(f"button_{name}.grid(row = rows, column = columns, ipadx = 8, ipady = 8)")
    columns += 1
    
    if columns == 3 :
        rows += 1
        columns = 0

######################################################################################

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

button_abs = ttk.Button(root, text = "abs", command = lambda:insert("abs("))
button_abs.grid(row = 9, column = 2, ipady = 8, ipadx = 8)

# the ninth row
button_comma = ttk.Button(root, text = ",", command = lambda:insert(","))
button_comma.grid(row = 10, column = 0, ipady = 8, ipadx = 8)

button_π = ttk.Button(root, text = "π", command = lambda:insert("π"))
button_π.grid(row = 10, column = 1, ipady = 8, ipadx = 8)

def calculate():
    ans = str(eval(entry.get()))
    messagebox.showinfo(message = ans)
    entry.delete(0, END)


def insert(text) :
    entry.insert(END, text)

root.mainloop()
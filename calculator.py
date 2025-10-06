from tkinter import *

# Functions and variables
equation_text = ""

def button_pressing(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def clear_screen():
    global equation_text
    equation_label.set("")
    equation_text = ""

def equals():
    global equation_text
    try:
        total = str(eval(equation_text))  # WARNING: eval() is insecure—locked for learning only
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""

# Window config
window = Tk()
window.title("calculator")
window.geometry("350x400")
window.config(bd=5, relief="groove")

# Label
equation_label = StringVar()
label = Label(window, textvariable=equation_label, bg="gray", height=2, bd=3, relief="ridge")
label.pack(side="top", fill="both", expand=True)

# Frame
frame = Frame(window)
frame.pack(fill="both", expand=True)

for i in range(4):
    frame.grid_columnconfigure(i, weight=1)
for j in range(5):
    frame.grid_rowconfigure(j, weight=1)

# Buttons
button1 = Button(frame, text="1", font=("Arial", 16), bg="#76D36D", border=2, relief="groove", width=4, height=3, command=lambda: button_pressing(1))
button1.grid(column=0, row=0, sticky="nsew")

button2 = Button(frame, text="2", font=("Arial", 16), bg="#76D36D", border=2, relief="groove", width=4, height=3, command=lambda: button_pressing(2))
button2.grid(column=1, row=0, sticky="nsew")

button3 = Button(frame, text="3", font=("Arial", 16), bg="#76D36D", border=2, relief="groove", width=4, height=3, command=lambda: button_pressing(3))
button3.grid(column=2, row=0, sticky="nsew")

button4 = Button(frame, text="4", font=("Arial", 16), bg="#76D36D", border=2, relief="groove", width=4, height=3, command=lambda: button_pressing(4))
button4.grid(column=0, row=1, sticky="nsew")

button5 = Button(frame, text="5", font=("Arial", 16), bg="#76D36D", border=2, relief="groove", width=4, height=3, command=lambda: button_pressing(5))
button5.grid(column=1, row=1, sticky="nsew")

button6 = Button(frame, text="6", font=("Arial", 16), bg="#76D36D", border=2, relief="groove", width=4, height=3, command=lambda: button_pressing(6))
button6.grid(column=2, row=1, sticky="nsew")

button7 = Button(frame, text="7", font=("Arial", 16), bg="#76D36D", border=2, relief="groove", width=4, height=3, command=lambda: button_pressing(7))
button7.grid(column=0, row=2, sticky="nsew")

button8 = Button(frame, text="8", font=("Arial", 16), bg="#76D36D", border=2, relief="groove", width=4, height=3, command=lambda: button_pressing(8))
button8.grid(column=1, row=2, sticky="nsew")

button9 = Button(frame, text="9", font=("Arial", 16), bg="#76D36D", border=2, relief="groove", width=4, height=3, command=lambda: button_pressing(9))
button9.grid(column=2, row=2, sticky="nsew")

button0 = Button(frame, text="0", height=4, font=("Arial", 16), bg="#76D36D", border=2, relief="groove", width=3, command=lambda: button_pressing(0))
button0.grid(row=3, column=0, sticky="nsew")

plus = Button(frame, text='+', height=4, font=("Arial", 16), bg="#EF8666", border=2, relief="groove", width=3, command=lambda: button_pressing('+'))
plus.grid(row=0, column=3, sticky="nsew")

minus = Button(frame, text='-', height=4, font=("Arial", 16), bg="#EF8666", border=2, relief="groove", width=3, command=lambda: button_pressing('-'))
minus.grid(row=1, column=3, sticky="nsew")

multiply = Button(frame, text='×', height=4, font=("Arial", 16), bg="#EF8666", border=2, relief="groove", width=3, command=lambda: button_pressing('*'))
multiply.grid(row=2, column=3, sticky="nsew")

divide = Button(frame, text='÷', height=4, font=("Arial", 16), bg="#EF8666", border=2, relief="groove", width=3, command=lambda: button_pressing('/'))
divide.grid(row=3, column=3, sticky="nsew")

equal = Button(frame, text='=', height=4, font=("Arial", 16), bg="#7DCDDD", border=2, relief="groove", width=3, command=equals)
equal.grid(row=3, column=2, sticky="nsew")

decimal = Button(frame, text='.', height=4, font=("Arial", 16), bg="#E6E263", border=2, relief="groove", width=3, command=lambda: button_pressing('.'))
decimal.grid(row=3, column=1, sticky="nsew")

clear_screen = Button(frame, text='clear', height=4, font=("Arial", 16), bg="#E8DCC6", border=2, relief="groove", width=12, command=clear)
clear_screen.grid(row=4, column=0, columnspan=4, sticky="nsew")

window.mainloop()
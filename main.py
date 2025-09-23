from tkinter import *



#functions and variabes

equation_text = ""


def button_pressing(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)






# window config

window = Tk()

window.title("calculator")

window.geometry("400x400")

window.config(bg="black")



#label
equation_label = StringVar()

label = Label(window, textvariable= equation_label, bg="gray", width=35, height=2)

label.pack()



window.mainloop()
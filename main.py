from tkinter import *



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
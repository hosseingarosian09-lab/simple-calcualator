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


#frame
frame = Frame(window)
frame.pack()

  
  

#buttons

button1 = Button(frame,text="1",width=4,height=3,command= lambda:button_pressing(1))
button1.grid(column=0,row=0)

  
button2 = Button(frame,text="2",width=4,height=3,command= lambda:button_pressing(2))
button2.grid(column=1,row=0)

  
button3 = Button(frame,text="3",width=4,height=3,command= lambda:button_pressing(3))
button3.grid(column=2,row=0)

  
button4 = Button(frame,text="4",width=4,height=3,command= lambda:button_pressing(4))
button4.grid(column=0,row=1)

  
button5 = Button(frame,text="5",width=4,height=3,command= lambda:button_pressing(5))
button5.grid(column=1,row=1)

  
button6 = Button(frame,text="6",width=4,height=3,command= lambda:button_pressing(6))
button6.grid(column=2,row=1)


button7 = Button(frame,text="7",width=4,height=3,command= lambda:button_pressing(7))
button7.grid(column=0,row=2)

  
button8 = Button(frame,text="8",width=4,height=3,command= lambda:button_pressing(8))
button8.grid(column=1,row=2)

  
button9 = Button(frame,text="9",width=4,height=3,command= lambda:button_pressing(9))
button9.grid(column=2,row=2)




button0 = Button(frame, text=0, height=4, width=3,command=lambda: button_pressing(0))
button0.grid(row=3, column=0)


plus = Button(frame, text='+', height=4, width=3,command=lambda: button_pressing('+'))
plus.grid(row=0, column=3)


minus = Button(frame, text='-', height=4, width=3,command=lambda: button_pressing('-'))
minus.grid(row=1, column=3)

  
multiply = Button(frame, text='*', height=4, width=3,command=lambda: button_pressing('*'))
multiply.grid(row=2, column=3)

  
divide = Button(frame, text='/', height=4, width=3,command=lambda: button_pressing('/'))
divide.grid(row=3, column=3)


equal = Button(frame, text='=', height=4, width=3,command=equals)
equal.grid(row=3, column=2)


decimal = Button(frame, text='.', height=4, width=3,command=lambda: button_pressing('.'))
decimal.grid(row=3, column=1)

  

clear = Button(window, text='clear', height=4, width=12,command=clear)
clear.pack()


window.mainloop()
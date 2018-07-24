# Problem 2

from tkinter import *

class Calculator:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.result = StringVar()
        self.equation = StringVar()
        self.result.set('0.0')
        self.equation.set('')
        Label(frame,
              textvariable=self.result,
              justify=RIGHT,
              anchor=E,
              background='white').grid(row=0, columnspan = 4, sticky=N+S+E+W)
        button_clr = Button(frame, text='C', command=self.clear)
        button_clr.grid(row=1, column=0, sticky=N+S+E+W)
        button_div = Button(frame, text='/', command= lambda: self.add('/'))
        button_div.grid(row=1, column=1, sticky=N+S+E+W)
        button_mul = Button(frame, text='*', command= lambda: self.add('*'))
        button_mul.grid(row=1, column=2, sticky=N+S+E+W)
        button_sub = Button(frame, text='-', command= lambda: self.add('-'))
        button_sub.grid(row=1, column=3, sticky=N+S+E+W)
        button_add = Button(frame, text='+', command= lambda: self.add('+'))
        button_add.grid(row=2, column=3, rowspan=2, sticky=N+S+E+W)
        button_dot = Button(frame, text='.', command= lambda: self.add('.'))
        button_dot.grid(row=5, column=2, sticky=N+S+E+W)
        button_eqs = Button(frame, text='=', command=self.evaluate)
        button_eqs.grid(row=4, column=3, rowspan=2, sticky=N+S+E+W)
        button_9 = Button(frame, text='9', command= lambda: self.add('9'))
        button_9.grid(row=2, column=2, sticky=N+S+E+W)
        button_8 = Button(frame, text='8', command= lambda: self.add('8'))
        button_8.grid(row=2, column=1, sticky=N+S+E+W)
        button_7 = Button(frame, text='7', command= lambda: self.add('7'))
        button_7.grid(row=2, column=0, sticky=N+S+E+W)
        button_6 = Button(frame, text='6', command= lambda: self.add('6'))
        button_6.grid(row=3, column=2, sticky=N+S+E+W)
        button_5 = Button(frame, text='5', command= lambda: self.add('5'))
        button_5.grid(row=3, column=1, sticky=N+S+E+W)
        button_4 = Button(frame, text='4', command= lambda: self.add('4'))
        button_4.grid(row=3, column=0, sticky=N+S+E+W)
        button_3 = Button(frame, text='3', command= lambda: self.add('3'))
        button_3.grid(row=4, column=2, sticky=N+S+E+W)
        button_2 = Button(frame, text='2', command= lambda: self.add('2'))
        button_2.grid(row=4, column=1, sticky=N+S+E+W)
        button_1 = Button(frame, text='1', command= lambda: self.add('1'))
        button_1.grid(row=4, column=0, sticky=N+S+E+W)
        button_0 = Button(frame, text='0', command= lambda: self.add('0'))
        button_0.grid(row=5, column=0, columnspan=2, sticky=N+S+E+W)

    def clear(self):
        self.result.set('0.0')
        self.equation.set('')

    def evaluate(self):
        equation = self.equation.get()
        if equation == '':
            return
        try:
            self.result.set(str(float(eval(equation))))
            self.equation.set(str(float(eval(equation))))
        except:
            self.result.set('Invalid Equation')
            self.equation.set('')
            
    def add(self,value):
        current = self.equation.get()
        current = current + value
        self.equation.set(current)
        self.result.set(current)

root = Tk()
root.geometry("150x160")
root.resizable(0, 0)
app = Calculator(root)
root.mainloop()

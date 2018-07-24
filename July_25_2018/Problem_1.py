# Problem 1

import sys, os
from tkinter import *

sys.path.append('/home/pi/Documents/Pithon_Directories/Pithon_JohnD')
from July_18_2018.Problem_1_2 import fastaCount
from tkinter.filedialog import askopenfilename

class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='Fasta file').grid(row=0, column=0)
        self.input_file = StringVar()
        self.input_name = StringVar()
        Label(frame, textvariable=self.input_name).grid(row=0, column=1)
        Label(frame, text='Number of fasta records').grid(row=1, column=0)
        self.count = IntVar()
        Label(frame, textvariable=self.count).grid(row=1, column=1)
        button_1 = Button(frame, text='File', command=self.select)
        button_1.grid(row=2, column=0)
        button_2 = Button(frame, text='Count', command=self.counter)
        button_2.grid(row=2, column=1)

    def select(self):
        name = askopenfilename()
        self.input_name.set(os.path.split(name)[1])
        self.input_file.set(name)

    def counter(self):
        file = self.input_file.get()
        self.count.set(fastaCount(file))


root = Tk()
root.wm_title('Fasta Sequence Counter')
root.geometry("350x75")
root.resizable(0, 0)
app = App(root)
root.mainloop()

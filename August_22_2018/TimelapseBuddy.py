# Take picture at specific intervals

from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import ImageTk, Image
from picamera import PiCamera
from time import sleep
import datetime, os

camera = PiCamera()
splits = ['Seconds', 'Minutes', 'Hours', 'Days']

class Camera:
        def __init__(self, master):
            frame = Frame(master)
            frame.pack()
            self.directory = StringVar()
            self.directorypath = StringVar()
            button_1 = Button(frame, text='Directory', command=self.select)
            button_1.grid(row = 0,
                          column = 0,
                          sticky=W+E)
            self.directory = StringVar()
            self.directorypath = StringVar()
            Label(frame,
                  textvariable = self.directory,
                  background='white').grid(row = 0,
                                           column = 1,
                                           columnspan = 3,
                                           sticky=W+E)
            
            camera.capture('preview.jpg')
            self.image = ImageTk.PhotoImage(Image.open('preview.jpg').resize((250, 250), Image.ANTIALIAS))
            Label(frame, image = self.image). grid(row = 0,
                                                   column = 4,
                                                   columnspan = 4,
                                                   rowspan = 8,
                                                   sticky=N+S+E+W)
            
            Label(frame, text='Duration:').grid(row = 1,
                                                column = 0)
            
            self.duration = IntVar()
            self.duration.set(2)
            Entry(frame,
                  textvariable = self.duration,
                  justify=RIGHT,
                  background='white').grid(row = 1,
                                          column = 1,
                                          columnspan = 3,
                                          sticky=W+E)
            self.durationtype = IntVar()
            self.durationtype.set(1)
            for val, time in enumerate(splits):
                Radiobutton(frame,
                            text = time,
                            command = self.durationselect,
                            value = val,
                            variable = self.durationtype).grid(row = 2,
                                                               column = val)
                
            Label(frame, text='Lapse:').grid(row = 3,
                                                column = 0)
            self.lapse = IntVar()
            self.lapse.set(0)
            Entry(frame,
                  textvariable = self.lapse,
                  justify=RIGHT,
                  background='white').grid(row = 3,
                                           column = 1,
                                           columnspan = 3,
                                           sticky=W+E)
            self.lapsetype = IntVar()
            self.lapsetype.set(1)
            for val, time in enumerate(splits):
                Radiobutton(frame,
                            text = time,
                            command = self.lapseselect,
                            value = val,
                            variable = self.lapsetype).grid(row = 4,
                                                               column = val)

            button_2 = Button(frame, text='Start', command=self.start)
            button_2.grid(row = 5,
                          column = 1,
                          columnspan = 2)


            self.taken = IntVar()
            self.taken.set('0')
            Label(frame, text='Pictures taken:').grid(row = 6,
                                                      column = 0)
            Label(frame, textvariable=self.taken).grid(row = 6,
                                                       column = 2,
                                                       columnspan = 2,
                                                       sticky = W+E)

        
        def capture(self):
            now = datetime.datetime.now()
            now = '_'.join([str(now.year),str(now.month),str(now.day),
                           str(now.hour),str(now.minute),str(now.second)])
            path = self.directorypath.get()
            if path == '':
                name = now + '.jpg'
                camera.capture(name)
            else:
                name = self.directorypath.get() + '/' + now + '.jpg'
                camera.capture(name)
            
        def durationselect(self):
            pass
        
        def lapseselect(self):
            pass

        def start(self):
            self.taken.set(0)
            duration = self.duration.get()
            dtype = self.durationtype.get()
            lapse = self.lapse.get()
            ltype = self.lapsetype.get()
            if dtype == 1:
                    duration = duration * 60
            elif dtype == 2:
                    duration = duration * 60 * 60
            elif dtype == 3:
                    duration = duration * 60 * 60 * 24
            if ltype == 1:
                    lapse = lapse * 60
            elif ltype == 2:
                    lapse = lapse * 60 * 60
            elif ltype == 3:
                    lapse = lapse * 60 * 60 * 24
            timer = 0
            while timer < duration:
                self.capture()
                self.taken.set(self.taken.get() + 1)
                sleep(lapse)
                timer += lapse

        def select(self):
            name = askdirectory()
            self.directory.set(os.path.split(name)[1])
            self.directorypath.set(name)


root = Tk()
root.wm_title('Timelapse Buddy')
root.geometry('550x250')
root.resizable(0,0)
app = Camera(root)
root.mainloop()

#img = Image.open('/home/pi/Desktop/pic.jpg')
#img.show()


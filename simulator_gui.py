import tkinter
import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#define method to quit
def quit(event=None):
    root.destroy()


#create object rep of GUI
root = tkinter.Tk()


exit_but = tkinter.Button(text='Exit', command=quit)
exit_but.pack(side='bottom',fill='both')

greeting = tkinter.Label(text='Welcome to Are You The One!')
greeting.pack()



#run the GUI
root.mainloop()

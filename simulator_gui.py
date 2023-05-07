import tkinter as tk
import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from are_you_the_one import Contestant, Simulation
from histogram import random_histogram, naive_histogram, optimized_histogram, comparison_histogram
s1 = Simulation()

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        #title
        self.title('Are You The One?')
        self.master_frame = tk.Frame(self)
        self.master_frame.pack()
        #create exit button
        options_frame = tk.Frame(self.master_frame,relief=tk.RAISED,borderwidth=0,width=10)
        options_frame.grid(row=0,column=0)
        exit_btn = tk.Button(text='Stop Game', command=self.quit,master=options_frame,relief=tk.RAISED,width=5)
        restart_btn = tk.Button(text='Restart',command=self.restart,master=options_frame,relief=tk.RAISED,width=5)

        exit_btn.grid(row=0,column=0)
        restart_btn.grid(row=1,column=0)

        #greet user and list contestants
        title_frame = tk.Frame(self.master_frame)
        title_frame.grid(row=0,column=1)
        greeting = tk.Label(title_frame,text='Welcome to Are You The One!',width=100,bg='white',fg='black')
        greeting.grid(row=0,column=0)
        prompt = tk.Label(title_frame,text='Please select which algorithm you would like to use to solve the game',width=100,bg='white',fg='black',font='bold')
        prompt.grid(row=1,column=0)
        random_btn = tk.Button(text='Random Algorithm',command=self.random_frame,master=self.master_frame, relief=tk.RAISED,bg='red',fg='black')
        random_btn.grid(row=1,column=1)
        naive_btn = tk.Button(text='Naive Algorithm',command=self.naive_frame,master=self.master_frame, relief=tk.RAISED,bg='red',fg='black')
        naive_btn.grid(row=2,column=1)
        optimized_btn = tk.Button(text='Optimized Algorithm',command=self.optimized_frame,master=self.master_frame, relief=tk.RAISED,bg='red',fg='black')
        optimized_btn.grid(row=3,column=1)
        compare_btn = tk.Button(text='Compare all Algorithms',command=self.all_frames,master=self.master_frame, relief=tk.RAISED,bg='red',fg='black')
        compare_btn.grid(row=4,column=1)
    #define method to quit
    def quit(self, event=None):
        self.destroy()
    #define method to restart
    def restart(self, event=None):
        self.destroy()
        new_root = GUI()
        
        root.mainloop()
    #functions to assign to buttons
    def random_frame(self):
        histogram  = random_histogram(1000)
        plt.show()
    def naive_frame(self):
        histogram = naive_histogram(1000)
        plt.show()
    def optimized_frame(self):
        histogram = optimized_histogram(1000)
        plt.show()
    def all_frames(self):
        histogram = comparison_histogram(1000)
        plt.show()

if __name__ == '__main__':
    root = GUI()
    root.mainloop()

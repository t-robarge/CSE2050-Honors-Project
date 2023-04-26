import tkinter as tk
import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from are_you_the_one import Contestant, Simulation
from histogram import random_histogram, naive_histogram, optimized_histogram
s1 = Simulation()

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#print(color.BOLD + 'Hello, World!' + color.END)
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
        naive_btn = tk.Button(text='Optimized Algorithm',command=self.optimized_frame,master=self.master_frame, relief=tk.RAISED,bg='red',fg='black')
        naive_btn.grid(row=3,column=1)
#define method to quit
    def quit(self, event=None):
        self.destroy()
    def restart(self, event=None):
        self.destroy()
        new_root = GUI()
        
        root.mainloop()
    def random_frame(self):
        histogram  = random_histogram(1000)
        plt.show()
    def naive_frame(self):
        histogram = naive_histogram(1000)
        plt.show()
    def optimized_frame(self):
        histogram = optimized_histogram(1000)
        plt.show()

    #create object rep of GUI

 

    

        """
    meeting = tk.Label(title_frame, text="Let's meet our contestants:")
    count = 0
    contestant_frame = tk.Frame(master_frame)
    contestant_frame.grid(row=1,column=1)
    for i in range(4):
        for j in range(4):
            contestant = tk.Label(contestant_frame,text=s1.meet_contestants()[count],width=10,fg='purple',bg='white',relief=tk.RIDGE)
            #contestant.grid(row=j+2,column=i)
            contestant.pack()
            count += 1


    #put it on the screen
    greeting.grid(row=0, column=0)
    meeting.grid(row=1, column=0)
        """


#run the GUI
if __name__ == '__main__':
    root = GUI()
    root.mainloop()

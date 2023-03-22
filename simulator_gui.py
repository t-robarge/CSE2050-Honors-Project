import tkinter as tk
import matplotlib 
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from are_you_the_one import Contestant, Simulation
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

#define method to quit
def quit(event=None):
    root.destroy()
def restart(event=None):
    root.destroy()
    new_root = tk.Tk()
    
    root.mainloop


#create object rep of GUI
root = tk.Tk()
master_frame = tk.Frame(root)
master_frame.pack()

#title
root.title('Are You The One?')

#create exit button
options_frame = tk.Frame(master_frame,relief=tk.RAISED,borderwidth=0,width=10)
options_frame.grid(row=0,column=0)
exit_btn = tk.Button(text='Stop Game', command=quit,master=options_frame,relief=tk.RAISED,width=5)
restart_btn = tk.Button(text='Restart',command=restart,master=options_frame,relief=tk.RAISED,width=5)

exit_btn.grid(row=0,column=0)
restart_btn.grid(row=1,column=0)

#greet user and list contestants
title_frame = tk.Frame(master_frame)
title_frame.grid(row=0,column=1)
greeting = tk.Label(title_frame,text='Welcome to Are You The One!',width=100,bg='white',fg='black')
meeting = tk.Label(title_frame, text="Let's meet our contestants:")
count = 0
contestant_frame = tk.Frame(master_frame)
contestant_frame.grid(row=1,column=1)
for i in range(4):
    for j in range(4):
        contestant = tk.Label(contestant_frame,text=s1.meet_contestants()[count],width=10,fg='white',bg='blue',relief=tk.RIDGE)
        #contestant.grid(row=j+2,column=i)
        contestant.pack()
        count += 1


#put it on the screen
greeting.grid(row=0, column=0)
meeting.grid(row=1, column=0)



#run the GUI
root.mainloop()

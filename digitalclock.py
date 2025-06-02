import tkinter as tk
from time import strftime
root = tk.Tk()
root.title("Digital Clock")

clock_label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='cyan')
clock_label.pack(anchor='center')


def update_time():
    time_string = strftime('%H:%M:%S %p')  
    clock_label.config(text=time_string)
    clock_label.after(1000, update_time)  

update_time()


root.mainloop()

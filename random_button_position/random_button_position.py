import tkinter as tk, random
from tkinter import messagebox

WINDOW = tk.Tk()
WINDOW.geometry('200x200')
WINDOW.configure(bg="pink")

def yes():
    messagebox.showinfo(message='HAHAH KNEW IT')
    quit()

def no():
    new_x = random.randint(50,150)
    new_y = random.randint(50,150)
    

    #Check for overlap with the Yes button
    while (yes_button.winfo_x() < new_x < yes_button.winfo_x() + yes_button.winfo_width()
           and yes_button.winfo_y() < new_x < yes_button.winfo_y() + yes_button.winfo_height()):
        
        new_x = random.randint(50,150)
        new_y = random.randint(50,150)
    
    no_button.place(x=new_x,y=new_y)

text = tk.Label(WINDOW, text="Are you dvmp?", bg = "pink", fg="white",font="impact").pack()
yes_button = tk.Button(WINDOW, text='Yes',command=yes, bg="red",fg="white",font="impact")
yes_button.place(x=50, y=50)
no_button = tk.Button(WINDOW, text='No', command=no, bg="red",fg="white",font="impact")
no_button.place(x=100, y=50)

WINDOW.mainloop()
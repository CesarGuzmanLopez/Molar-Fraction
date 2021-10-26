from tkinter import * 
from tkinter import messagebox

import tkinter as tk
import tkinter.ttk as ttk

class NuevoProyectoApp:
    def __init__(self, master=None):
        # build ui
        self.frame1 = tk.Frame(master, container='false')
        self.labelDataentry = tk.Label(self.frame1)
        self.labelDataentry.configure(compound='top', font='{Arial} 10 {bold}', justify='left', text='Data Entry')
        self.labelDataentry.place(anchor='nw', relwidth='0.12', relx='0.13', rely='0.06', x='0', y='0')
        self.label2 = tk.Label(self.frame1)
        self.label2.configure(relief='flat', text='Number of Acido Base Equilibria')
        self.label2.place(height='10', relheight='0.0', relwidth='0.0', relx='0.0', rely='0.0', width='200', y='60')
        self.__tkvar = tk.StringVar(value='')
        __values = ['none', '1pka', '']
        self.optionmenu1 = tk.OptionMenu(self.frame1, self.__tkvar, None, *__values, command=None)
        self.optionmenu1.place(anchor='nw', bordermode='inside', relheight='0.05', relwidth='0.04', width='50', x='200', y='50')
        self.frame1.configure(height='450', takefocus=True, width='600')
        self.frame1.grid(column='0', row='0')

        # Main widget
        self.mainwindow = self.frame1
    
    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = NuevoProyectoApp(root)
    app.run()

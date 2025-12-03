import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
class Sidebar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        def select_file(): 
            filetypes = ("All files","*.*")
            filename = fd.askopenfilname(title="open a file ", initialder= "/", filetypes=filetypes)
            showinfo(title="selected a file", message=filename)
            open_button =tk.Button(
                text="Open a File "
                command= select_file
            )
            open_button(expand=True)

            self.mainloop ()

         
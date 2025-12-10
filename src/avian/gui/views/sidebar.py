import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class Sidebar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        open_button = tk.Button(
            self,
            text="Open a File ",
            command=lambda: self.select_file
        )
        open_button.pack(expand=True)

    def select_file():
        filetypes = ("All files","*.*")
        filename = fd.askopenfilename(title="open a file", filetypes=filetypes)
        showinfo(title="selected a file", message=filename)

         
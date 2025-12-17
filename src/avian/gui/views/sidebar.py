import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from src.avian.gui.windows.connection import ConnectionWindow


class Sidebar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(padx=50, pady=10)

        
        self.recepient = tk.StringVar()
        entry = tk.Entry(self, textvariable=self.recepient)
        entry.pack(pady=10)

        self.open_button = ttk.Button(
            self,
            textvariable=self.recepient,
            command=self.select_file
        )
        self.open_button.pack(expand=True)

        self.connect_button = ttk.Button(
            self,
            text="Connect to peer",
            command=lambda: ConnectionWindow(self)
        )
        self.connect_button.pack(expand=True)

    @staticmethod
    def select_file():
        filetypes = {
            ("All files", "*.*")
        }
        filename = fd.askopenfilename(title="open a file", filetypes=filetypes)
        showinfo(title="selected a file", message=filename)

         
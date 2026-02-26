import tkinter as tk
from tkinter import ttk


class Toolbar(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.columnconfigure(0)
        self.rowconfigure(0, weight=1, uniform="x")
        self.rowconfigure(1, weight=1, uniform="x")

        self.configure(padx=5, pady=5)

        self.button = ttk.Button(self, text="Connection Window")
        self.button.grid(column=0, row=0, sticky="w")

        self.button2 = ttk.Button(self, text="Settings")
        self.button2.grid(column=0, row=1, sticky="e")

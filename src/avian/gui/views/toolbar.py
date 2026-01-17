import tkinter as tk
from tkinter import ttk


class Toolbar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.columnconfigure(0, weight=1, uniform="x")
        self.columnconfigure(1, weight=1, uniform="x")
        self.rowconfigure(0)

        self.configure(padx=5, pady=5)

        self.button = ttk.Button(self, text="test", padding=(0, 0))
        self.button.grid(column=0, row=0, sticky="w")

import tkinter as tk
from tkinter import ttk


class Sidebar(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.configure(padx=50, pady=10)

        ttk.Label(self, text="test").grid()

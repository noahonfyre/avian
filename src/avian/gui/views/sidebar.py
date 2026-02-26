import tkinter as tk
from tkinter import ttk

from src.avian.gui.windows import ConnectionWindow


class Sidebar(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.configure(padx=50, pady=10)

        ttk.Label(self, text="test").grid()

import tkinter as tk
from tkinter import ttk


class SettingsOption(tk.Frame):
    """
    A helper class for defining an option with an associated label easily.
    """

    def __init__(self, master, text: str):
        super().__init__(master)

        self.config(padx=5)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0)

        self.heading = ttk.Label(self, text=text)
        self.heading.grid(column=0, row=0, sticky="we")

        self.wrapper = tk.Frame(self)
        self.wrapper.grid(column=0, row=1, sticky="nswe")

        self.wrapper.columnconfigure(0, weight=1)

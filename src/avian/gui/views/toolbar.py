import tkinter as tk
from tkinter import ttk

from avian.gui.windows.settings.window import SettingsWindow
from src.avian.gui.windows.connection.window import ConnectionWindow


class Toolbar(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)                
        self.rowconfigure(0)
        

        self.configure(padx=5, pady=5)

        self.button = ttk.Button(self, text="Connection Window")
        self.button.grid(column=0, row=0, sticky="w")
        self.button["command"]=lambda: ConnectionWindow(self)

        self.button2 = ttk.Button(self, text="Settings")
        self.button2.grid(column=1, row=0, sticky="e")
        self.button2["command"]=lambda: SettingsWindow(self)
            

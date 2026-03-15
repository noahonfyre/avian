import tkinter as tk
from tkinter import ttk

from avian.gui.windows.settings.about import AboutTab
from avian.gui.windows.settings.general import GeneralTab


class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Settings")
        self.geometry("600x350")
        self.minsize(600, 350)
        self.transient(parent)
        self.grab_set()

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=0, column=0, sticky="nsew")

        self.notebook.add(GeneralTab(self.notebook), text="General")
        self.notebook.add(AboutTab(self.notebook), text="About")

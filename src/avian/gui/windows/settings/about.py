import tkinter as tk
from tkinter import PhotoImage, ttk

from avian.models.constants import NAME, VERSION
from avian.models.resources import get_resource


class AboutTab(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.icon = tk.PhotoImage(data=get_resource("icon.png").read_bytes())

        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.overview = ttk.Frame(self, padding=10)
        self.overview.grid(column=0, row=0, sticky="nsew")

        self.app_icon = PhotoImage(data=get_resource("icon.png").read_bytes())

        ttk.Label(self.overview, image=self.app_icon).grid()
        ttk.Label(self.overview, text="About Avian").grid()

        self.details = ttk.LabelFrame(self, text="About")
        self.details.grid(column=0, row=1, sticky="nsew")

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
        self.rowconfigure(1)

        self.overview = ttk.Frame(self, padding=10)
        self.overview.grid(column=0, row=0, sticky="nsew")

        self.app_icon = PhotoImage(data=get_resource("icon.png").read_bytes())

        self.icon_label = ttk.Label(self.overview, image=self.app_icon)
        self.icon_label.grid()

        self.version_label = ttk.Label(self.overview, text=f"{NAME} v{VERSION}")
        self.version_label.grid(pady=5)

        self.tagline_label = ttk.Label(
            self.overview,
            text="Here is a placeholder of the tagline of the application",
            wraplength=128,
        )
        self.tagline_label.grid()

        self.copyright_label = ttk.Label(self, text="© 2025-2026 | MIT License")
        self.copyright_label.grid(column=0, row=1, padx=5)

        self.details = ttk.LabelFrame(self, text="Contributors")
        self.details.grid(column=1, row=0, rowspan=2, sticky="nsew", padx=10, pady=5)

        ttk.Label(
            self.details,
            text="Noah Zeisberg",
        ).grid(sticky="nw")
        ttk.Label(
            self.details,
            text="- Technical Lead",
        ).grid(sticky="nw")
        ttk.Label(
            self.details,
            text="- Fullstack Developer",
        ).grid(sticky="nw")
        ttk.Label(
            self.details,
            text="- Project Owner",
        ).grid(sticky="nw")
        ttk.Label(self.details, text="").grid(sticky="nw")

        ttk.Label(
            self.details,
            text="Luca Peter",
        ).grid(sticky="nw")
        ttk.Label(
            self.details,
            text="- Frontend Developer",
        ).grid(sticky="nw")
        ttk.Label(self.details, text="").grid(sticky="nw")

        ttk.Label(
            self.details,
            text="Dominik Bauer",
        ).grid(sticky="nw")
        ttk.Label(
            self.details,
            text="- Frontend Developer",
        ).grid(sticky="nw")
        ttk.Label(self.details, text="").grid(sticky="nw")

        ttk.Label(
            self.details,
            text="Enrico Sanfratello",
        ).grid(sticky="nw")
        ttk.Label(
            self.details,
            text="- Frontend Developer",
        ).grid(sticky="nw")
        ttk.Label(self.details, text="").grid(sticky="nw")

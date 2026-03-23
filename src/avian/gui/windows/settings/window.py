import tkinter as tk
from tkinter import ttk

from avian.gui.windows.settings.general import GeneralSection
from avian.models.constants import NAME, VERSION
from avian.models.resources import get_resource


class SettingsWindow(tk.Toplevel):
    """
    Provides an interface for tweaking application settings.
    """

    def __init__(self, parent):
        super().__init__(parent)

        self.title("Settings")
        self.geometry("550x300")
        self.minsize(550, 300)
        self.transient(parent)
        self.grab_set()

        self.icon = tk.PhotoImage(data=get_resource("icon.png").read_bytes())

        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1)

        self.overview = ttk.Frame(self, padding=10)
        self.overview.grid(column=0, row=0, sticky="nsew")

        self.app_icon = tk.PhotoImage(data=get_resource("icon.png").read_bytes())

        self.icon_label = ttk.Label(self.overview, image=self.app_icon)
        self.icon_label.grid()

        self.version_label = ttk.Label(self.overview, text=f"{NAME} v{VERSION}")
        self.version_label.grid(pady=5)

        self.tagline_label = ttk.Label(
            self.overview,
            text="Peer-to-peer file transfers, as simple and effective as they can be.",
            wraplength=128,
        )
        self.tagline_label.grid()

        self.copyright_label = ttk.Label(self, text="© 2025-2026 | MIT License")
        self.copyright_label.grid(column=0, row=1, padx=5)

        self.general = GeneralSection(self)
        self.general.grid(column=1, row=0, sticky="nsew", padx=5)

        self.button_wrapper = ttk.Frame(self)
        self.button_wrapper.grid(column=1, row=1, padx=5, pady=5, sticky="nse")

        self.save_button = ttk.Button(self.button_wrapper, text="Save", command=self.general.apply_config)
        self.save_button.grid(column=1, row=1, sticky="se")

        self.close_button = ttk.Button(self.button_wrapper, text="Close", command=self.destroy)
        self.close_button.grid(column=0, row=1, sticky="se")

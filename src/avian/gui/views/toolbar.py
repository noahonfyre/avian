import tkinter as tk
from tkinter import ttk

from avian.gui.windows.connection.window import ConnectionWindow
from avian.gui.windows.settings.window import SettingsWindow
from avian.models import Channel
from avian.models.messages import Message


class Toolbar(tk.Frame):
    def __init__(self, master, incoming: Channel[Message], outgoing: Channel[Message]):
        super().__init__(master)

        self.incoming = incoming
        self.outgoing = outgoing

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0)

        self.configure(padx=5, pady=5)

        self.connect_button = ttk.Button(self, text="Connection Window")
        self.connect_button.grid(column=0, row=0, sticky="w")
        self.connect_button["command"] = lambda: ConnectionWindow(
            self, self.incoming, self.outgoing
        )

        self.settings_button = ttk.Button(self, text="Settings")
        self.settings_button.grid(column=1, row=0, sticky="e")
        self.settings_button["command"] = lambda: SettingsWindow(self)

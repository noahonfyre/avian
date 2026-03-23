import tkinter as tk
from pathlib import Path
from tkinter import ttk

from avian.gui.windows.connection.window import ConnectionWindow
from avian.gui.windows.settings.window import SettingsWindow
from avian.models.channel import Channel
from avian.models.config.config import Config
from avian.models.messages import Message
from avian.models.resources import get_resource
from avian.utils.paths import open_folder


class Toolbar(tk.Frame):
    """
    Provides the main way of interaction with the application.
    """

    def __init__(self, master, incoming: Channel[Message], outgoing: Channel[Message]):
        super().__init__(master)

        self.incoming = incoming
        self.outgoing = outgoing

        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0)

        self.configure(padx=2, pady=2)

        self.icon_connect = tk.PhotoImage(
            data=get_resource("icon/connect.png").read_bytes(),
            width=16,
            height=16,
        )
        self.icon_saves = tk.PhotoImage(
            data=get_resource("icon/saves.png").read_bytes(),
            width=16,
            height=16,
        )
        self.icon_settings = tk.PhotoImage(
            data=get_resource("icon/settings.png").read_bytes(),
            width=16,
            height=16,
        )

        self.connect_button = ttk.Button(
            self, text="Connect", image=self.icon_connect, compound="left"
        )
        self.connect_button.grid(column=0, row=0, sticky="w")
        self.connect_button["command"] = lambda: ConnectionWindow(
            self, self.incoming, self.outgoing
        )

        self.saves_button = ttk.Button(
            self, text="Saves", image=self.icon_saves, compound="left"
        )
        self.saves_button.grid(column=1, row=0, sticky="w")
        self.saves_button["command"] = lambda: open_folder(Path(Config.SAVE_PATH.get()))

        self.settings_button = ttk.Button(self, text="Settings")
        self.settings_button = ttk.Button(
            self, text="Settings", image=self.icon_settings
        )

        self.settings_button.grid(column=1, row=0, sticky="e")
        self.settings_button["command"] = lambda: SettingsWindow(self)

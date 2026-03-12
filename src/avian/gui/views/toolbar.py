from pathlib import Path
import tkinter as tk
from tkinter import ttk

from avian.gui.windows.connection.window import ConnectionWindow
from avian.gui.windows.settings.window import SettingsWindow
from avian.models.channel import Channel
from avian.models.constants import SAVE_PATH
from avian.models.messages import Message
from avian.utils.paths import open_folder


class Toolbar(tk.Frame):
    def __init__(self, master, incoming: Channel[Message], outgoing: Channel[Message], run_path: Path):
        super().__init__(master)

        self.incoming = incoming
        self.outgoing = outgoing
        self.run_path = run_path

        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0)

        self.configure(padx=2, pady=2)

        self.icon_settings = tk.PhotoImage(file=self.run_path / "assets" / "app" / "settings.png", width=16, height=16)
        self.icon_connect = tk.PhotoImage(file=self.run_path / "assets" / "app" / "connect.png", width=16, height=16)
        

        self.connect_button = ttk.Button(self, text="Connect", image=self.icon_connect, compound="left")
        self.connect_button.grid(column=0, row=0, sticky="w")
        self.connect_button["command"] = lambda: ConnectionWindow(
            self, self.incoming, self.outgoing
        )

        self.savedfiles_button = ttk.Button(self, text="saved Files")
        self.savedfiles_button.grid(column=1, row=0, sticky="w")
        self.savedfiles_button["command"] = lambda: open_folder(SAVE_PATH)   

        
        self.settings_button = ttk.Button(self, text="Settings")
        self.settings_button = ttk.Button(self, text="Settings", image=self.icon_settings)

        self.settings_button.grid(column=1, row=0, sticky="e")
        self.settings_button["command"] = lambda: SettingsWindow(self)

import tkinter as tk
import tkinter.filedialog as fd
from pathlib import Path
from tkinter import ttk

from avian.gui.windows.settings.settings_option import SettingsOption
from avian.models.config.config import Config


class GeneralSection(ttk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="General")

        self.config(padding=10)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0)

        self.protocol_port_var = tk.IntVar(value=Config.PROTOCOL_PORT.get())

        self.protocol_port_option = SettingsOption(self, "Protocol port")
        self.protocol_port_option.grid(column=0, row=0, sticky="nsew")

        self.protocol_port_spinbox = ttk.Spinbox(
            self.protocol_port_option.wrapper,
            to=65_536,
            textvariable=self.protocol_port_var
        )
        self.protocol_port_spinbox.grid(sticky="nswe")

        self.chunk_size_var = tk.IntVar(value=Config.CHUNK_SIZE.get())

        self.chunk_size_option = SettingsOption(self, "Chunk size")
        self.chunk_size_option.grid(column=1, row=0, sticky="nsew")

        self.chunk_size_spinbox = ttk.Spinbox(
            self.chunk_size_option.wrapper,
            increment=1024, to=0xFFFFFF,
            textvariable=self.chunk_size_var
        )
        self.chunk_size_spinbox.grid(sticky="nswe")

        self.save_location_var = tk.StringVar(value=Config.SAVE_PATH.get())

        self.save_location_option = SettingsOption(self, "Save location")
        self.save_location_option.grid(columnspan=2, sticky="nsew")

        self.save_location_display = ttk.Entry(
            self.save_location_option.wrapper,
            textvariable=self.save_location_var,
            state="disabled"
        )
        self.save_location_display.grid(column=0, row=0, sticky="nswe")

        self.save_location_browse_button = ttk.Button(
            self.save_location_option.wrapper,
            text="Select...",
            command=self.select_folder
        )
        self.save_location_browse_button.grid(column=1, row=0, sticky="nswe")

    def apply_config(self):
        Config.PROTOCOL_PORT.set(self.protocol_port_var.get())
        Config.CHUNK_SIZE.set(self.chunk_size_var.get())
        Config.SAVE_PATH.set(self.save_location_var.get())

        Config.SPEC.apply()
        self.master.destroy()

    def select_folder(self) -> None:
        raw_folder: str = fd.askdirectory(initialdir=Path(Config.SAVE_PATH.get()), title="Add files")

        self.save_location_var.set(raw_folder)

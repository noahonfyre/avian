import tkinter as tk
import tkinter.filedialog as fd
from pathlib import Path
from tkinter import ttk
from typing import List, Literal, Tuple

from avian.models.channel import Channel
from avian.models.config.config import Config
from avian.models.messages import Message, StartSender


class ConnectionWindow(tk.Toplevel):
    """
    Provides functionality for initiating a transaction such as selecting files and entering the peer address and port.
    """

    def __init__(self, parent, incoming: Channel[Message], outgoing: Channel[Message]):
        super().__init__(parent)

        self.selected_name: str = ""

        self.filenames: List[Path] = []
        self.incoming = incoming
        self.outgoing = outgoing

        self.title("Initiate transaction")
        self.geometry("600x350")
        self.minsize(600, 350)
        self.transient(parent)
        self.grab_set()

        self.configure(padx=10, pady=5)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1)

        self.attachment_wrapper = tk.Frame(self)
        self.attachment_wrapper.grid(row=0, column=0, sticky="nsew")
        self.attachment_wrapper.columnconfigure(0, weight=1)
        self.attachment_wrapper.columnconfigure(1)
        self.attachment_wrapper.rowconfigure(0, weight=1)

        self.file_list = ttk.Treeview(self.attachment_wrapper)
        self.file_list.grid(row=0, column=0, sticky="nsew")
        self.file_list.heading("#0", text="Files")

        self.file_list_scrollbar = ttk.Scrollbar(
            self.attachment_wrapper, orient="vertical", command=self.file_list.yview
        )
        self.file_list.configure(yscrollcommand=self.file_list_scrollbar.set)
        self.file_list_scrollbar.grid(row=0, column=1, sticky="nsew")

        self.compose_wrapper = ttk.LabelFrame(
            self, text="Peer", padding=(10, 5, 10, 10)
        )
        self.compose_wrapper.grid(row=0, column=1, padx=(10, 0), sticky="new")
        self.compose_wrapper.columnconfigure(0, weight=1)
        self.compose_wrapper.columnconfigure(1, weight=1)

        ttk.Label(self.compose_wrapper, text="Peer address").grid(
            row=0, column=0, sticky="w"
        )
        self.target_address = tk.StringVar()
        self.target_address_entry = ttk.Entry(
            self.compose_wrapper, textvariable=self.target_address
        )
        self.target_address_entry.grid(row=1, column=0, sticky="nsew")

        ttk.Label(self.compose_wrapper, text="Peer port").grid(
            row=0, column=1, sticky="w"
        )
        self.target_port = tk.IntVar(value=Config.PROTOCOL_PORT.get())
        self.target_port_entry = ttk.Spinbox(
            self.compose_wrapper, from_=1, to=65536, textvariable=self.target_port
        )
        self.target_port_entry.grid(row=1, column=1, sticky="nsew")

        self.file_pane = ttk.Frame(self)
        self.file_pane.grid(column=0, row=1, pady=5, sticky="nsw")

        self.add_button = ttk.Button(
            self.file_pane, text="Add", command=self.select_file
        )
        self.add_button.grid(column=0, row=0, sticky="w")

        self.remove_button = ttk.Button(
            self.file_pane, text="Remove", command=self.remove_selection
        )
        self.remove_button.grid(column=1, row=0, sticky="w")

        self.action_pane = ttk.Frame(self)
        self.action_pane.grid(column=1, row=1, pady=5, sticky="nse")

        self.cancel_button = ttk.Button(
            self.action_pane, text="Cancel", command=self.close
        )
        self.cancel_button.grid(column=0, row=0, sticky="e")

        self.connect_button = ttk.Button(
            self.action_pane, text="Connect", command=self.connect
        )
        self.connect_button.grid(column=1, row=0, sticky="e")

        self.file_list.bind("<ButtonRelease-1>", lambda *_: self.handle_item_select())

    def handle_item_select(self):
        item = self.file_list.focus()
        self.selected_name = item

    def remove_selection(self):
        if self.selected_name == "":
            return
        self.file_list.delete(self.selected_name)

    def update_remove_button(self):
        if self.file_list:
            pass

    def connect(self):
        self.outgoing.send(
            StartSender(
                self.target_address.get(),
                self.target_port.get(),
                self.filenames,
            )
        )
        self.destroy()

    def select_file(self):
        filetypes = {("All files", "*.*")}
        raw_filenames: Literal[""] | Tuple[str, ...] = fd.askopenfilenames(
            title="Add files", filetypes=filetypes
        )
        self.filenames = [Path(filename) for filename in raw_filenames]

        for filename in self.filenames:
            self.file_list.insert("", "end", text=filename.name)

    def close(self):
        self.destroy()

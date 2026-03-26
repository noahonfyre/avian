import tkinter as tk
from tkinter import ttk
from typing import Dict

from avian.models.channel import Channel
from avian.models.constants import LOGGER
from avian.models.messages import Message


class Mainframe(tk.Frame):
    """
    Provides information of transaction progress.
    """

    def __init__(self, master, incoming: Channel[Message], outgoing: Channel[Message]):
        super().__init__(master)

        self.row_indices: Dict[str, str] = {}

        self.incoming = incoming
        self.outgoing = outgoing

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1)

        self.treeview = ttk.Treeview(
            self, columns=("Size", "Progress", "Status", "Speed", "ETA")
        )
        self.vertical_scrollbar = ttk.Scrollbar(
            self, orient="vertical", command=self.treeview.yview
        )
        self.horizontal_scrollbar = ttk.Scrollbar(
            self, orient="horizontal", command=self.treeview.xview
        )
        self.treeview.configure(yscrollcommand=self.vertical_scrollbar.set)
        self.treeview.configure(xscrollcommand=self.horizontal_scrollbar.set)

        self.treeview.heading("#0", text="File name")
        self.treeview.heading("Size", text="Size")
        self.treeview.heading("Progress", text="Progress")
        self.treeview.heading("Status", text="Status")
        self.treeview.heading("Speed", text="Speed")
        self.treeview.heading("ETA", text="ETA")

        self.treeview.column("#0", width=100)
        self.treeview.column("Size", width=20)
        self.treeview.column("Progress", width=1)
        self.treeview.column("Status", width=1)
        self.treeview.column("Speed", width=1)
        self.treeview.column("ETA", width=1)

        self.treeview.grid(row=0, column=0, sticky="nsew")
        self.vertical_scrollbar.grid(row=0, column=1, sticky="nsew")

    def delete_item(self, address: str, port: int, filename: str):
        """
        Helper method for deleting an item as well as its associated row index.
        """

        key = f"{address}:{port}/{filename}"

        if key in self.row_indices:
            self.treeview.delete(self.row_indices[key])
            self.row_indices.pop(key)
        else:
            LOGGER.warning("Nothing to delete.")

    def update_item(
        self,
        address: str,
        port: int,
        filename: str,
        size: str,
        progress: str,
        status: str,
        speed: str,
        eta: str,
    ) -> None:
        """
        Helper method for creating and updating new entries.
        Automatically handles row indices as needed.
        """

        key = f"{address}:{port}/{filename}"

        if key in self.row_indices:
            self.treeview.item(
                self.row_indices[key],
                text=filename,
                values=(size, progress, status, speed, eta),
            )
        else:
            iid = self.treeview.insert(
                "",
                "end",
                text=filename,
                values=(size, progress, status, speed, eta),
            )
            self.row_indices[key] = iid

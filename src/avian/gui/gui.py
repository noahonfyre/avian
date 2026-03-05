import time
import tkinter as tk
from typing import Callable, Optional

from avian.gui.views import Mainframe, Sidebar, Statistics, Toolbar
from avian.models.channel import Channel
from avian.models.constants import LOGGER
from avian.models.messages import Message, TransactionUpdate


class GUI(tk.Tk):
    def __init__(self, incoming: Channel[Message], outgoing: Channel[Message]) -> None:
        super().__init__()

        self.incoming = incoming
        self.outgoing = outgoing

        self.title("Avian - Peer-to-peer file transfers")

        self.geometry("900x500")
        self.minsize(900, 500)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self.rowconfigure(0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2)
        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)

        self.toolbar = Toolbar(self, self.incoming, self.outgoing)
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.sidebar = Sidebar(self, self.incoming, self.outgoing)
        self.sidebar.grid(row=1, column=0, sticky="nsew")

        self.mainframe = Mainframe(self, self.incoming, self.outgoing)
        self.mainframe.grid(row=1, column=1, sticky="nsew")

        self.statistics = Statistics(self, self.incoming, self.outgoing)
        self.statistics.grid(row=2, column=0, columnspan=2, sticky="nsew")

    def run(self) -> None:
        self.schedule(20, self.consume_events)
        self.mainloop()

    def consume_events(self) -> None:
        start = time.perf_counter()
        while True:
            if self.incoming.is_empty():
                break
            data: Optional[Message] = self.incoming.recv()
            LOGGER.debug(data)
        elapsed = time.perf_counter() - start
        LOGGER.debug(f"Event cycle lasted {elapsed:.2f} seconds")

    def handle_update_transactions(self, msg: Message):
        if isinstance(msg, TransactionUpdate):
            treeview = self.mainframe.treeview
            
            treeview.insert("#0", tk.END, text=msg.filename)
            treeview.insert("Size", text=msg.file_size)
            treeview.insert("Progress", text=msg.bytes_transferred/msg.file_size)
            treeview.insert("Status", text="Status")
            treeview.insert("Speed", text=msg.bytes_transferred/msg.elapsed)
            treeview.insert("Health", text="Health")
            treeview.insert("ETA", text=msg.file_size/(msg.bytes_transferred/msg.elapsed))


    def schedule(self, interval_ms: int, func: Callable[[], None]) -> None:
        func()
        self.after(interval_ms, self.schedule, interval_ms, func)

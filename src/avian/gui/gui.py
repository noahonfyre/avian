import time
import tkinter as tk
from typing import Callable, Optional

from avian.gui.views import Mainframe, Sidebar, Statistics, Toolbar
from avian.models.channel import Channel
from avian.models.messages import Message, Shutdown, TransactionUpdate


class GUI(tk.Tk):
    def __init__(self, incoming: Channel[Message], outgoing: Channel[Message]) -> None:
        super().__init__()

        self.incoming = incoming
        self.outgoing = outgoing

        self.title("Avian - Peer-to-peer file transfers")

        self.geometry("1200x650")
        self.minsize(1200, 650)
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
        self.outgoing.send(Shutdown())

    def consume_events(self) -> None:
        start = time.perf_counter()
        while True:
            if self.incoming.is_empty():
                break
            msg: Optional[Message] = self.incoming.recv()
            if not msg:
                continue
            # TODO: change if-elif branching to a more dynamic solution
            if isinstance(msg, TransactionUpdate):
                self.handle_update_transactions(msg)

    def handle_update_transactions(self, msg: TransactionUpdate):
        progress = msg.bytes_transferred / msg.file_size
        speed = msg.bytes_transferred / msg.elapsed
        remaining = msg.file_size - msg.bytes_transferred
        eta = remaining / speed

        self.mainframe.upsert_info(
            msg.address,
            msg.port,
            msg.filename,
            f"{msg.bytes_transferred}B/{msg.file_size}B",
            f"{progress * 100:.2f}%",
            "status",
            f"{speed:.2f}B/s",
            "health",
            f"{eta:.2f}s",
        )

    def schedule(self, interval_ms: int, func: Callable[[], None]) -> None:
        func()
        self.after(interval_ms, self.schedule, interval_ms, func)

import tkinter as tk
from typing import Callable, Optional

from avian.gui.store import TransactionStore
from avian.gui.views import Mainframe, Statistics, Toolbar
from avian.models.channel import Channel
from avian.models.messages import (
    Message,
    Shutdown,
    TransactionConclude,
    TransactionUpdate, ResolverUpdate,
)
from avian.models.resources import get_resource


class GUI(tk.Tk):
    def __init__(self, incoming: Channel[Message], outgoing: Channel[Message]) -> None:
        super().__init__()

        self.incoming = incoming
        self.outgoing = outgoing

        self.store = TransactionStore()

        self.title("Avian - Peer-to-peer file transfers")
        self.icon = tk.PhotoImage(data=get_resource("icon.png").read_bytes())
        self.iconphoto(True, self.icon)

        self.geometry("1000x550")
        self.minsize(1000, 550)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self.rowconfigure(0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2)
        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)

        self.toolbar = Toolbar(self, self.incoming, self.outgoing)
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.mainframe = Mainframe(self, self.incoming, self.outgoing)
        self.mainframe.grid(row=1, column=1, columnspan=2, sticky="nsew")

        self.statistics = Statistics(self, self.incoming, self.outgoing)
        self.statistics.grid(row=2, column=0, columnspan=2, sticky="nsew")

    def run(self) -> None:
        self.schedule(20, self.consume_events)
        self.mainloop()
        self.outgoing.send(Shutdown())

    def consume_events(self) -> None:
        while True:
            if self.incoming.is_empty():
                break
            msg: Optional[Message] = self.incoming.recv()
            if not msg:
                continue
            # TODO: change if-elif branching to a more dynamic solution
            if isinstance(msg, TransactionUpdate):
                self.handle_update_transactions(msg)
            elif isinstance(msg, TransactionConclude):
                self.handle_conclude_transactions(msg)
            elif isinstance(msg, ResolverUpdate):
                self.handle_update_resolver(msg)

    def handle_update_transactions(self, msg: TransactionUpdate):
        key = f"{msg.address}:{msg.port}/{msg.filename}"
        progress = msg.bytes_transferred / msg.file_size
        speed = msg.bytes_transferred / msg.elapsed
        remaining = msg.file_size - msg.bytes_transferred
        eta = remaining / speed

        self.store.transactions[key].address = msg.address
        self.store.transactions[key].port = msg.port
        self.store.transactions[key].filename = msg.filename
        self.store.transactions[key].transferred = msg.bytes_transferred
        self.store.transactions[key].size = msg.file_size
        self.store.transactions[key].progress = progress
        self.store.transactions[key].speed = speed
        self.store.transactions[key].eta = eta
        self.store.push_updates(self.mainframe, self.statistics)

    def handle_conclude_transactions(self, msg: TransactionConclude) -> None:
        key = f"{msg.address}:{msg.port}/{msg.filename}"
        self.store.transactions.pop(key)
        self.after(
            10_000,
            lambda: self.mainframe.delete_item(msg.address, msg.port, msg.filename),
        )
        self.store.push_updates(self.mainframe, self.statistics)

    def handle_update_resolver(self, msg: ResolverUpdate) -> None:
        if msg.private:
            self.store.private_ip = msg.private
        if msg.public:
            self.store.public_ip = msg.public
        self.store.push_updates(self.mainframe, self.statistics)

    def schedule(self, interval_ms: int, func: Callable[[], None]) -> None:
        func()
        self.after(interval_ms, self.schedule, interval_ms, func)

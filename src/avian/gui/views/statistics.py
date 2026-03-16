import tkinter as tk
from tkinter import ttk

from avian.gui.misc.dynamic_template import DynamicTemplate
from avian.gui.misc.supplier_template import SupplierTemplate
from avian.models.channel import Channel
from avian.models.messages import Message
from avian.utils.numbers import fmt_bin


class Statistics(tk.Frame):
    def __init__(self, master, incoming: Channel[Message], outgoing: Channel[Message]):
        super().__init__(master)

        self.incoming = incoming
        self.outgoing = outgoing

        self.configure(padx=10, pady=5)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0)

        self.active_transactions = tk.IntVar()

        self.active_transaction_label = ttk.Label(
            self,
            textvariable=DynamicTemplate(
                "{} active transaction(s)",
                self.active_transactions,
            ),
        )
        self.active_transaction_label.grid(row=0, column=0, sticky="w")

        self.ip_addresses = tk.StringVar()

        self.address_label = ttk.Label(self, textvariable=self.ip_addresses)
        self.address_label.grid(row=0, column=1)

        self.downstream_speed = tk.DoubleVar()
        self.upstream_speed = tk.DoubleVar()

        self.speed_label = ttk.Label(
            self,
            textvariable=SupplierTemplate(
                lambda down, up: f"Downstream: {fmt_bin(down, 'B/s')} | Upstream: {fmt_bin(up, 'B/s')}",
                self.downstream_speed,
                self.upstream_speed,
            ),
        )
        self.speed_label.grid(row=0, column=2, sticky="e")

import tkinter as tk
from tkinter import ttk

from avian.gui.misc.dynamic_template import DynamicTemplate


class Statistics(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.configure(padx=10, pady=5)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0)

        self.active_transactions = tk.IntVar()
        self.active_peers = tk.IntVar()

        self.active_connections = ttk.Label(
            self,
            textvariable=DynamicTemplate(
                "{} active transaction(s) via {} peer(s)",
                self.active_transactions,
                self.active_peers,
            ),
        )
        self.active_connections.grid(row=0, column=0, sticky="w")

        self.private_ip = tk.StringVar(value="127.0.0.1")
        self.public_ip = tk.StringVar(value="127.0.0.1")

        self.address_display = ttk.Label(
            self,
            textvariable=DynamicTemplate("{} | {}", self.private_ip, self.public_ip),
        )
        self.address_display.grid(row=0, column=1)

        self.downstream_speed = tk.DoubleVar()
        self.upstream_speed = tk.DoubleVar()

        self.speed_display = ttk.Label(
            self,
            textvariable=DynamicTemplate(
                "Downstream: {:.2f} | Upstream: {:.2f}",
                self.downstream_speed,
                self.upstream_speed,
            ),
        )
        self.speed_display.grid(row=0, column=2, sticky="e")

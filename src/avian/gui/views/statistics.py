import tkinter as tk
from tkinter import ttk

from src.avian.gui.misc.dynamic_template import DynamicTemplate


class Statistics(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.configure(padx=10, pady=5)

        self.columnconfigure(0, weight=1, uniform="x")
        self.columnconfigure(1, weight=1, uniform="x")
        self.columnconfigure(2, weight=1, uniform="x")
        self.rowconfigure(0)

        self.active_transactions = tk.IntVar(value=0)
        self.active_peers = tk.IntVar(value=0)

        ttk.Label(
            self,
            textvariable=DynamicTemplate(
                "{} active transaction(s) via {} peer(s)",
                self.active_transactions, self.active_peers
            )
        ).grid(row=0, column=0, sticky="w")

        self.address_private = tk.StringVar(value="127.0.0.1")
        self.address_public = tk.StringVar(value="127.0.0.1")

        ttk.Label(
            self,
            textvariable=DynamicTemplate(
                "{} | {}",
                self.address_private, self.address_public
            )
        ).grid(row=0, column=1)

        self.downstream_speed = tk.DoubleVar(value=0.0)
        self.upstream_speed = tk.DoubleVar(value=0.0)

        ttk.Label(
            self,
            textvariable=DynamicTemplate(
                "Downstream: {:.2f} | Upstream: {:.2f}",
                self.downstream_speed, self.upstream_speed
            )
        ).grid(row=0, column=2, sticky="e")

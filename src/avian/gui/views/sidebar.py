import tkinter as tk
from tkinter import ttk

from avian.models import Channel
from avian.models.messages import Message


class Sidebar(tk.Frame):
    def __init__(self, master, incoming: Channel[Message], outgoing: Channel[Message]):
        super().__init__(master)

        self.incoming = incoming
        self.outgoing = outgoing

        self.configure(padx=50, pady=10)

        ttk.Label(self, text="test").grid()

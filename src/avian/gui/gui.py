import tkinter as tk

from avian.models.event_bus import EventBus
from src.avian.gui.views import Mainframe, Sidebar, Statistics
from src.avian.gui.views.toolbar import Toolbar


class GUI(tk.Tk):
    def __init__(self, bus: EventBus) -> None:
        super().__init__()
        self.bus = bus

        self.title("Avian - Peer-to-peer file transfers")

        self.geometry("900x500")
        self.minsize(900, 500)
        self.protocol("WM_DELETE_WINDOW", self.handle_close)

        self.rowconfigure(0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2)
        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)

        self.toolbar = Toolbar(self)
        self.toolbar.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=1, column=0, sticky="nsew")

        self.mainframe = Mainframe(self)
        self.mainframe.grid(row=1, column=1, sticky="nsew")

        self.statistics = Statistics(self)
        self.statistics.grid(row=2, column=0, columnspan=2, sticky="nsew")

    def handle_close(self) -> None:
        self.destroy()

    def run(self) -> None:
        self.mainloop()

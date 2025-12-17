import threading
import tkinter as tk

from src.avian.gui.menubar import Menubar
from src.avian.gui.views import Mainframe
from src.avian.gui.views import Sidebar
from src.avian.gui.views import Statistics


class App(tk.Tk):
    def __init__(self, terminate: threading.Event) -> None:
        super().__init__()
        self.terminate = terminate

        self.title("Avian - Peer-to-peer file transfers")
        self.geometry("900x500")
        self.minsize(1200, 650)
        self.protocol("WM_DELETE_WINDOW", self.handle_close)
        self.configure(menu=Menubar(self))

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1)
        self.columnconfigure(0)
        self.columnconfigure(1, weight=1)

        self.sidebar = Sidebar(self)
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.mainframe = Mainframe(self)
        self.mainframe.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.statistics = Statistics(self)
        self.statistics.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew"
        )


    def handle_close(self) -> None:
        self.terminate.set()
        self.destroy()

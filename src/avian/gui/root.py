import tkinter as tk

from src.avian.gui.views.statistics import Statistics
from src.avian.gui.views.sidebar import Sidebar
from src.avian.models.app_context import AppContext


class App(tk.Tk):
    def __init__(self, ctx: AppContext) -> None:
        super().__init__()
        self.ctx = ctx
        self.title("Avian - Peer-to-peer file transfers")
        self.geometry("900x500")
        self.minsize(1200, 650)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=4)

        # tk.Frame(gui, bg="#000000")

        self.sidebar = Sidebar(self)
        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"

        )
        self.mainframe = tk.Frame(self, bg="gray")
        self.mainframe.grid(
            row=0,
            column=1,
            sticky="nsew"

        )
        self.statistics = Statistics(self, ctx)
        self.statistics.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew"
        )


    def handle_close(self) -> None:
        self.ctx.termination_event.set()
        self.destroy()

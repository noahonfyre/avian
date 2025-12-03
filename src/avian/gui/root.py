import tkinter as tk

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

        sidebar = Sidebar(self)
        sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"

        )
        mainframe = tk.Frame(self, bg="gray")
        mainframe.grid(
            row=0,
            column=1,
            sticky="nsew"

        )
        statistics = tk.Frame(self, bg="blue", height=50)
        statistics.grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

        statistics.rowconfigure(0)
        statistics.columnconfigure(0, weight=1)
        statistics.columnconfigure(1, weight=1)

        active_connections_wrapper = tk.Frame(statistics, bg="red")
        active_connections_wrapper.grid(
            row=0,
            column=0,
            sticky="nsew"
        )
        active_connections = tk.Label(active_connections_wrapper, text="Hallo")
        active_connections.pack(anchor="w")

        speed_display_wrapper = tk.Frame(statistics, bg="green")
        speed_display_wrapper.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        speed_display = tk.Label(speed_display_wrapper, text="Hallo")
        speed_display.pack(anchor="e")

        self.mainloop()

    def handle_close(self) -> None:
        self.ctx.termination_event.set()
        self.destroy()

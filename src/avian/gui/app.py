import tkinter as tk
from multiprocessing import Queue
from typing import Callable

from src.avian.gui.menubar import Menubar


class App(tk.Tk):
    def __init__(self, q: Queue) -> None:
        super().__init__()

        self.q = q
        self.message = tk.StringVar()

        self.title("Avian - Peer-to-peer file transfers")
        self.geometry("1200x600")
        self.minsize(1200, 600)

        self.protocol("WM_DELETE_WINDOW", self.handle_close)
        self.config(menu=Menubar(self))

        self.button = tk.Button(self, textvariable=self.message)
        self.button.pack()

        self.schedule(250, self.poll)

        self.entry = tk.Entry()
        self.entry.pack()

    def handle_close(self) -> None:
        self.destroy()

    def schedule(self, repeat_ms: int, func: Callable, *args) -> None:
        def wrapper(*wrapper_args):
            func(*wrapper_args)
            self.after(repeat_ms, wrapper, *wrapper_args)

        self.after(repeat_ms, wrapper, *args)


    def poll(self) -> None:
        if self.q.empty():
            return

        message = self.q.get()["type"]
        if message:
            self.message.set(message)

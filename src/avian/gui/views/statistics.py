import queue
import random
import tkinter as tk
from src.avian.models.app_context import AppContext

class Statistics(tk.Frame):
    def __init__(self, master: tk.Tk, ctx: AppContext):
        super().__init__(master)
        self.rowconfigure(0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.active_connections_wrapper = tk.Frame(self, bg="red")
        self.active_connections_wrapper.grid(
            row=0,
            column=0,
            sticky="nsew"
        )
        
        self.active_connections_var = tk.StringVar()
        self.active_connections_var.set(f"Active connection(s): {str(2)}")
        
        self.active_connections = tk.Label(self.active_connections_wrapper, textvariable=self.active_connections_var)
        self.active_connections.pack(anchor="w")

        self.speed_display_wrapper = tk.Frame(self, bg="green")
        self.speed_display_wrapper.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.speed_display_var = tk.StringVar()
        self.speed_display_var.set(f"{str(1)} | {str(2)}")

        self.speed_display = tk.Label(self.speed_display_wrapper, textvariable=self.speed_display_var)
        self.speed_display.pack(anchor="e")
        self.after(250, lambda: self.poll_data(ctx.chan))

    def poll_data(self, chan: queue.Queue):
        chan.put({"speed": random.randint(1, 67), "connection_count": random.randint(0, 10)})
        
        if not chan.empty():
            item = chan.get()
            if (not "speed" in item) and (not "connection_count" in item):
                self.after(250, lambda: self.poll_data(chan))
                return
            s = item["speed"]
            conns = item["connection_count"]
            self.active_connections_var.set(f"{s} | {str(2)}")
            self.active_connections_var.set(f"Active connection(s): {conns}")
        self.after(250, lambda: self.poll_data(chan))




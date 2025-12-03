import tkinter as tk

class Statistics(tk.Frame):
    def __init__(self, master: tk.Tk):
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
        self.active_connections = tk.Label(self.active_connections_wrapper, text="Hallo")
        self.active_connections.pack(anchor="w")

        self.speed_display_wrapper = tk.Frame(self, bg="green")
        self.speed_display_wrapper.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.speed_display = tk.Label(self.speed_display_wrapper, text="Hallo")
        self.speed_display.pack(anchor="e")
        
        download_speed_var = tk.StringVar(str(20))
        download_speed = tk.Label(self.speed_display, text_variable=download_speed_var)
        
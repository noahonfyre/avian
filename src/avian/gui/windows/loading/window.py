import random
import tkinter as tk
from tkinter import ttk


class LoadingWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("250x100")
        self.minsize(250, 100)
        self.title("Connecting...")
        self.transient(parent)
        self.grab_set()

        self.configure(padx=5, pady=5)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1)

        self.cancel_button = ttk.Button(self, text="Cancel", command=self.close)
        self.cancel_button.grid(column=0, row=1, sticky="se")

        self.progress_var = tk.IntVar()

        self.loadingbar = ttk.Progressbar(
            self,
            orient="horizontal",
            mode="determinate",
            maximum=100,
            variable=self.progress_var,
        )
        self.loadingbar.grid(column=0, row=0, sticky="ew")

        value_label = ttk.Label(self, textvariable=self.progress_var)
        value_label.grid(column=0, row=1, sticky="sw")

        self.after(250, lambda: self.progress(random.randint(1, 100)))

    def progress(self, progress: int):
        if self.progress_var.get() < 100:
            self.progress_var.set(progress)

    def close(self):
        self.destroy()

import tkinter as tk
from tkinter import ttk

class LoadingWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry("400x250")
        self.minsize(400, 250)
        self.transient(parent)
        self.grab_set()

        self.configure(padx=5, pady=5)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.cancel_button = ttk.Button(self, text="Cancel")
        self.cancel_button.grid(column=0, row=2, sticky="se")

        self.loadingbar = ttk.Progressbar(self, orient= "horizontal", mode="determinate",length=300)
        self.loadingbar.grid(column=1, row=1)

        self.progress_step_var = tk.StringVar()
    
        value_label = ttk.Label(self, textvariable=self.progress_step_var)
        value_label.grid(column=2, row=1)   
        
             
    def progress(self, progress: int):
        current_progress = self.loadingbar.value
        if current_progress < 100:
            self.loadingbar.value = progress


    def close(self):
        self.destroy()
import tkinter as tk
from tkinter import ttk

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        notebook = ttk.Notebook(parent)
        notebook.pack(pady=10, expand=True)


        frame1 = ttk.Frame(notebook, width=400, height=280)
        frame2 = ttk.Frame(notebook, width=400, height=280)
        frame3 = ttk.Frame(notebook, width=400, height=280)

        frame1.pack(fill= "both", expand=True)
        frame2.pack(fill= "both", expand=True)
        frame3.pack(fill= "both", expand=True)

        notebook.add(frame1, text = "General")
        notebook.add(frame2, text = "Download")
        notebook.add(frame3, text = "Upload")

        tk.Label(text="Test").grid(frame1)
        tk.Label(text="Download Speed").grid(frame2)
        

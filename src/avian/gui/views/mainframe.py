import tkinter as tk
from tkinter import ttk


class Mainframe(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1)

        self.treeview = ttk.Treeview(self, columns=("Size", "Progress", "Status", "Speed", "Health", "ETA"))
        self.vertical_scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.treeview.yview)
        self.horizontal_scrollbar = ttk.Scrollbar(self, orient="horizontal", command=self.treeview.xview)
        self.treeview.configure(yscrollcommand=self.vertical_scrollbar.set)
        self.treeview.configure(xscrollcommand=self.horizontal_scrollbar.set)

        self.treeview.heading("#0", text="File name")
        self.treeview.heading("Size", text="Size")
        self.treeview.heading("Progress", text="Progress")
        self.treeview.heading("Status", text="Status")
        self.treeview.heading("Speed", text="Speed")
        self.treeview.heading("Health", text="Health")
        self.treeview.heading("ETA", text="ETA")

        self.treeview.column("#0", width=200)
        self.treeview.column("Size", width=1)
        self.treeview.column("Progress", width=1)
        self.treeview.column("Status", width=1)
        self.treeview.column("Speed", width=1)
        self.treeview.column("Health", width=1)
        self.treeview.column("ETA", width=1)

        self.treeview.grid(row=0, column=0, sticky="nsew")
        self.vertical_scrollbar.grid(row=0, column=1, sticky="nsew")
        self.horizontal_scrollbar.grid(row=1, column=0, sticky="nsew")

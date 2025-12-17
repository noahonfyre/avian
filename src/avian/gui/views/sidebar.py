import tkinter as tk
from tkinter import ttk

from src.avian.gui.windows.connection import ConnectionWindow


class Sidebar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(padx=50, pady=10)

        # Für Enrico: (Bitte Kommentare nach Ausführung löschen)
        # StringVar erstellen
        # tkinter Entry
        # Entry self hinzufügen
        # Entry wert der StringVar zuweisen

        self.connect_button = ttk.Button(
            self,
            text="Connect to peer",
            command=lambda: ConnectionWindow(self)
        )
        self.connect_button.pack(expand=True)

         
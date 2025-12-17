import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

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

        self.open_button = ttk.Button(
            self,
            text="Open a File ",
            command=self.select_file
        )
        self.open_button.pack(expand=True)

        self.connect_button = ttk.Button(
            self,
            text="Connect to peer",
            command=lambda: ConnectionWindow(self)
        )
        self.connect_button.pack(expand=True)

    @staticmethod
    def select_file():
        filetypes = {
            ("All files", "*.*")
        }
        filename = fd.askopenfilename(title="open a file", filetypes=filetypes)
        showinfo(title="selected a file", message=filename)

         
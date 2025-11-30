import tkinter as tk
from tkinter import messagebox

from src.avian.gui.menubar.file import FileMenu


class Menubar(tk.Menu):
    def __init__(self, master):
        super().__init__(master)
        test_message = lambda: messagebox.showinfo("This is a message", "This is a message")

        self.file_menu = FileMenu(self)
        self.edit_menu = tk.Menu(self, tearoff=False)
        self.view_menu = tk.Menu(self, tearoff=False)
        self.help_menu = tk.Menu(self, tearoff=False)

        self.add_cascade(label="File", menu=self.file_menu)
        self.add_cascade(label="Edit", menu=self.edit_menu)
        self.add_cascade(label="View", menu=self.view_menu)
        self.add_cascade(label="Help", menu=self.help_menu)



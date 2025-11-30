import tkinter as tk
from tkinter import messagebox


class FileMenu(tk.Menu):
    def __init__(self, master):
        super().__init__(master, tearoff=False)

        test_message = lambda: messagebox.showinfo("This is a message", "This is a message")

        self.add_command(label="Transfer file(s)", command=test_message)
        self.add_command(label="Show received files", command=test_message)
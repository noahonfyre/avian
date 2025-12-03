import tkinter as tk
from tkinter import filedialog as fd
class Sidebar(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        def select_file(): 
            filetypes = ("All files","*.*")
            filename = fd.askopenfilname(
                title="open a file "
                initialder= "/"
                filtypes=filtypes
            )
            showinfo(
                title="selected a file"
                message=filename 
        
          )
            open_button =tk.Button(
                text="Open a File "
                command= select_file
            )
            open_button(expand=True)

            self.mainloop ()

         
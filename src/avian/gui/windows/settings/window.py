import tkinter as tk
from tkinter import ttk

class SettingsWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        notebook = ttk.Notebook(self)
        notebook.grid(pady=10)


        frame1 = ttk.Frame(notebook, width=400, height=280)
        frame2 = ttk.Frame(notebook, width=400, height=280)
        frame3 = ttk.Frame(notebook, width=400, height=280)

        frame1.grid(sticky="nswe")
        frame2.grid(sticky="nswe")
        frame3.grid(sticky="nswe")
        
        notebook.add(frame1, text = "General")
        notebook.add(frame2, text = "Download")
        notebook.add(frame3, text = "Upload")

        tk.Label(text="Test").grid(frame1)
        tk.Label(text="Download Speed").grid(frame2)
        
        tk.Label(frame1, text="").grid(row=0)
        tk.Label(frame2, text="").grid(row=0)
        tk.Label(frame3, text="").grid(row=0)

        spin_number = ttk.Spinbox(frame1)
        spin_number.grid()
        spin_number = ttk.Spinbox(frame2)
        spin_number.grid()
        spin_number = ttk.Spinbox(frame3)
        spin_number.grid()

        var1 = tk.IntVar()
        c1 = tk.Checkbutton(frame1,text="",variable=var1, onvalue=1, offvalue=0)
        c1.grid()
        var1 = tk.IntVar()
        c1 = tk.Checkbutton(frame2,text="",variable=var1, onvalue=1, offvalue=0)
        c1.grid()
        var1 = tk.IntVar()
        c1 = tk.Checkbutton(frame3,text="",variable=var1, onvalue=1, offvalue=0)
        c1.grid()

        n = tk.StringVar()
        selection = ttk.Combobox(frame1, width=27, textvariable=n)

        selection["values"]=("1",
                             "2",
                             "3")
        selection.grid(column=1, row=5)
        n = tk.StringVar()
        selection = ttk.Combobox(frame2, width=27, textvariable=n)

        selection["values"]=("1",
                             "2",
                             "3")
        selection.grid(column=1, row=5)
        n = tk.StringVar()
        selection = ttk.Combobox(frame3, width=27, textvariable=n)

        selection["values"]=("1",
                             "2",
                             "3")
        selection.grid(column=1, row=5)

        scale = ttk.Scale(frame1,orient="horizontal", length=200, from_=1, to=100)
        scale = ttk.Scale(frame2,orient="horizontal", length=200, from_=1, to=100)
        scale = ttk.Scale(frame3,orient="horizontal", length=200, from_=1, to=100)

        v = tk.IntVar()
        tk.Radiobutton(frame1, text="1", padx=20, variable=v, value=1)
        tk.Radiobutton(frame1, text="2", padx=20, variable=v, value=2)
        tk.Radiobutton(frame1, text="3", padx=20, variable=v, value=3)
        v = tk.IntVar()
        tk.Radiobutton(frame2, text="", padx=20, variable=v, value=1)
        tk.Radiobutton(frame2, text="", padx=20, variable=v, value=2)
        tk.Radiobutton(frame2, text="", padx=20, variable=v, value=3)
        v = tk.IntVar()
        tk.Radiobutton(frame3, text="", padx=20, variable=v, value=1)
        tk.Radiobutton(frame3, text="", padx=20, variable=v, value=2)
        tk.Radiobutton(frame3, text="", padx=20, variable=v, value=3)



   
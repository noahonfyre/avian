import tkinter as tk
gui = tk.Tk()
gui.title("Avian - Peer-to-peer file transfers")
gui.geometry("900x500")
gui.minsize(1200,650)
gui.rowconfigure(0, weight=1)
gui.rowconfigure(1)
gui.columnconfigure(0, weight=1)
gui.columnconfigure(1, weight=4)

sidebar = tk.Frame(gui, bg="#000000")
sidebar.grid(
    row=0, 
    column=0,
    sticky="nsew"
    
)
mainframe = tk.Frame(gui, bg="gray")
mainframe.grid(
    row=0,
    column=1,
    sticky="nsew"

)
statistics = tk.Frame(gui, bg="blue", height=50)
statistics.grid(
    row=1,
    column=0,
    columnspan=2,
    sticky="nsew"
)
gui.mainloop()
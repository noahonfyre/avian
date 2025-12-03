#https://www.pythonguis.com/tutorials/create-ui-with-tkinter-grid-layout-manager/

#hälfte des Fensters ist 600 Pixel 



import tkinter as tk

from gui.views.sidebar import Sidebar
gui = tk.Tk()
gui.title("Avian - Peer-to-peer file transfers")
gui.geometry("900x500")
gui.minsize(1200,650)
gui.rowconfigure(0, weight=1)
gui.rowconfigure(1)
gui.columnconfigure(0, weight=1)
gui.columnconfigure(1, weight=4)

# tk.Frame(gui, bg="#000000")

sidebar = Sidebar(gui)
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

statistics.rowconfigure(0)
statistics.columnconfigure(0, weight=1)
statistics.columnconfigure(1, weight=1)


active_connections_wrapper = tk.Frame(statistics, bg="red")
active_connections_wrapper.grid(
    row=0,
    column=0,
    sticky="nsew"
)
active_connections = tk.Label(active_connections_wrapper, text="Hallo")
active_connections.pack(anchor="w")

speed_display_wrapper = tk.Frame(statistics, bg="green")
speed_display_wrapper.grid(
    row=0,
    column=1,
    sticky="nsew"
)

speed_display = tk.Label(speed_display_wrapper, text="Hallo")
speed_display.pack(anchor="e")

gui.mainloop()
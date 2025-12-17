import tkinter as tk
from tkinter import ttk

from src.avian.gui.misc.dynamic_template import DynamicTemplate


class Statistics(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master)
        self.configure(padx=10, pady=5)

        # Für Luca: (Bitte Kommentare nach Ausführung löschen)
        # Nur beim ersten und dritten column konfigurieren, das mittlere soll den rest des platzes für sich beanspruchen
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0)

        # Alles hierunter umwandeln zu drei labels (keine wrapper mehr); bitte variablen und templates stehen lassen
        # Die drei label elemente ihrer jeweiligen column zuweisen und sticky-wert angeben (Tipp: mittleres Element muss nicht sticky sein)
        #
        # Für das neue, mittlere label zwei neue Variablen (beide StringVar) erstellen, eine für die private ip, eine für die public ip
        # Durch "|" getrennt in dem label erscheinen lassen (Tipp: Benutze `DynamicTemplate` und gebe einen template string an)
        
        self.active_transactions = tk.IntVar()
        self.active_peers = tk.IntVar()
        
        self.active_connections = ttk.Label(
            self,
            textvariable=DynamicTemplate("{} active transaction(s) via {} peer(s)", self.active_transactions, self.active_peers)
        )
        self.active_connections.grid(
            row=0,
            column=0,
            sticky="w"
        )

        self.address_display = ttk.Label(
        self,
        text="hallo"
        )

        self.address_display.grid(
            row=0,
            column=1,
            

        )






        

        self.downstream_speed = tk.DoubleVar()
        self.upstream_speed = tk.DoubleVar()

        self.speed_display = ttk.Label(
            self,
            textvariable=DynamicTemplate("Downstream: {:.2f} | Upstream: {:.2f}", self.downstream_speed, self.upstream_speed)
        )
        self.speed_display.grid(
            row=0,
            column=2,
            sticky="e"
        )

import random
import threading
import time

from src.avian.gui import App


class Controller:
    def __init__(self, view: App, terminate: threading.Event) -> None:
        dl1 = view.mainframe.treeview.insert("", "end", text="Fortnite.exe")

        dl2 = view.mainframe.treeview.insert("", "end", text="Among-Us-Guide.pdf")

        while not terminate.is_set():
            view.statistics.active_transactions.set(random.randint(1, 100))
            view.statistics.active_peers.set(random.randint(1, 100))

            view.statistics.downstream_speed.set(random.random() * random.randint(1, 100))
            view.statistics.upstream_speed.set(random.random() * random.randint(1, 100))

            view.mainframe.treeview.item(
                dl1,
                text="Fortnite.exe",
                values=(
                    f"{random.random()*100:.2f} GiB",
                    f"{random.randint(1, 100)}%",
                    "Active",
                    f"{random.random()*100:.2f} MiB/s",
                    f"{random.randint(1, 100)}ms | Good",
                    f"{random.randint(1,5)}h {random.randint(1,60)}min {random.randint(1,60)}s"
                )
            )

            view.mainframe.treeview.item(
                dl2,
                text="Among-Us-Guide.pdf",
                values=(
                    f"{random.random()*100:.2f} GiB",
                    f"{random.randint(1, 100)}%",
                    "Active",
                    f"{random.random()*100:.2f} MiB/s",
                    f"{random.randint(1, 100)}ms | Good",
                    f"{random.randint(1,5)}h {random.randint(1,60)}min {random.randint(1,60)}s"
                )
            )

            time.sleep(0.5)
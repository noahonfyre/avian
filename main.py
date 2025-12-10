from queue import Queue
from threading import Thread, Event
from tkinter import messagebox

from src.avian.config import Config
from src.avian.core import Controller
from src.avian.models import AppContext
from src.avian.gui import App


def main() -> None:
    try:
        config: Config = Config()
        chan: Queue = Queue()
        termination_event: Event = Event()

        ctx = AppContext(config=config, chan=chan, termination_event=termination_event)

        controller_thread: Thread = Thread(target=Controller, args=(ctx,))
        controller_thread.start()

        app = App(ctx)
        app.mainloop()

        controller_thread.join()
    except Exception as e:
        print(e)
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

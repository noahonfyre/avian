import threading
import traceback
from threading import Thread
from tkinter import messagebox

from src.avian.core import Controller
from src.avian.gui import App


def main() -> None:
    terminate = threading.Event()

    try:
        app: App = App(terminate)
        controller_thread: Thread = Thread(target=Controller, args=(app,terminate))

        controller_thread.start()
        app.mainloop()

        if not terminate.is_set():
            terminate.set()

        controller_thread.join()
    except Exception as e:
        # TODO: add better error handling
        traceback.print_exception(type(e), e, e.__traceback__)


if __name__ == "__main__":
    main()

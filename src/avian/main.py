from queue import Queue
from threading import Thread

from src.avian.core import Orchestrator
from src.avian.gui import App


def main() -> None:
    try:
        communicator: Queue = Queue()

        orchestrator_thread: Thread = Thread(target=Orchestrator, args=(communicator,))
        orchestrator_thread.start()

        app = App(communicator)
        app.mainloop()

        orchestrator_thread.join()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

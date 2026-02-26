import threading
from concurrent.futures import ThreadPoolExecutor

from avian.models import Channel
from avian.models.messages import Message


class Bootstrap(threading.Thread):
    def __init__(self, incoming: Channel[Message], outgoing: Channel[Message]):
        super().__init__()
        self.incoming = incoming
        self.outgoing = outgoing

    def run(self):
        with ThreadPoolExecutor(max_workers=5) as executor:
            pass

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.join()

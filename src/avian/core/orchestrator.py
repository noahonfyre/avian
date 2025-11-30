import sys
import time
from multiprocessing import Queue


class Orchestrator:
    def __init__(self, q: Queue) -> None:
        messages = ["test", "orchestrator", sys.winver]

        for i in range(25):
            for message in messages:
                q.put({"type": message})
                time.sleep(0.75)

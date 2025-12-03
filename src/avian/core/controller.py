import sys
import threading
import time

from src.avian.models import AppContext


class Controller:
    def __init__(self, ctx: AppContext) -> None:
        messages = ["hello world", "test", "foo", sys.argv, "bar", f"t-{threading.current_thread().name}"]

        while not ctx.termination_event.is_set():
            for message in messages:
                ctx.chan.put({"type": message})
                time.sleep(1)

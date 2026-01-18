import queue
from enum import Enum

from avian.models.messages import Message


class EventBus:
    def __init__(self) -> None:
        self.view_bound: queue.Queue[Message] = queue.Queue[Message]()
        self.controller_bound: queue.Queue[Message] = queue.Queue[Message]()

    class Destination(Enum):
        BOTH = 0
        VIEW_BOUND = 1
        CONTROLLER_BOUND = 2

    def emit(self, msg: Message, dest: Destination = Destination.BOTH) -> None:
        if dest == EventBus.Destination.BOTH:
            self.view_bound.put(msg)
            self.controller_bound.put(msg)
        elif dest == EventBus.Destination.VIEW_BOUND:
            self.view_bound.put(msg)
        elif dest == EventBus.Destination.CONTROLLER_BOUND:
            self.controller_bound.put(msg)
        else:
            raise NotImplementedError

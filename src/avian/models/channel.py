import threading
from collections import deque
from typing import Deque, Generic, Optional, Type, TypeVar

from avian.models.exceptions import ChannelClosed

T = TypeVar("T")


class Channel(Generic[T]):
    """
    A thread-safe Channel object that can carry messages of type `T`.
    """

    def __init__(self, chan_type: Type[T], buffer_size: int = 0):
        self.chan_type = chan_type
        self.buffer_size: int = buffer_size
        self.buffer: Deque[T] = deque[T]()
        self.closed: bool = False

        self.sync: threading.Condition = threading.Condition()

    def is_full(self) -> bool:
        """
        Helper function to check if the channel's internal buffer is full.
        """
        if self.buffer_size < 0:
            return False
        else:
            return 0 < self.buffer_size <= len(self.buffer)

    def send(self, value: T) -> None:
        """
        Puts a message of type `T` into the channel's buffer which can be read by `Channel.recv()`.
        """

        with self.sync:
            while self.is_full():
                self.sync.wait()

            if self.closed:
                raise ChannelClosed(
                    "unable to send messages on a closed channel object."
                )

            self.buffer.append(value)
            self.sync.notify_all()

    def recv(self) -> Optional[T]:
        """
        Reads a message from the channel's buffer.
        """

        with self.sync:
            while len(self.buffer) == 0:
                if self.closed:
                    return None
                self.sync.wait()

            value: T = self.buffer.popleft()
            self.sync.notify_all()
            return value

    def close(self) -> None:
        """
        Closes the channel, preventing future writes to the buffer.
        """
        with self.sync:
            self.closed = True
            self.sync.notify_all()

    def __iter__(self) -> "Channel[T]":
        return self

    def __next__(self) -> Optional[T]:
        value: Optional[T] = self.recv()
        if value is None:
            raise StopIteration
        return value

    def __repr__(self):
        return f"<Channel(buffer_size={self.buffer_size}, buffer_len={len(self.buffer)}, closed={self.closed})>"

from abc import ABC, abstractmethod


class Service(ABC):
    """
    Abstract base class for service implementations.
    """

    @abstractmethod
    def run(self):
        """
        Abstract method which has to be overridden with the main service functionality.
        """
        pass

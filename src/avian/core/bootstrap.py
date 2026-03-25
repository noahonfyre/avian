import threading
from pathlib import Path

from avian.models.channel import Channel
from avian.models.config.config import Config
from avian.models.constants import LOGGER, RESOLVER_TARGET
from avian.models.messages import Message, Shutdown, StartSender
from avian.services.receiver_service import ReceiverService
from avian.services.resolver_service import ResolverService
from avian.services.sender_service import SenderService
from avian.services.service import Service


class Bootstrap(threading.Thread):
    """
    The secondary application thread for orchestrating threads.
    Also carries the backend event loop.
    """

    def __init__(self, incoming: Channel[Message], outgoing: Channel[Message]) -> None:
        super().__init__()
        self.incoming = incoming
        self.outgoing = outgoing

    def run(self):
        threading.Thread(
            target=run_service,
            args=(
                ReceiverService(
                    self.outgoing,
                    Path(Config.SAVE_PATH.get()),
                    Config.PROTOCOL_PORT.get(),
                ),
            ),
            daemon=True,
        ).start()

        threading.Thread(
            target=run_service,
            args=(ResolverService(self.outgoing, RESOLVER_TARGET),),
            daemon=True,
        ).start()

        for msg in self.incoming:
            # TODO: change if-elif branching to a more dynamic solution
            if isinstance(msg, StartSender):
                threading.Thread(
                    target=run_service,
                    args=(
                        SenderService(self.outgoing, msg.files, msg.address, msg.port),
                    ),
                    daemon=True,
                ).start()
            elif isinstance(msg, Shutdown):
                LOGGER.info("Received SHUTDOWN signal.")
                break

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.join()


def run_service(service: Service) -> None:
    """
    Helper function for starting services via thread targets more organized.
    """

    service.run()

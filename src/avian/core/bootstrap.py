import threading

from avian.models.channel import Channel
from avian.models.constants import LOGGER, PROTOCOL_PORT, SAVE_PATH
from avian.models.messages import Message, Shutdown, StartSender
from avian.services.receiver_service import ReceiverService
from avian.services.sender_service import SenderService
from avian.services.service import Service


class Bootstrap(threading.Thread):
    def __init__(self, incoming: Channel[Message], outgoing: Channel[Message]):
        super().__init__()
        self.incoming = incoming
        self.outgoing = outgoing

    def run(self):
        # TODO: change hardcoded values to dynamic values from config
        threading.Thread(
            target=run_service,
            args=(ReceiverService(self.outgoing, SAVE_PATH, PROTOCOL_PORT),),
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
    service.run()

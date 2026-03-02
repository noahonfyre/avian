import threading
from pathlib import Path

from avian.models import Channel
from avian.models.constants import SAVE_PATH
from avian.models.messages import Message
from avian.services.receiver_service import ReceiverService
from avian.services.sender_service import SenderService
from avian.services.service import Service


class Bootstrap(threading.Thread):
    def __init__(self, incoming: Channel[Message], outgoing: Channel[Message]):
        super().__init__()
        self.incoming = incoming
        self.outgoing = outgoing

    def run(self):
        # TODO: change hardcoded values to dynamic inputs
        threading.Thread(
            target=run_service,
            args=(ReceiverService(self.outgoing, SAVE_PATH, 23500),),
            daemon=True,
        ).start()

        # TODO: change hardcoded values to dynamic inputs
        threading.Thread(
            target=run_service,
            args=(
                SenderService(
                    self.outgoing,
                    [Path("C:\\Users\\Noah\\Downloads\\20260128 121019.gif")],
                    "127.0.0.1",
                    23500,
                ),
            ),
            daemon=True,
        ).start()

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.join()


def run_service(service: Service) -> None:
    service.run()

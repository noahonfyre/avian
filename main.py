import logging
import signal
import sys
import traceback

from avian.core.bootstrap import Bootstrap
from avian.gui.gui import GUI
from avian.models.channel import Channel
from avian.models.config.config import Config
from avian.models.constants import ID, LOGGER, VERSION
from avian.models.messages import Message

event_channel: Channel[Message] = Channel(Message, -1)
command_channel: Channel[Message] = Channel(Message, -1)


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s",
        datefmt="%H:%M:%S",
    )

    LOGGER.info(f"Initializing {ID} v{VERSION}...")

    Config.register()

    signal.signal(signal.SIGINT, shutdown)
    signal.signal(signal.SIGTERM, shutdown)

    try:
        gui: GUI = GUI(event_channel, command_channel)
        with Bootstrap(command_channel, event_channel):
            gui.run()
    except Exception as e:
        # TODO: add better error handling
        traceback.print_exception(type(e), e, e.__traceback__)

    shutdown(0, None)


def shutdown(signum: int, _) -> None:
    LOGGER.info("Shutdown signal received...")
    LOGGER.info("Shutting down...")

    event_channel.close()
    command_channel.close()

    sys.exit(signum)


if __name__ == "__main__":
    main()

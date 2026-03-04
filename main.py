import logging
import traceback

from avian.core import Bootstrap
from avian.gui.gui import GUI
from avian.models.channel import Channel
from avian.models.constants import ID, LOGGER, PROTOCOL_VERSION, VERSION
from avian.models.messages import Message


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s",
        datefmt="%H:%M:%S",
    )

    LOGGER.info(f"Initializing {ID} v{VERSION}...")

    event_channel: Channel[Message] = Channel(Message, -1)
    command_channel: Channel[Message] = Channel(Message, -1)

    try:
        gui: GUI = GUI(event_channel, command_channel)
        with Bootstrap(command_channel, event_channel):
            gui.run()
    except Exception as e:
        # TODO: add better error handling
        traceback.print_exception(type(e), e, e.__traceback__)

    LOGGER.info("Shutting down...")


if __name__ == "__main__":
    main()

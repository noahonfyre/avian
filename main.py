import traceback

from avian.core.bootstrap import bootstrap
from avian.models.event_bus import EventBus
from avian.gui import GUI


def main() -> None:
    bus: EventBus = EventBus()

    try:
        gui: GUI = GUI(bus)

        bootstrap(bus)
        gui.run()

    except Exception as e:
        # TODO: add better error handling
        traceback.print_exception(type(e), e, e.__traceback__)


if __name__ == "__main__":
    main()

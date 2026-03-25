import json
import socket
import urllib.request

from avian.models.channel import Channel
from avian.models.constants import LOGGER
from avian.models.messages import Message, ResolverUpdate
from avian.services.service import Service


class ResolverService(Service):
    """
    Service for resolving private and public IP addresses.
    Accuracy of the resolved public address can vary based on network configuration and setup.
    Takes in the channel `outgoing` to which updates will be posted and the `resolver_target` HTTP address to which the request will be sent.
    """

    def __init__(self, outgoing: Channel[Message], resolver_target: str) -> None:
        self.outgoing: Channel[Message] = outgoing
        self.resolver_target: str = resolver_target

    def run(self):
        """
        Run the service which will resolve the private and public IP addresses and send a `ResolverUpdate` message to `self.outgoing`.
        """
        LOGGER.info("Resolving private IP address...")
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("192.0.2.1", 80))
            private_ip = sock.getsockname()[0]

        LOGGER.info(f"Private address is {private_ip}.")

        LOGGER.info("Resolving public IP address...")
        with urllib.request.urlopen(self.resolver_target) as res:
            public_ip = json.loads(res.read())["ip"]

        LOGGER.info(f"Public address is {public_ip}.")

        self.outgoing.send(ResolverUpdate(private_ip, public_ip))

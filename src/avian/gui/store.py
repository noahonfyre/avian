from collections import defaultdict
from typing import Optional, List

from attr import dataclass

from avian.gui.views import Statistics
from avian.gui.views.mainframe import Mainframe
from avian.utils.numbers import fmt_bin


@dataclass
class Transaction:
    address: Optional[str] = None
    port: Optional[int] = None
    filename: Optional[str] = None
    transferred: Optional[int] = None
    size: Optional[int] = None
    progress: Optional[float] = None
    status: Optional[str] = None
    speed: Optional[int] = None
    eta: Optional[float] = None


class TransactionStore:
    """
    A class for storing application/transaction data.
    """

    transactions: defaultdict[str, Transaction] = defaultdict(Transaction)
    ip_addresses: List[str] = []

    @classmethod
    def get_transaction_count(cls) -> int:
        """
        Returns the total number of transactions registered.
        """
        return len(cls.transactions.values())

    @classmethod
    def get_downstream(cls) -> int:
        """
        Returns the speed of all downstream transactions in bytes per second.
        """
        i = 0
        for transaction in cls.transactions.values():
            if not transaction.speed:
                continue
            if transaction.address != "127.0.0.1":
                i += transaction.speed
        return i

    @classmethod
    def get_upstream(cls) -> int:
        """
        Returns the speed of all upstream transactions in bytes per second.
        """
        i = 0
        for transaction in cls.transactions.values():
            if not transaction.speed:
                continue
            if transaction.address == "127.0.0.1":
                i += transaction.speed
        return i

    @classmethod
    def push_updates(cls, mainframe: Mainframe, statistics: Statistics) -> None:
        """
        Applies the values stored internally to the defined locations in `mainframe` and `statistics`.
        """

        for value in cls.transactions.values():
            mainframe.update_item(
                address=value.address or "",
                port=value.port or 0,
                filename=value.filename or "",
                size=f"{fmt_bin(value.transferred or 0, 'B')}/{fmt_bin(value.size or 0, 'B')}",
                progress=f"{value.progress or 0:.2%}",
                status=value.status or "",
                speed=fmt_bin(value.speed or 0, "B/s"),
                eta=f"{value.eta or 0:.2f}s",
            )

        statistics.active_transactions.set(cls.get_transaction_count())
        statistics.downstream_speed.set(cls.get_downstream())
        statistics.upstream_speed.set(cls.get_upstream())

        statistics.ip_addresses.set(" | ".join(cls.ip_addresses))

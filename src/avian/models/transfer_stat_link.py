from dataclasses import dataclass


@dataclass
class TransferStatLink:
    progress: float
    speed: float
    eta: float

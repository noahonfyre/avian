class Config:
    # Additional Services
    ENABLE_RENDEZVOUS: bool = False
    RENDEZVOUS_HOST: str = "localhost"
    RENDEZVOUS_PORT: int = 9240

    ENABLE_DISCOVERY: bool = False
    DISCOVERY_PORT: int = 9245

    ENABLE_RESOLUTION: bool = True
    RESOLUTION_HOST: str = "1.1.1.1"
    RESOLUTION_PORT: int = 80

    @classmethod
    def load(cls) -> "Config":
        pass

    @classmethod
    def save(cls) -> "Config":
        pass

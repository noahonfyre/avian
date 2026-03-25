from avian.models.config.night import ConfigField, ConfigSpec
from avian.models.constants import AVIAN_PATH, LOGGER


class Config:
    """
    The application config.
    Has to be accessed as a class, not as an instance.
    """

    SPEC = ConfigSpec(AVIAN_PATH / "config.json")

    PROTOCOL_PORT = SPEC.define(
        ConfigField("protocol_port", 9250, lambda i: 1024 < i < 65_536)
    )
    CHUNK_SIZE = SPEC.define(ConfigField("chunk_size", 4096, lambda i: 0 < i))
    SAVE_PATH = SPEC.define(ConfigField("save_path", str(AVIAN_PATH / "saved")))

    @classmethod
    def register(cls):
        LOGGER.info("Loading config...")
        cls.SPEC.load()

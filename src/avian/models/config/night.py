import json
import os
from pathlib import Path
from typing import Any, Callable, Dict, Generic, Optional, Type, TypeVar

T = TypeVar("T")


class ConfigField(Generic[T]):
    """
    A wrapper for defining updatable fields with the `ConfigSpec` object.
    """

    def __init__(
            self,
            key: str,
            default: T,
            validator: Optional[Callable[[T], bool]] = None,
    ):
        self.key = key
        self.default: T = default
        self.v_type: Type[T] = type(default)
        self.validator: Callable[[T], bool] = validator or self.default_validator

    @staticmethod
    def default_validator(_: Any) -> bool:
        # Instance check is already done in `load()`; Only check other stuff in the validator.
        return True


class ConfigReference(Generic[T]):
    def __init__(self, key: str, config: "ConfigSpec"):
        self.key: str = key
        self.config: ConfigSpec = config

    def set(self, new: T) -> None:
        self.config.dataset[self.key] = new

    def get(self) -> T:
        return self.config.dataset[self.key]


class ConfigSpec(Generic[T]):
    """
    The wrapper of a config.
    Provides functionality for loading and saving the data structure to the file and defining fields.
    """

    def __init__(self, path: Path):
        self.path: Path = path
        self.fields: Dict[str, ConfigField] = {}
        self.dataset: Dict[str, Any] = {}

    def define(self, field: ConfigField[T]) -> ConfigReference[T]:
        """
        Define a config field
        """
        self.fields[field.key] = field
        return ConfigReference(field.key, self)

    def load(self):
        """
        Loads the data of the file at `self.path`, parses it, validates it and applies it to the internal value.
        """

        if not self.path.exists():
            os.makedirs(self.path.parent, exist_ok=True)
            self.save()

        with open(self.path, "r") as file:
            data: Dict[str, Any] = json.load(file)
            for key, field in self.fields.items():
                value = data.get(key, field.default)

                type_mismatch: bool = not isinstance(value, field.v_type)
                validator_mismatch: bool = not field.validator

                if type_mismatch or validator_mismatch:
                    self.dataset[key] = field.default
                    continue

                self.dataset[key] = value

    def save(self):
        """
        Saves the internal data to the file at `self.path`.
        """

        with open(self.path, "w") as file:
            json.dump(self.dataset, file)

    def apply(self):
        self.save()
        self.load()

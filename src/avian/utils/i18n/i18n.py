import json
from pathlib import Path
from typing import Any, Optional

from src.avian.utils.i18n.translations import Translations


class I18n:
    def __init__(self, app_path: str, lang: str):
        self.loaded_translations = Translations()
        path = Path(app_path) / "lang" / (lang + ".json")
        if not path.exists():
            return
        try:
            with path.open("rt") as file:
                data = json.load(file)
                self.loaded_translations = Translations(**data)
        except OSError:
            return

    def translatable(self, key: str, inject: dict[str, Any]) -> str:
        inject = inject or {}

        if not hasattr(self.loaded_translations, key):
            return key

        return getattr(self.loaded_translations, key).format(**inject)

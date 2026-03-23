import tkinter as tk
from typing import Callable


class SupplierTemplate(tk.StringVar):
    """
    A helper class that dynamically recomputes the output on variable update based on the variable values.
    """

    def __init__(self, template: Callable[[...], str], *args: tk.Variable):
        super().__init__()
        self.template = template
        self.args = args

        self.update()

        for a in args:
            a.trace_add("write", self.update)

    def update(self, *_):
        values = [a.get() for a in self.args]
        self.set(self.template(*values))

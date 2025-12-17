import tkinter as tk


class DynamicTemplate(tk.StringVar):
    def __init__(self, template: str, *args: tk.Variable):
        super().__init__()
        self.template = template
        self.args = args

        self.update()

        for a in args:
            a.trace_add("write", self.update)

    def update(self, *_):
        values = [a.get() for a in self.args]
        self.set(self.template.format(*values))

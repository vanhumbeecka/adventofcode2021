
class Entry:
    def __init__(self, name: str):
        self.name = name
        self._next = None
        self.split = False

    def set_next(self, next: "Entry"):
        self._next = next

    def has_next(self):
        return self._next is not None

    def get_next(self):
        return self._next

    def __repr__(self):
        return f"<Entry {self.name} next={self._next.name if self._next else None}>"

    @property
    def pair(self):
        if self._next:
            return self.name + self._next.name
        return None

    def insert_and_return_last(self, entry: "Entry"):
        self.split = True
        last = self._next
        self.set_next(entry)
        entry.set_next(last)
        return last
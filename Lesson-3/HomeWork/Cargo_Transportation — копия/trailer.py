from cargo import Cargo

class Trailer:
    def __init__(self, max_cargo_size :int):
        self._max_cargo_size = max_cargo_size

    def get_max_cargo_size(self):
        return self._max_cargo_size


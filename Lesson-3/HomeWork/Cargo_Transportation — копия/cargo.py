class Cargo:
    def __init__(self,name :str, size: int = 1, dangerous: bool = False):
        self._size = size
        self._dangerous = dangerous
        self._name = name

    def get_size(self):
        return self._size

    def is_dangerous(self):
        return self._dangerous

    def get_name(self):
        return self._name
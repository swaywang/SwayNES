class Register:
    def __init__(self, size):
        self._size = size
        self._value = 0

    def read(self):
        return self._value

    def write(self, value):
        bits = (2 ** self._size) - 1
        self._value = value & bits
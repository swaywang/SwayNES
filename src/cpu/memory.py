class Memory:
    def __init__(self, size):
        self._size = size
        self._memory = [0] * size

    def read(self, address):
        return self._memory[address]

    def write(self, address, value):
        if not self.check_memory_bound(address):
            raise Exception("Memory write out of bounds: {0x:#06x}".format(address))

        self._memory[address] = value

    def check_memory_bound(self, address):
        if address < 0 or address > self._size:
            return False
        return True

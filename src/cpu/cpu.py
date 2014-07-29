import os
import sys
from register import Register

class CPU:
    def _init_CPU_registers(self):
        self.registers = {'pc': Register(16), 'a': Register(8),
                          'x': Register(8), 'y': Register(8),
                          'sp': Register(8), 'p': Register(8)}

        self.registers['pc'].write(0xc000)
        self.registers['a'].write(0x00)
        self.registers['x'].write(0x00)
        self.registers['y'].write(0x00)
        self.registers['sp'].write(0xfd)
        self.registers['p'].write(0x24)

    def __init__(self):
        self._init_CPU_registers()


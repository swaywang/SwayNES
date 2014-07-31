import unittest
import os
import sys

lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from cpu.cpu import CPU

class CPUTestCase(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU()

    def tearDown(self):
        pass

    def test_cpu_registers_init(self):
        self.assertEquals(0xc000, self.cpu.registers["pc"].read())
        self.assertEquals(0x00, self.cpu.registers["a"].read())
        self.assertEquals(0x00, self.cpu.registers["x"].read())
        self.assertEquals(0x00, self.cpu.registers["y"].read())
        self.assertEquals(0xfd, self.cpu.registers["sp"].read())
        self.assertEquals(0x24, self.cpu.registers["p"].read())

    def test_cpu_ram_size(self):
        cpu_memory_len = self.cpu.ram.get_memory_size()
        self.assertEquals(0xFFFF, cpu_memory_len)

if __name__ == '__main__':
    unittest.main()

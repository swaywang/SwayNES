import unittest
import os
import sys

lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from cpu.memory import Memory

class MemoryTestCase(unittest.TestCase):
    def setUp(self):
        self.memory = Memory(0xffff)

    def tearDown(self):
        pass

    def test_write_memory(self):
        self.memory.write(0x1000, 0x55)
        self.assertEquals(self.memory.read(0x1000), 0x55)

    def test_read_memory(self):
        self.memory.write(0x4545, 0x66)
        self.assertEquals(self.memory.read(0x4545), 0x66)

    def write_memory_out_of_bounds(self):
        self.memory.write(0x10000, 0x55)

    def test_write_memory_out_of_bounds(self):
        self.assertRaises(Exception, self.write_memory_out_of_bounds)

if __name__ == '__main__':
    unittest.main()

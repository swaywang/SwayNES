import unittest
import os
import sys

lib_path = os.path.abspath('../')
sys.path.append(lib_path)

from cpu.register import Register
 
class RegisterTestCase(unittest.TestCase):
    def setUp(self):
        pass
 
    def tearDown(self):
        pass
 
    def test_register_write_8bits(self):
        reg = Register(8)
        reg.write(0xff)
        read_value = reg.read()
        self.assertEquals(0xff, read_value)
        
    def test_register_read_8bits(self):
        reg = Register(8)
        read_value = reg.read()
        self.assertEquals(0x00, read_value)
        
        reg.write(0xff)
        read_value = reg.read()
        self.assertEquals(0xff, read_value)
        
    def test_register_write_16bits(self):
        reg = Register(16)
        reg.write(0xffff)
        read_value = reg.read()
        self.assertEquals(0xffff, read_value)
        
    def test_register_read_16bits(self):
        reg = Register(16)
        read_value = reg.read()
        self.assertEquals(0x0000, read_value)
        
        reg.write(0xffff)
        read_value = reg.read()
        self.assertEquals(0xffff, read_value)

if __name__ == '__main__':
    unittest.main()
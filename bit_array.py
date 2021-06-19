import math

BITS_ONE = [0b10000000, 0b01000000, 0b00100000, 
    0b00010000, 0b00001000, 0b00000100, 0b00000010,
    0b00000001
]

BITS_ZERO = [0b01111111, 0b10111111, 0b11011111,
    0b11101111, 0b11110111, 0b11111011, 0b11111101,
    0b11111110
]

def set_bit(byte, bit, index):
    if bit == 1:
        v = BITS_ONE[index]
    if bit == 0:
        v = BITS_ZERO[index]
        return byte & v
    return byte | v

def get_bit(byte, index):
    result = 0
    v = BITS_ONE[index]
    shift = 8 - index - 1
    byte = byte & v
    result = byte >> shift
    return result

class BitArray():
    def __init__(self):
        self.bytes = bytearray(0)
        self.length = 0

    def append(self, v):
        bit_index = self.length % 8
        byte_index = int(math.floor(self.length / 8.0))
        byte = self.bytes[byte_index]
        byte = set_bit(byte, v, bit_index)
        self.bytes[byte_index] = byte
        self.length += 1
    
    def __getitem__(self, index):
        bit_index = index % 8
        byte_index = int(math.floor(index / 8.0))
        byte = self.bytes[byte_index]
        return get_bit(byte, bit_index)
        

    def __setitem__(self, index, v):
        bit_index = index % 8
        byte_index = int(math.floor(index / 8.0))
        byte = self.bytes[byte_index]
        byte = set_bit(byte, v, bit_index)
        self.bytes[byte_index] = byte

    def __len__(self):
        return self.length

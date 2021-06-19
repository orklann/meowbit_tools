import math

def set_bit(byte, bit, index):
    if index == 0:
        if bit == 1:
            v = 0b10000000
        elif bit == 0:
            v = 0b01111111
    elif index == 1:
        if bit == 1:
            v = 0b01000000
        elif bit == 0:
            v = 0b10111111
    elif index == 2:
        if bit == 1:
            v = 0b00100000
        elif bit == 0:
            v = 0b11011111
    elif index == 3:
        if bit == 1:
            v = 0b00010000
        elif bit == 0:
            v = 0b11101111
    elif index == 4:
        if bit == 1:
            v = 0b00001000
        elif bit == 0:
            v = 0b11110111
    elif index == 5:
        if bit == 1:
            v = 0b00000100
        elif bit == 0:
            v = 0b11111011
    elif index == 6:
        if bit == 1:
            v = 0b00000010
        elif bit == 0:
            v = 0b11111101
    elif index == 7:
        if bit == 1:
            v = 0b00000001
        elif bit == 0:
            v = 0b11111110
    if bit == 0:
        return byte & v
    return byte | v

def get_bit(byte, index):
    result = 0
    if index == 0:
        v = 0b10000000
        byte = byte & v
        result = byte >> 7
    elif index == 1:
        v = 0b01000000
        byte = byte & v
        result = byte >> 6
    elif index == 2:
        v = 0b00100000
        byte = byte & v
        result = byte >> 5
    elif index == 3:
        v = 0b00010000
        byte = byte & v
        result = byte >> 4
    elif index == 4:
        v = 0b00001000
        byte = byte & v
        result = byte >> 3
    elif index == 5:
        v = 0b00000100
        byte = byte & v
        result = byte >> 2
    elif index == 6:
        v = 0b00000010
        byte = byte & v
        result = byte >> 1
    elif index == 7:
        v = 0b00000001
        byte = byte & v
        result = byte
    return result

class BitArray():
    def __init__(self):
        self.bytes = bytearray(1)
        self.length = 0

    def append(self, v):
        bit_index = self.length % 8
        byte_index = int(math.floor(self.length / 8.0))
        if byte_index > len(self.bytes) - 1:
            self.bytes.append(0x00)
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

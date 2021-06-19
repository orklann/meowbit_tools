from bit_array import BitArray

b = BitArray()
print("len:", len(b))

for i in range(9):
    b.append(1)

print("len:", len(b))
print("b[0]:", b[0])
print("b[8]", b[8])
b[8] = 0
print("b[8]:", b[8])
b[0] = 0
print("b[0]:", b[0])
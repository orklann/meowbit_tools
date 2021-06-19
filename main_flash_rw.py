from meowbit import screen
from meowbit import pyb
import utime

fl = pyb.Flash()

# 4000th blocks to read and write, as Meowbit has 2MB flash size, 
# it has 1024 * 1024 * 2 / 512 = 4096 blocks
start = 4000

bufr = bytearray(1024) # Every block size is 512
fl.readblocks(start, bufr)

s = "" + str(bufr[0])

screen.text(s)

t1 = utime.ticks_ms()
s = str(t1)
screen.text(s, 50, 40)

buf = bytearray(1024)

buf[0] = bufr[0] + 1
if buf[0] > 255:
    buf[0] = 255

fl.writeblocks(start, buf)
t2 = utime.ticks_ms()

s = str(t2)
screen.text(s, 50, 80)
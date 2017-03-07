#!/usr/bin/python
#-*-coding:UTF-8-*-
import random
import struct
def work():
    #产生一个随机浮点数
    nNum = random.randint(1,10)
    if nNum == 1:
        nValue = random.uniform(0,1)
    elif nNum > 1 and nNum < 10:
        nValue = random.uniform(1,5)
    else:
        nValue = random.uniform(5,6)
    #“HH”以两个字节为分界，把4个字节的str分成了两个unsigned short型,小端存储的整数。
    return struct.unpack('<HH',struct.pack('<f',nValue))


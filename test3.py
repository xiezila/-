#!/usr/bin/python
#-*-coding:UTF-8-*-
import sys
import logging
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import random
import struct
import threading
import time
from test2 import work
logger = modbus_tk.utils.create_logger("console")
master = []
HOSTS = ["QS.station.com", "XQ.station.com", "LZ.station.com", 
         "LX.station.com", "LP.station.com", "XJ.station.com", 
         "BJ.station.com", "ZJ.station.com", "SZK.station.com", 
         "FY.station.com", "TL.station.com", "QI.station.com", 
         "XD.station.com", "BS.station.com", "JD.station.com", 
         "LA.station.com", "JJLFS.station.com", "SJLFS.station.com", 
         "JBFS.station.com", "FYBFS.station.com", "FY1FS.station.com", 
         "FY2FS.station.com", "JZFS.station.com"]
#设置一个定时器
def fun_timer():
    #写寄存器地址为00,02,04的保持寄存器
    for j in master:    
        logger.info(j.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 00000, output_value=work()))
        logger.info(j.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 00002, output_value=work()))
        logger.info(j.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 00004, output_value=work()))
    global timer
    timer = threading.Timer(5.5 , fun_timer)
    timer.start()

if __name__ == "__main__":
    try:
        class Master(object):
            def __init__(self, name):
                self.name = name
        #连接MODBUS TCP从机
        for i in range(23):
            _d = modbus_tcp.TcpMaster(host = HOSTS[i])
            _d.set_timeout(5.0)
            master.append(_d)
        logger.info("connected")
        #第一次1秒后运行定时器
        timer = threading.Timer(1, fun_timer)
        timer.start()
    except modbus_tk.modbus.ModbusError, e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))



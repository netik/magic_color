#!/usr/bin/python

import sys

# Python class to talk to a WF300 LED Controller
#
# I know little about these devices. They are possibly made by a company called Shenzhi
# Which may actually be LSM Lighting (http://www.lsmledlighting.com/)
#

import os 
import time

from socket import *
from Protocol import * 

class Magiccolor:
  DEBUG = False
  _socket = None
  _ip = "192.168.2.2"
  _port = 5000
  _mode = 0 

  def __init__(self,ip="192.168.2.2",port=5000):
    self._socket = None
    self._ip = ip
    self._port = port
    # mode 3 is SPI Mode
    # TODO: Implement other chips
    self._mode = 3

  def connect(self):
    print "trying..."
    self._socket = create_connection((self._ip, self._port), 10)
    print self._socket
    print "connected"

  def sendMsg(self,p):
    # I think based on mode we send the right thing here?
    #print self._socket.send(p.getAll())
    x=0

    if DEBUG:
      for b in p.spi_getAll():
        print "%d - %x" % ( x, b )
        x = x + 1

    print self._socket.send(p.spi_getAll())

m = Magiccolor()
m.connect()

# alright, in keynum 3, keyvalue selects mode. 
# but haalf the lights light. 
#p = Protocol()
#p.keyNum = 3
#x = 1 
#while x<4:
#  p.keyValue = x
#  m.sendMsg(p)
#  time.sleep(1)
#  x=x+1


p = Protocol()
# key number 1 turned it on
# key number 2 turned shit off 
# key #3 selects mode
# We don't know how to set speed or brightness.

#p.keyNum = 3
#p.keyValue = p.findProgram('WHITE')

# this turns things off.
p.keyNum=p.MODE_OFF
m.sendMsg(p)

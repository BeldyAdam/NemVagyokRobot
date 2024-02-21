#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import Feladatok

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
""" ev3 = EV3Brick()
jm = Motor(Port.B)
bm = Motor(Port.C)
km = Motor(Port.A)

# szenzorok
us = UltrasonicSensor(Port.S4)  #UltraSensor
ts = TouchSensor(Port.S1)       #TouchSensor
cs = ColorSensor(Port.S3)       #ColorSensor
gs = GyroSensor(Port.S2)        #GyroSensor """

""" robot = DriveBase(jm, bm, 45, 142) """

#főprogram
oraiMunka = Feladatok.Feladatok()

#oraiMunka.elsoFeladat()
#oraiMunka.masodikFeladat()
#oraiMunka.harmadikFeladat()
#oraiMunka.negyedikFeladat()
#oraiMunka.otodikFeladat()
#oraiMunka.hatodikFeladat()
oraiMunka.fordulas1()


# Write your program here.

#ev3.speaker.beep()
oraiMunka.csipog()

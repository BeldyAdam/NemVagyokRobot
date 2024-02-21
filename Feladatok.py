#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

class Feladatok():

    def __init__(self):
        self.ev3 = EV3Brick()
        #motorok
        self.jm = Motor(Port.B)
        self.bm = Motor(Port.C)
        self.km = Motor(Port.A)
        #szenzorok
        self.us = UltrasonicSensor(Port.S4)  #UltraSensor
        self.ts = TouchSensor(Port.S1)       #TouchSensor
        self.cs = ColorSensor(Port.S3)       #ColorSensor
        self.gs = GyroSensor(Port.S2)        #GyroSensor

        self.robot = DriveBase(self.jm, self.bm, 55, 115)

    def elsoFeladat(self):
        self.robot.straight(300)

    def csipog(self):
        self.ev3.speaker.beep()

    def masodikFeladat(self):
        self.robot.turn(90)

    def harmadikFeladat(self):
        self.robot.straight(300)
        self.robot.straight(-300)
        self.robot.turn(90)
        self.robot.turn(-90)

    def negyedikFeladat(self):
        self.ev3.speaker.set_speech_options('en', 'm2', 100, 400)
        self.ev3.speaker.set_volume(100)
        self.ev3.speaker.say("hey")

    def otodikFeladat(self):
        self.ev3.light.off()
        self.ev3.light.on(BLUE)

    def hatodikFeladat(self):
        self.ev3.speaker.play_file(SoundFile.READY)

    #Fordulások

    def fordulas1(self):
        #run_target(speed, target_angle, then=Stop.HOLD, wait=True)

    def fordulas2(self):
        #run(speed)

    def fordulas3(self):
        #turn(angle)
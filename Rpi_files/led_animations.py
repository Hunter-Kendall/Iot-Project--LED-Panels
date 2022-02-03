#!/usr/bin/env python3
# rpi_ws281x IoT Project

import RPi.GPIO as GPIO
import time
from rpi_ws281x import *
import argparse
import copy
import os
import socket


# LED strip configuration:
LED_COUNT = 89  # Number of LED pixels.
LED_PIN = 18  # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10  # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False  # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0  # set to '1' for GPIOs 13, 19, 41, 45 or 53

panel_1 = range(0, 13)
panel_2 = range(13, 22)
panel_3 = range(22, 31)
panel_4 = range(31, 40)
panel_5 = range(40, 49)
panel_6 = range(49, 58)
panel_7 = range(58, 67)
panel_8 = range(67, 76)
panel_9 = range(76, 89)

def to(i, t, s):
    diff = abs(i - t)
    if diff > s:
        if i > t:
            return i - s
        elif i < t:
            return i + s
        else:
            return i
    else:
        if i > t:
            return i - diff
        elif i < t:
            return i + diff
        else:
            return i


myfile = False
instructions = [["Fade", panel_1, [[255, 0, 0], [0, 0, 255]], [255, 0, 0], [0, 1], 7],
                    ["Fade", panel_2,[[0, 255, 0], [0, 0, 255], [255,122,4]], [0, 255, 0], [0,2], 7],
                    ["Static", panel_3, [25, 183, 205]],
                ["Static", panel_4, [25, 183, 205]],
                ["Static", panel_5, [25, 183, 205]],
                ["Static", panel_6, [25, 183, 205]],
                ["Static", panel_7, [25, 183, 205]],
                ["Static", panel_8, [25, 183, 205]],
                ["Static", panel_9, [25, 183, 205]]]
                    #["Strobe", panel_4, [[0, 255, 0], [0, 0, 255], [255,122,4]],[0,2], 3],
                    #["Fade", panel_5,[[0, 255, 0], [0, 60, 255], [255,122,4]], [0, 255, 0], [0,2], 7],
                    #["Fade", panel_6,[[204, 255, 0], [0, 204, 255], [255,122,4]], [0, 255, 0], [0,2], 7],
                    #["Strobe", panel_7, [[0, 255, 111], [179, 0, 255], [255,122,4]],[0,2], 3],
                    #["Fade", panel_8,[[19, 255, 203], [45, 77, 255], [255,122,4]], [0, 255, 0], [0,2], 7],
                    #["Strobe", panel_9, [[92, 255, 0], [0, 36, 255], [255,122,4]],[0,2], 3]]

def run_animations(ins):
    global myfile, instructions
    for i in reversed(ins):
        print(i)
        if i[0] == "Static":
            for j in i[1]:
                strip.setPixelColor(j, Color(i[2][0], i[2][1], i[2][2]))
                strip.show()
            ins.remove(i)
        time.sleep(1)
    print(ins)
    while True:
        myfile = os.path.exists('ins.txt')
        if myfile == True:
            time.sleep(4)
            print("break")
            file1 = open("ins.txt", "r")
            instructions = eval(file1.read())
            file1.close()
            os.remove("ins.txt")
            print(instructions)
            GPIO.cleanup()
            break
        for i in ins:
            if i[0] == "Fade":
                if i[3] != i[2][i[4][0]]:
                    i[3][0] = to(i[3][0], i[2][i[4][0]][0], i[5])
                    i[3][1] = to(i[3][1], i[2][i[4][0]][1], i[5])
                    i[3][2] = to(i[3][2], i[2][i[4][0]][2], i[5])
                    for j in i[1]:
                        strip.setPixelColor(j, Color(i[3][0], i[3][1], i[3][2]))
                        strip.show()
                elif i[4][0] != i[4][1]:

                    i[4][0] += 1
                    print(i[5], i[4][0])
                else:
                    i[4][0] = 0
                    print(i[5], "reset")
            elif i[0] == "Strobe":
                if i[3][0] != i[3][1] + 1:
                    for j in i[1]:
                        strip.setPixelColor(j, Color(i[2][i[3][0]][0], i[2][i[3][0]][1], i[2][i[3][0]][2]))
                        strip.show()
                    # time.sleep(1)
                    print(i[4], i[3][0])
                    i[3][0] += 1

                else:
                    i[3][0] = 0
                    print(i[4], "reset")


if __name__ == '__main__':
    # Process argument

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

    # Intialize the library (must be called once before other functions).
    # data structure for fade[[animation type, panel#, [colors][updated color][phase, num of phases], speed]
    # structure of strobe [[animation type, panel#, [colors],[phase, num of phases]]
    # structure of static [[animation type, panel#, [color]]


    strip.begin()



    while True:
        print("new animation")
        run_animations(instructions)


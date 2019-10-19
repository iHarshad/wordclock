import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 144)

import time_mode as time_mode
import mapping_matrix as mapping_matrix
from time_mode import *
from mapping_matrix import *


# Uses mapping matrix to assign which LEDs to light up and lights up LEDs
def disp_time():
    for j in range(12):
        for k in range(12):
            if (time_mode.Matrix[k][j] == 1):
                m = mapping_matrix.getMatrix() # create mapping matrix
                pixels[int(m[k][j])] = (0, 255, 0)

# clears LEDs except for words "it" "is" and "oclock"
def disp_clear_hour():
    time_mode.clear_hour()
    time_mode.clear_mins()
    for j in range(12):
        for k in range(8):
            m = mapping_matrix.getMatrix() # create mapping matrix
            pixels[int(m[k+1][j])] = (0, 0, 0)
            
# clears LEDs except for words "it" "is" and "oclock" and "hour"
def disp_clear_mins():
    time_mode.clear_mins()
    for j in range(12):
        for k in range(4):
            m = mapping_matrix.getMatrix() # create mapping matrix
            pixels[int(m[k+1][j])] = (0, 0, 0)

def clear_LEDs():
    pixels.fill((0,0,0))

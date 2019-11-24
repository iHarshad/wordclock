import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 144,  brightness=0.8, auto_write=False)

import time_mode as time_mode
import mapping_matrix as mapping_matrix
from time_mode import *
from mapping_matrix import *


# Uses mapping matrix to assign which LEDs to light up and lights up LEDs
def disp_time():
    time_mode.set_base_words()
    time_mode.set_hour(time_mode.getHour())
    time_mode.set_minutes(time_mode.getMinutes())
    time_mode.set_day(time_mode.getDay())
    for j in range(12):
        for k in range(12):
            m = mapping_matrix.getMatrix() # create mapping matrix
            if (time_mode.Matrix[k][j] == 1):
                pixels[int(m[k][j])] = (255, 255, 255)
            if (time_mode.Matrix[k][j] == 2):
                pixels[int(m[k][j])] = (255, 0, 0)
    pixels.show()

# clears LEDs except for words "it" "is" and "oclock"
def disp_clear_middle():
    time_mode.clear_middle()
    for j in range(12):
        for k in range(9):
            m = mapping_matrix.getMatrix() # create mapping matrix
            if k == 8 and j <= 3:
                pixels[int(m[9][j])] = (0, 0, 0)
            elif k != 8:
                pixels[int(m[k+1][j])] = (0, 0, 0)
    pixels.show()

def clear_LEDs():
    pixels.fill((0,0,0))
    pixels.show()


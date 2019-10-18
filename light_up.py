import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 144)

from time_mode import *
from mapping_matrix import *

# Uses mapping matrix to assign which LEDs to light up and lights up LEDs
def valid2Neopixels():
    for j in range(12):
        for k in range(12):
            if (time_mode.Matrix[k][j] == 1):
                pixels[mapping_matrix.Matrix[k][j]] = (255,0,0)

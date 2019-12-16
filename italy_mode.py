import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 144,  brightness=0.2, auto_write=False)
import mapping_matrix as mapping_matrix
from mapping_matrix import *

Matrix = np.zeros((12,12))

def disp_flag():
    m = mapping_matrix.getMatrix() 
    for r in range (12):
        for c in range(12):
            if c <= 3:
                pixels[int(m[r][c])] = (0, 255, 0)
            elif c <= 7:
                pixels[int(m[r][c])] = (255, 255, 255)
            else:
                pixels[int(m[r][c])] = (255, 0, 0)
    pixels.show();

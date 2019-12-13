# NOTE: needs to be optimized for negative + 3 digit temperatures
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 144,  brightness=0.6, auto_write=False)

import pyowm

import mapping_matrix as mapping_matrix
from mapping_matrix import *

Matrix = np.zeros((12,12))


def get_temp():
    owm = pyowm.OWM('42d3356ccc8eb2b64d2ac8acfffe0749')
    observation = owm.weather_at_place("Ithaca,US")
    w = observation.get_weather()
    temperature = w.get_temperature('fahrenheit')
    return round(temperature['temp'])

def clear_LEDs():
    global Matrix
    Matrix = np.zeros((12,12))
    pixels.fill((0,0,0))
    pixels.show()
    
def display_temp(rgb):
    global Matrix
    #light up "TEMP"
    m = mapping_matrix.getMatrix() 
    for t in range(4):
        pixels[int(m[0][t+8])] = (255, 255, 255)
    #light up "OUTSIDE"
    m = mapping_matrix.getMatrix() 
    for o in range(7):
        pixels[int(m[10][o+5])] = (255, 255, 255)
    
    # light up numerical temperature
    for j in range(12):
        for k in range(12):
            if (Matrix[k][j] == 1):
                print("here")
                pixels[int(m[k][j])] = rgb
    pixels.show();

#color is currently set based on temperature, but can be set based on weather, etc.
def set_rgb(temp):
    if temp >= 70:
        return (255, 0, 0)
    elif temp > 30:
        return (0, 255, 0)
    else:
        return (0, 150, 255)
        
def set_digit(digit, firstlastsingle): #first = 0, last = 1, single = 2
    global Matrix
    offset = 0
    if firstlastsingle == 1:
            offset = 5
    elif firstlastsingle == 2:
            offset = 3

    if (digit == 1):
        if firstlastsingle != 0:
            offset = 2
        for r in range(7):
            Matrix[r+2][4 + offset] = 1
    elif (digit == 2):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
        Matrix[6][1+offset] = 1
        Matrix[7][1+offset] = 1
        Matrix[8][1+offset] = 1
        Matrix[8][2+offset] = 1
        Matrix[8][3+offset] = 1
        Matrix[8][4+offset] = 1
    elif (digit == 3):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[8][1+offset] = 1
        Matrix[8][2+offset] = 1
        Matrix[8][3+offset] = 1
        Matrix[8][4+offset] = 1
    elif (digit == 4):
        Matrix[2][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[8][4+offset] = 1
        Matrix[2][1+offset] = 1
        Matrix[3][1+offset] = 1
        Matrix[4][1+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
    elif (digit == 5):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][1+offset] = 1
        Matrix[4][1+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[8][1+offset] = 1
        Matrix[8][2+offset] = 1
        Matrix[8][3+offset] = 1
        Matrix[8][4+offset] = 1
    elif (digit == 6):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][1+offset] = 1
        Matrix[4][1+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[6][1+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[7][1+offset] = 1
        Matrix[8][1+offset] = 1
        Matrix[8][2+offset] = 1
        Matrix[8][3+offset] = 1
        Matrix[8][4+offset] = 1
    elif (digit == 7):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[8][4+offset] = 1
    elif (digit == 8):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][1+offset] = 1
        Matrix[4][1+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
        Matrix[6][1+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[7][1+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[8][1+offset] = 1
        Matrix[8][2+offset] = 1
        Matrix[8][3+offset] = 1
        Matrix[8][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
    elif (digit == 9):
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[8][4+offset] = 1
        Matrix[3][1+offset] = 1
        Matrix[4][1+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[5][2+offset] = 1
        Matrix[5][3+offset] = 1
    else: # digit is 0
        Matrix[2][1+offset] = 1
        Matrix[2][2+offset] = 1
        Matrix[2][3+offset] = 1
        Matrix[2][4+offset] = 1
        Matrix[3][1+offset] = 1
        Matrix[4][1+offset] = 1
        Matrix[5][1+offset] = 1
        Matrix[6][1+offset] = 1
        Matrix[5][4+offset] = 1
        Matrix[7][1+offset] = 1
        Matrix[6][4+offset] = 1
        Matrix[7][4+offset] = 1
        Matrix[8][1+offset] = 1
        Matrix[8][2+offset] = 1
        Matrix[8][3+offset] = 1
        Matrix[8][4+offset] = 1
        Matrix[3][4+offset] = 1
        Matrix[4][4+offset] = 1
        
def split_digits(temp):
    if temp < 10:
        set_digit(temp, 2);
    else:
        t = str(temp)
        set_digit(int(t[0]), 0)
        set_digit(int(t[1]), 1)


def main():
    t = get_temp();
    split_digits(t);
    clear_LEDs();
    rgb = set_rgb(t);
    display_temp(rgb);
    
    while True:
        junk = 1;

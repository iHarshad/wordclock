# NOTE: needs to be optimized for negative + 3 digit temperatures
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 144,  brightness=0.6, auto_write=False)

import pyowm

import mapping_matrix as mapping_matrix
from mapping_matrix import *

Matrix = np.zeros((12,12))
rgb = (0,0,0)

def get_temp():
    global rgb
    owm = pyowm.OWM('42d3356ccc8eb2b64d2ac8acfffe0749')
    observation = owm.weather_at_place("Ithaca,US")
    w = observation.get_weather()
    rgb = set_rgb(w.get_status())
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
                pixels[int(m[k][j])] = rgb
    pixels.show();

#color is currently set based on temperature, but can be set based on weather, etc.
def set_rgb(status):
    if status == 'Mist':
        return((0, 100, 80))
    elif status == 'Rain':
        return((0, 150, 255))
    elif status == 'Drizzle':
        return((0, 200, 255))
    elif status == 'Snow':
        return((200, 200, 255))
    elif status == 'Clear':
        return((255, 200, 0))
    elif status == 'Clouds':
        return((255, 255, 255))
    elif status == 'Wind':
        return((255, 0, 255))
    return((255, 0, 0)) # default case
        
def set_digit(digit, firstlastsingle): #first = 0, last = 1, single = 2
    global Matrix
    offset = -1
    if firstlastsingle == 1:
            offset = 4
    elif firstlastsingle == 2:
            offset = 2

    if (digit == 1):
        if firstlastsingle != 0:
            offset = 1
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
        
    #display degrees symbol
    Matrix[2][10] = 1
    Matrix[2][11] = 1
    Matrix[3][10] = 1
    Matrix[3][11] = 1
        
def split_digits(temp):
    if temp < 10:
        set_digit(temp, 2);
    else:
        t = str(temp)
        set_digit(int(t[0]), 0)
        set_digit(int(t[1]), 1)


def main():
    global rgb
    t = get_temp();
    split_digits(t);
    display_temp(rgb);
    
    while True:
        junk = 1;

import numpy
import board
import neopixel
import random
pixels = neopixel.NeoPixel(board.D18, 144,  brightness=0.2, auto_write=False)

import mapping_matrix as mapping_matrix
from mapping_matrix import *

import RPi.GPIO as GPIO
import time

Matrix = np.zeros((12,12))
snake = [[5,5], [5,4], [5,3],[5,2]]
apple = [0,0]
end = False

def button_init():
    GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO17
    GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO27
    GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO22

def disp_snake():
    pixels.fill((0,0,0))
    pixels.show()
    for k in range(len(snake)):
        snake_x = get_x(snake[k])
        snake_y = get_y(snake[k])
        Matrix[snake_x][snake_y] = 1
        m = mapping_matrix.getMatrix()
        if k == 0:
            pixels[int(m[snake_x][snake_y])] = (255, 255, 255)
        else:
            pixels[int(m[snake_x][snake_y])] = (0, 255, 0)
    pixels.show()
    for i in range(12):
        for j in range(12):
            if Matrix[i][j] == 2:
                pixels[int(m[i][j])] = (255, 0, 0)
    pixels.show()


def generate_apple():
    global apple
    x = random.randint(0,11)
    y = random.randint(0,11)
    if snake.count([x,y]) > 0:
        x = random.randint(0,11)
        y = random.randint(0,11)
    apple = [x,y]
    Matrix[x][y] = 2
    
def get_x(arr):
    return arr[0]

def get_y(arr):
    return arr[1]

def get_button_press():
    while True:
        top = GPIO.input(23)
        bottom = GPIO.input(17)
        right = GPIO.input(27)
        left = GPIO.input(22)

        if top == False:
            return 0;
        elif bottom == False:
            return 1;
        elif right == False:
            return 2;
        elif left == False:
            return 3;

def move_snake():
    x = get_x(snake[0])
    y = get_y(snake[0])

    direction = get_button_press()
    boundary = True
    location = [0,0]
    if direction == 0:
        if x-1 >= 0: # boundary condition
            boundary = False
            location = [x-1, y]
    elif direction == 1:
        if x+1 <= 11: # boundary condition
            boundary = False
            location = [x+1, y]
    elif direction == 2:
        if y+1 <= 11: # boundary condition
            boundary = False
            location = [x, y+1]
    elif direction == 3:
        if y-1 >= 0: # boundary condition
            boundary = False
            location = [x, y-1]

    if boundary == False:
        snake.insert(0, location)
        check_snake_hit(location)
        if location != apple:
            snake.pop(len(snake)-1)
        else:
            generate_apple()

def check_snake_hit(location):
    global end
    if snake.count(location) > 1:
        end = True

def end_game():
    # flash lights
    while True:
        pixels.fill((0,0,0))
        pixels.show()
        time.sleep(1)
        disp_snake()
        time.sleep(1)

def main():
    global end
    button_init()
    generate_apple()
    while end == False:
        disp_snake()
        move_snake()
        time.sleep(0.2)
    end_game()
main()

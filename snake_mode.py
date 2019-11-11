import numpy
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 144,  brightness=0.2, auto_write=False)

import mapping_matrix as mapping_matrix
from mapping_matrix import *

import RPi.GPIO as GPIO
import time

Matrix = np.zeros((12,12))
snake = [[5,5], [5,4], [5,3],[5,2]]
apple = [0,0]

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

def generate_apple():
    global apple
    x = random.randint(0,11)
    y = random.randint(0,11)
    if snake.count([x,y]) > 0:
        x = random.randint(0,11)
        y = random.randint(0,11)
    apple = [x,y]
    Matrix[x][y] = 2
    m = mapping_matrix.getMatrix()
    pixels[int(m[x][y])] = (255, 0, 0)
    pixels.show()

def get_x(arr):
    return arr[0]

def get_y(arr):
    return arr[1]

def get_button_press():
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
    x = snake.get_x(snake[0])
    y = snake.get_y(snake[0])
    snake.insert(0, [x,y])

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
        if y-1 <= 11: # boundary condition
            boundary = False
            location = [x, y-1]

    if boundary == False:
        snake[0] = location
        check_snake_hit(location)
        if location != apple:
            snake.pop(len(snake)-1)
        else:
            generate_apple()

def check_snake_hit(location):
    if snake.count(location) > 1:
        end_game()

def end_game():
    # flash lights
    while True:
        disp_snake()
        time.sleep(0.5)
        pixels.fill((0,0,0))
        time.sleep(0.5)

def main():
    generate_apple()

    while True:
        disp_snake()
        move_snake()
        time.sleep(0.2)
main()

import time_mode as time_mode
import light_up as light_up
import snake_mode as snake_mode
from snake_mode import *
from time_mode import *
from light_up import *
changed = 0;
mode = 0;

def clock(): #mode 0
    light_up.clear_LEDs()
    light_up.disp_time()
    
    while (1):
        if mode == 0:
            if time_mode.getSeconds() == 0:
                if time_mode.getMinutes() % 5 == 0:
                    light_up.disp_clear_middle()
                    light_up.disp_time()
                    time.sleep(1)
            check_mode_change(); # may effect the check on every five mins since delay incurred
        else:
            snake();

def snake(): #mode 1
    snake_mode.reset_game()
    global mode
    snake_mode.button_init()
    snake_mode.generate_apple()
    while snake_mode.end == False:
        if mode == 1:
            snake_mode.disp_snake()
            snake_mode.move_snake()
            check_mode_change()
            time.sleep(0.1)
        else:
            clock();
    snake_mode.end = False;
    # display end of the game
    while True:
        if mode == 1:
            snake_mode.end_game()
            check_mode_change()
        else:
            clock();

def check_mode_change():
    global mode
    pressed = GPIO.input(26)
    if pressed == False:
        mode = not(mode)
        time.sleep(.8)
    
def main():
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    clock() # begin on mode 1


main()


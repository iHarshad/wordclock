
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
    #print(time_mode.getMinutes())
    #print(time_mode.getHour())
    
    while (1):
        if time_mode.getSeconds() == 0:
            if time_mode.getMinutes() % 5 == 0:
                light_up.disp_clear_middle()
                light_up.disp_time()
                time.sleep(1)
        check_mode_change(); # may effect the check on every five mins since delay incurred
        
def snake():
    snake_mode.button_init()
    snake_mode.generate_apple()
    while snake_mode.end == False:
        snake_mode.disp_snake()
        snake_mode.move_snake()
        time.sleep(0.1)
        check_mode_change();
    snake_mode.end_game() # need to check for mode change here

def check_mode_change():
    timeout = .1
    timeout_start = time.time()
    
    while time.time() < timeout_start + timeout:
        pressed = GPIO.input(XXX)
        if pressed == False:
            if mode == 0:
                #clear matrix?
                snake();
            elif mode == 1:
                #clear matrix and reset snake?
                clock();

def main():
    GPIO.setup(XXX, GPIO.IN, pull_up_down=GPIO.PUD_UP)#setup button, change XXX to actual gpio pin number
    clock();



main()

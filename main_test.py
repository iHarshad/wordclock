import time_mode as time_mode
import light_up as light_up
import snake_mode as snake_mode
import temp_test as temp_test
from temp_test import *
from snake_mode import *
from time_mode import *
from light_up import *
changed = 0;
mode = 0;

def clock(): #mode 0
    print("clock");
    global mode
    light_up.clear_LEDs()
    light_up.disp_clear_middle()
    light_up.disp_time()
    
    while (1):
        if mode == 0:
            if time_mode.getSeconds() == 0:
                if time_mode.getMinutes() % 5 == 0:
                    light_up.disp_clear_middle()
                    light_up.disp_time()
                    time.sleep(1)
            check_mode_change(); # may effect the check on every five mins since delay incurred
        elif mode == 1:
            temp();

def temp():
    print("temp");
    global mode
    try:
        temp_test.clear_LEDs();
        t = temp_test.get_temp();
        temp_test.split_digits(t);
        rgb = temp_test.set_rgb(t);
        temp_test.display_temp(rgb);
    except:
        mode = 2; # if offline or no internet, weather mode not availible
    while True:
        if time_mode.getSeconds() == 0 and time_mode.getMinutes() % 5 == 0: # read temperature every 5 mins
            try:
                temp_test.clear_LEDs();
                t = temp_test.get_temp();
                temp_test.split_digits(t);
                rgb = temp_test.set_rgb(t);
                temp_test.display_temp(rgb);
                time.sleep(1)
            except:
                mode = 2; # if offline or no internet, weather mode not availible
        
        if mode == 1:
            check_mode_change()
        elif mode == 2:
            light_up.clear_LEDs()
            snake();

def snake(): #mode 2
    print("snake");
    snake_mode.reset_game()
    global mode
    snake_mode.button_init()
    snake_mode.generate_apple()
    while snake_mode.end == False:
        if mode == 2:
            snake_mode.disp_snake()
            snake_mode.move_snake()
            check_mode_change()
            time.sleep(0.1)
        elif mode == 0:
            light_up.clear_LEDs()
            clock();
    snake_mode.end = False;
    # display end of the game
    while True:
        if mode == 2:
            snake_mode.end_game()
            check_mode_change()
        elif mode == 0:
            light_up.clear_LEDs()
            clock();

def check_mode_change():
    global mode
    pressed = GPIO.input(26)
    if pressed == False:
        if mode == 0:
            mode = 1;
        elif mode == 1:
            mode = 2;
        else:
            mode = 0;
        time.sleep(.8)
    
def main():
    GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    mode = 0;
    clock() # begin on mode 1


main()


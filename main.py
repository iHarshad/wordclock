import time_mode as time_mode
import light_up as light_up
import snake_mode as snake_mode
from snake_mode import *
from time_mode import *
from light_up import *
changed = 0;

def clock():
    light_up.clear_LEDs()
    light_up.disp_time()
    #print(time_mode.getMinutes())
    #print(time_mode.getHour())
    
    while 1:
        if time_mode.getSeconds() == 0:
            if time_mode.getMinutes() % 5 == 0:
                light_up.disp_clear_middle()
                light_up.disp_time()
                time.sleep(1)
        
def snake():
    snake_mode.button_init()
    snake_mode.generate_apple()
    while snake_mode.end == False:
        snake_mode.disp_snake()
        snake_mode.move_snake()
        time.sleep(0.1)
    snake_mode.end_game()

snake()



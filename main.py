
import time_mode as time_mode
import light_up as light_up

from time_mode import *
from light_up import *
changed = 0;

def main():
    light_up.clear_LEDs()
    light_up.disp_time()
    #print(time_mode.getMinutes())
    #print(time_mode.getHour())
    
    while 1:
        if (time_mode.getMinutes() == 0 and time_mode.getSeconds() == 0 or
            time_mode.getMinutes() % 5 == 0 and time_mode.getSeconds() == 0):
            light_up.disp_clear_middle()
            light_up.disp_time()
            time.sleep(1)
        

main()



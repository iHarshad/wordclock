
import time_mode as time_mode
import light_up as light_up

from time_mode import *
from light_up import *
changed = 0;

def main():
    light_up.clear_LEDs()
    while 1:
        if (time_mode.getMinutes() == 0 and time_mode.getSeconds() == 0):
            light_up.disp_clear_hour()
            time_mode.set_hour(time_mode.getHour())
            time_mode.set_minutes(time_mode.getMinutes())
            time_mode.set_base_words()
            light_up.disp_time()
            time.sleep(1)
            
        elif (time_mode.getMinutes() % 5 == 0 and time_mode.getSeconds() == 0):
            light_up.disp_clear_mins()
            time_mode.set_hour(time_mode.getHour())
            time_mode.set_minutes(time_mode.getMinutes())
            time_mode.set_base_words()
            light_up.disp_time()
            time_mode.clear_matrix()
            time.sleep(1)

        else:
            time_mode.set_hour(time_mode.getHour())
            time_mode.set_minutes(time_mode.getMinutes())
            time_mode.set_base_words()
            light_up.disp_time()
            time_mode.clear_matrix()
main()



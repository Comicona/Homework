from nums_for_clock import get_num, print_time
import os
import time

while True:
    curr_time = time.strftime("%H:%M:%S")
    dig_time = []

    for char in curr_time:
        dig_time.append(get_num(char))

    print_time(dig_time)
    time.sleep(1) 
    os.system('cls' if os.name == 'nt' else 'clear')
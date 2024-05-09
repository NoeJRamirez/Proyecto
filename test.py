
from digital_clock import DigitalClock
from utime import sleep

def clock_test()->None:
    clock=DigitalClock(23,59,50)
    while True:
        h,m,s=clock.get_time()
        time=f'{h:02} : {m:02} : {s:02}'
        print(time)
        sleep(1)
        clock.increment()


from digital_clock import DigitalClock
from utime import sleep
from pantalla import Pantalla

def clock_test():
    pantalla = Pantalla()
    clock=DigitalClock(23,59,50)
    while True:
        h,m,s=clock.get_time()
        time_str=f'{h:02} : {m:02} : {s:02}'
        pantalla.mostrar_texto(time_str)
        #print(time)
        sleep(1)
        clock.increment()
if __name__ == "__main__":
    # Ejecutar las pruebas del reloj
    clock_test()
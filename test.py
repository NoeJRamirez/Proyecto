
from digital_clock import DigitalClock
from utime import sleep
from pantalla import Pantalla
from random import randint
from fsm import FSM

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

def fsm_test()->None:
    fsm=FSM()
    event={
        'unconditional':0,
        'default':      1,
        'Press_Buton':  2,
        'Button':       3,
        'Not_Button':   4,
        'not_timeout':  5,
        #timeout event si handled by the interrup uC interrupt Mechanism
    }
    fsm.set_transition_rule(0, event['unconditional'],1)
    fsm.set_transition_rule(1, event['default'],1)
    fsm.set_transition_rule(1, event['Press_Buton'],2)
    fsm.set_transition_rule(2, event['Button'],4)
    fsm.set_transition_rule(2, event['Not_Button'],1)
    fsm.set_transition_rule(4, event['not_timeout'],5)
    fsm.set_transition_rule(5,event['not_timeout'],1)
    while True:
        state=fsm.get_current_state()
        if state==0:
            print(f'current state{state}')
            sleep(1)
            fsm.compute_next_state(event['unconditional'])
        elif state==1:
            print(f'current state{state}')
            sleep(1)
            rnd_ev=randint(event['default'],event['Press_Buton'])
            fsm.compute_next_state(rnd_ev)
        elif state==2:
            print(f'current state{state}')
            sleep(1)
            rnd_ev=randint(event['Button'],event['Not_Button'])
            fsm.compute_next_state(rnd_ev)
        #estado 3  si handled by interrupting the uC
        elif state==4:
            print(f'current state{state}')
            sleep(1)
            fsm.compute_next_state(event['not_timeout'])
        else:
            print('Are you OK, Any?')    
if __name__ == "__main__":
    fsm_test()

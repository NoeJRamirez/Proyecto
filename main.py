from test import clock_test
from test import fsm_test 

debug = True

def main() -> None:
    pass

if __name__ == '__main__':
    if debug:
        # Descomenta segun el test que quieras hacer 
        # clock_test()
        fsm_test()
    else:
        main()
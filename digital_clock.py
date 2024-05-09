class DigitalClock:
    def __init__(self, h: int=0, m: int=0,s: int=0)->None:
        """constructor reloj digital con Horas,Minutos,segundos

        Args:
            h (int, optional): _description_. Defaults to 0.
            m (int, optional): _description_. Defaults to 0.
            s (int, optional): _description_. Defaults to 0.
        """
        assert h <24 and h>=0
        self.__h=h
        assert m<60 and m >=0
        self.__m=m
        assert s<60 and s >=0
        self.__s=s

def get_time(self)->tuple[int, int, int]:
    """muestra la hora del reloj digital(DigitalClock)

    Returns:
        tuple[int, int, int]:h,m,s es en formato 24 hrs
    """
    return self.__h, self.__m, self.__s
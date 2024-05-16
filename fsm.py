class FSM:
    """Esta clase está diseñada para implementar una FSM determinista modelando tanto los estados como las transiciones."""
    
    def __init__(self, initial_state: int = 0) -> None:
        """Este método inicializa un objeto FSM con el estado inicial.
        
        Args:
            initial_state (int, optional): El estado inicial de la FSM. Por defecto es 0.
        """
        self.__current_state: int = initial_state
        self.__transitions: dict[tuple[int, int], int] = {}

    def get_current_state(self) -> int:
        """Obtiene el estado actual.
        
        Returns:
            int: El estado actual de la FSM.
        """
        return self.__current_state

    def compute_next_state(self, ev: int) -> None:
        """Actualiza el estado actual tomando en cuenta el evento dado.
        
        Args:
            ev (int): El código del evento que produce la transición.
        """
        if (self.__current_state, ev) in self.__transitions:
            self.__current_state = self.__transitions[(self.__current_state, ev)]
        else:
            raise KeyError(f"No transition defined for state {self.__current_state} and event {ev}")

    def set_transition_rule(self, current_state: int, event_number: int, next_state: int) -> None:
        """Define una nueva regla de transición.
        
        Args:
            current_state (int): El código del estado actual.
            event_number (int): El código del evento.
            next_state (int): El código del siguiente estado.
        """
        self.__transitions[(current_state, event_number)] = next_state
class Position:
    def __init__(self, position: tuple[float, float] = (0.0, 0.0)) -> None:
        self.x: float = position[0]
        self.y: float = position[1]
    
    # Reset the position
    def reset(self) -> None:
        self.x = 0.0
        self.y = 0.0
    
    # Set the position
    def set(self, x: float = None, y: float = None) -> None: # type: ignore
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
    
    # Get the position
    def get(self) -> tuple[float, float]:
        return (self.x, self.y)

    # Create a copy
    def copy(self):
        return Position((self.x, self.y))
    
    # When two Position variables are substracted
    def __sub__(self, other: 'Position') -> 'Position':
        return Position((self.x - other.x, self.y - other.y))
    
    # When two Position variables are added
    def __add__(self, other: 'Position') -> 'Position':
        return Position((self.x + other.x, self.y + other.y))
    
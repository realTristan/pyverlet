class Vector2D:
    def __init__(self, x: float, y: float) -> None:
        self.x: float = x
        self.y: float = y
    
    # When two Vector2D variables are substracted
    def __sub__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x - other.x, self.y - other.y)
    
    # When two Vector2D variables are added
    def __add__(self, other: 'Vector2D') -> 'Vector2D':
        return Vector2D(self.x + other.x, self.y + other.y)
    
    # When two Vector2D variables are multiplied
    def __mul__(self, other: float) -> 'Vector2D':
        return Vector2D(self.x * other, self.y * other)
    
    # When two Vector2D variables are divided
    def __truediv__(self, other: float) -> 'Vector2D':
        return Vector2D(self.x / other, self.y / other)
    
    # Reset the position
    def zero(self) -> 'Vector2D':
        self.x = 0.0
        self.y = 0.0
        return self

    # Negate the entire vector
    def negate(self, index: int = -1) -> 'Vector2D':
        if index == 0:
            self.x *= -1.0
        elif index == 1:
            self.y *= -1.0
        else:
            self.scale(-1.0)
        return self
        
    # Set the position
    def set(self, x: float = None, y: float = None) -> 'Vector2D': # type: ignore
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        return self
    
    # Get the position
    def get(self) -> tuple[float, float]:
        return (self.x, self.y)

    # Create a copy
    def copy(self)-> 'Vector2D':
        return Vector2D(self.x, self.y)
    
    # Dot product
    def dot(self, other: 'Vector2D') -> float:
        return self.x * other.x + self.y * other.y
    
    # Cross product
    def cross(self, other: 'Vector2D') -> float:
        return self.x * other.y - self.y * other.x
    
    # Magnitude
    def magnitude(self) -> float:
        return (self.x * self.x + self.y * self.y) ** 0.5
    
    # Normalize
    def normalize(self) -> 'Vector2D':
        mag: float = self.magnitude()
        self.x /= mag
        self.y /= mag
        return self
        
    # Scale all values
    def scale(self, scalar: float) -> 'Vector2D':
        self.x *= scalar
        self.y *= scalar
        return self
    
    # Add to all values
    def add(self, scalar: float) -> 'Vector2D':
        self.x += scalar
        self.y += scalar
        return self
        
    # Substract from all values
    def sub(self, scalar: float) -> 'Vector2D':
        self.x -= scalar
        self.y -= scalar
        return self
    
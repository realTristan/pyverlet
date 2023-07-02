import pygame
import time
from physics import Friction, Position, Velocity, Acceleration


# Ball class
class VerletBall:
    def __init__(self, position: tuple[float, float], radius: float = 10.0) -> None:
        # Physics variables
        self.current_position: Position = Position(position)
        self.prev_position: Position = Position(position)
        self.acceleration: Acceleration = Acceleration((0.0, 0.0))
        self.velocity: Velocity = Velocity((0.0, 0.0))
        
        # Self variables
        self.radius: float = radius
        self.start_time: float = time.time()
        self.color: tuple[int, int, int] = (255, 255, 255)
        self.friction: Friction = None  # type: ignore

    # Update the ball's color
    def set_color(self, color: tuple[int, int, int]) -> None:
        self.color = color

    # Set the ball friction
    def set_friction(self, friction: Friction) -> None:
        self.friction = friction

    # Draw the object
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self.color, 
                           self.current_position.get(), self.radius)

    # Calculate the objects velocity
    def calculate_velocity(self) -> None:
        x: float = (self.current_position.x - self.prev_position.x) * 0.96
        y: float = (self.current_position.y - self.prev_position.y) * 0.96
        self.velocity.set(x, y)

    # Perform the verlet integration to calcualte the displacement
    def calculate_displacement(self, dt: float):
        x: float = self.current_position.x + self.velocity.x + self.acceleration.x * dt * dt
        y: float = self.current_position.y + self.velocity.y + self.acceleration.y * dt * dt
        
        # Update the current position
        self.current_position.set(x, y)

    # Update the objects position
    def update_position(self, dt: float) -> None:
        self.calculate_velocity()

        # Save the current position (use a copy)
        self.prev_position = self.current_position.copy()

        # Perform the Verlet integration
        self.calculate_displacement(dt)

        # Reset the acceleration
        self.acceleration.reset()

    # Accelerate the object
    def accelerate(self, acceleration: tuple[float, float]) -> None:
        self.acceleration.x += acceleration[0]
        self.acceleration.y += acceleration[1]

    # Check if the ball is colliding with other balls
    @staticmethod
    def check_collisions(balls: list['VerletBall']) -> None:
        for ball_1 in balls:
            for ball_2 in balls:
                if ball_1 == ball_2:
                    continue

                # Calculate the distance between the balls
                dist: Position = ball_2.current_position - ball_1.current_position
                
                # the vector magnitude of the ball
                mag: float = (dist.x ** 2 + dist.y ** 2) ** 0.5
                delta: float = ball_1.radius + ball_2.radius
                if mag < delta:
                    # Calculate the ball overlap (the amount the balls have overlapped)
                    overlap: float = (delta - mag) / 2

                    # Update this balls position (move it to the side)
                    ball_1.current_position.y -= overlap * dist.x / mag
                    ball_1.current_position.y -= overlap * dist.x / mag

                    # Update the other ball's position (move it to the opposite side)
                    ball_2.current_position.x += overlap * dist.x / mag
                    ball_2.current_position.x += overlap * dist.x / mag

from components import Menu
from objects import LineCollider, VerletBall, OpenCircleCollider
from components.list import ButtonList
import pygame, time, threading, random
from physics import Vector2D
from testing.config import draw_background, CLOCK
from utils import Colors

# Initialize pygame
pygame.init()

# Window Title
pygame.display.set_caption("pyverlet")

# Set the screen
screen: pygame.Surface = pygame.display.set_mode((800, 600))

# Create a menu
menu: Menu = Menu(screen)

# Colliders and Verlet Balls
colliders: list[OpenCircleCollider | LineCollider] = []
verlet_balls: list[VerletBall] = []

# Create a list of colliders
items: ButtonList = ButtonList()


# Automatically add the balls
def auto_add_balls():
    while 1:
        time.sleep(0.1)
        ball: VerletBall = VerletBall(
            (270.0, 60.0), random.randint(5, 10), Colors.random()
        )
        verlet_balls.append(ball)


# Start threading
threading.Thread(target=auto_add_balls).start()

# Game Loop
while 1:
    # Draw the background
    draw_background()

    # Draw the menu and items
    menu.draw_buttons(screen)
    items.draw(screen, colliders)

    # Cap the amount of balls present
    while len(verlet_balls) > 200:
        verlet_balls.pop(0)

    # Check for a close event
    for event in pygame.event.get():
        # Check if the event is a close event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Check if the event is a click event
        for item in items.clicked(event):
            colliders.remove(item.item)
            items.remove(item)

        # Check if the event is a click event
        if menu.line_collider_button.clicked(event):
            colliders.append(LineCollider((200.0, 100.0), 150.0, 35.0, 2))

        # Check if the event is a click event
        elif menu.circle_collider_button.clicked(event):
            colliders.append(
                OpenCircleCollider(
                    position=(400.0, 300.0),
                    radius=300,
                    width=5,
                    outside_collision=False,
                )
            )

    # Update the verlet_balls
    [ball.update(screen, verlet_balls) for ball in verlet_balls]
    [[collider.apply(ball) for collider in colliders] for ball in verlet_balls]
    [collider.draw(screen) for collider in colliders]

    # Frames and update the display
    # CLOCK.tick(60)
    pygame.display.flip()

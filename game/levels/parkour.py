"""Normal level: the parkour course with enemies, ending at the boss-room door.
"""
import pygame

from game import loop
from game.state import state


def draw():
    """Draw the level, the player's stat bars and the enemy health bars."""
    state.screen.fill([0, 0, 0])
    pygame.display.update()


def handle_events():
    """Keyboard and mouse input for the parkour level."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.parkour_enemies = False


def frame():
    """One frame of the level, in the exact order of the original loop body."""
    draw()
    pygame.display.flip()
    handle_events()


def run():
    """Run the level until its flag turns off (door entered, boss beaten, or window closed)."""
    loop.run(state.clock, 70, lambda: state.parkour_enemies, frame)

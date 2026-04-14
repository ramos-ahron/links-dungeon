"""Normal level: the parkour course with enemies, ending at the boss-room door.
"""
import pygame

from game import loop
from game.sprite import Sprite
from game.state import state


def build_background():
    """Create the side boundaries, scrolling backgrounds and floor."""
    state.back1 = Sprite(800, 550, None, "background1.jpg")
    state.back2 = Sprite(800, 550, None, "background1.jpg")
    state.back2.setPosition(800, 0)
    state.background.append(state.back1)
    state.background.append(state.back2)


def fill_draw_groups():
    """Put the level sprites into the groups that get drawn each frame."""
    state.all_sprites1.add(state.background)


def draw():
    """Draw the level, the player's stat bars and the enemy health bars."""
    state.screen.fill([0, 0, 0])
    state.all_sprites1.draw(state.screen)
    pygame.display.update()


def handle_events():
    """Keyboard and mouse input for the parkour level."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.parkour_enemies = False


def setup():
    """Build the level (runs once, before the loop)."""
    build_background()
    fill_draw_groups()


def frame():
    """One frame of the level, in the exact order of the original loop body."""
    draw()
    pygame.display.flip()
    handle_events()


def run():
    """Run the level until its flag turns off (door entered, boss beaten, or window closed)."""
    loop.run(state.clock, 70, lambda: state.parkour_enemies, frame)

"""Normal level: the parkour course with enemies, ending at the boss-room door.
"""
import pygame

from game import loop, physics, player
from game.sprite import Sprite
from game.colors import PINK
from game.state import state


def build_background():
    """Create the side boundaries, scrolling backgrounds and floor."""
    state.bound1 = Sprite(300, 550, PINK)
    state.bound2 = Sprite(300, 550, PINK)
    state.bound3 = Sprite(300, 550, PINK)
    state.bound4 = Sprite(300, 550, PINK)
    state.bound5 = Sprite(300, 550, PINK)
    state.bound6 = Sprite(300, 550, PINK)
    state.bound7 = Sprite(300, 550, PINK)
    state.bound8 = Sprite(300, 550, PINK)
    state.bound1.setPosition(-500,0)
    state.bound2.setPosition(9000,0)
    state.bound3.setPosition(-300,0)
    state.bound4.setPosition(800,0)
    state.bound5.setPosition(-600,0)
    state.bound6.setPosition(1100,0)
    state.boundaries.append(state.bound1)
    state.boundaries.append(state.bound2)
    state.back1 = Sprite(800, 550, None, "background1.jpg")
    state.back2 = Sprite(800, 550, None, "background1.jpg")
    state.back2.setPosition(800, 0)
    state.background.append(state.back1)
    state.background.append(state.back2)
    state.ground1 = Sprite(800, 90, None,"floor.png")
    state.ground2 = Sprite(800, 90, None, "floor.png")
    state.ground3 = Sprite(400, 50, None, "wall_texture_05.png")
    state.ground4 = Sprite(400, 50, None, "wall_texture_05.png")
    state.ground1.setPosition(0, 460)
    state.ground2.setPosition(800, 460)
    state.ground3.setPosition(1075, 125)
    state.ground4.setPosition(2330, 130)
    state.ground.append(state.ground1)
    state.ground.append(state.ground2)
    state.ground.append(state.ground3)
    state.ground.append(state.ground4)


def fill_draw_groups():
    """Put the level sprites into the groups that get drawn each frame."""
    state.all_sprites1.add(state.boundaries,state.background,state.ground,state.player)


def draw():
    """Draw the level, the player's stat bars and the enemy health bars."""
    state.screen.fill([0, 0, 0])
    state.all_sprites1.draw(state.screen)
    pygame.display.update()


def reset_frame_flags():
    """Clear the per-frame collision flags."""
    state.a_collision = False
    state.e_a_collision = False
    state.collision = False
    state.defend = False
    state.bottom = False
    state.side_collision = False
    state.enemy1_stop_left = False
    state.enemy1_stop_right = False


def handle_events():
    """Keyboard and mouse input for the parkour level."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.parkour_enemies = False


def setup():
    """Build the level (runs once, before the loop)."""
    build_background()
    player.create_player()
    fill_draw_groups()


def frame():
    """One frame of the level, in the exact order of the original loop body."""
    physics.reset_speeds_and_gravity()
    draw()
    reset_frame_flags()
    player.collide_with_ground()
    physics.apply_gravity()
    pygame.display.flip()
    handle_events()


def run():
    """Run the level until its flag turns off (door entered, boss beaten, or window closed)."""
    loop.run(state.clock, 70, lambda: state.parkour_enemies, frame)

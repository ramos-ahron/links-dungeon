"""Window setup, text drawing, and the core game loop.
"""
import pygame

from game.state import state


def init_display():
    """Open the 800x550 window and set its title."""
    pygame.init()
    state.screen = pygame.display.set_mode([800, 550])
    state.screen.fill([0, 0, 0])
    pygame.display.set_caption("Link's Dungeon")


def add_text(my_text,position,size,color):
    """Draw `my_text` on the screen. (Builds the font on every call, like the original.)"""
    my_font = pygame.font.SysFont(None,size)
    text = my_font.render(my_text, True,color)
    state.screen.blit(text,position)


# Every speed, gravity value and animation counter in the game is "per frame", and the game
# felt right on a slow machine that managed about this many frames per second. The original
# code asked for 70 (clock.tick(70)); fast machines reach that, so the game ran too fast.
TUNED_FPS = 40
STEP_MS = 1000 / TUNED_FPS
# ponytail: if even logic-only frames can't keep up, the game slows down instead of freezing.
MAX_CATCH_UP = 5


def run(clock, keep_running, frame):
    """Core game loop: one game frame per 1/TUNED_FPS seconds, on fast and slow machines.

    Fast machine: tick() waits, so this is a plain frame cap at TUNED_FPS.
    Slow machine: frames take longer than STEP_MS, so the loop runs extra frames
    without drawing them (frame(render=False)) until the game has caught up.
    """
    clock.tick()  # start timing now, not when the level was being built
    behind = 0.0  # milliseconds of game time owed to the player (rounded to whole frames)
    while keep_running():
        behind += clock.tick(TUNED_FPS) - STEP_MS
        behind = max(-STEP_MS / 2, min(behind, STEP_MS * MAX_CATCH_UP))
        frame()
        while behind >= STEP_MS / 2 and keep_running():
            frame(render=False)
            behind -= STEP_MS

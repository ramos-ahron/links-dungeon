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


def run(clock, fps, keep_running, frame):
    """Core game loop: cap the frame rate, then run one frame of the level."""
    while keep_running():
        clock.tick(fps)
        frame()

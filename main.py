"""Link's Dungeon - entry point.

Run from the project folder with:  python main.py
"""
import pygame

from game import loop, state as game_state
from game.levels import parkour


def main():
    """Start the game: parkour level, then the boss room, then the credits."""
    loop.init_display()
    game_state.init()
    parkour.run()
    pygame.quit()


if __name__ == "__main__":
    main()

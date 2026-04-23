"""Link's Dungeon - entry point.

Run from the project folder with:  python main.py
"""
import pygame

from game import loop, state as game_state
from game.levels import boss, parkour


def print_credits():
    """Print the closing credits."""
    print("""
This game is made by:
    Marcus Reid &
    Ahron Ramos

Thanks for playing our game!!!
""")


def main():
    """Start the game: parkour level, then the boss room, then the credits."""
    loop.init_display()
    game_state.init()
    parkour.setup()
    parkour.run()
    boss.setup()
    boss.run()
    print_credits()
    pygame.quit()


if __name__ == "__main__":
    main()

"""Gravity, world scrolling and the endless background.
"""
from game.state import state


def reset_speeds_and_gravity():
    """Reset scroll speeds and set parkour gravity (no gravity once the player is dead)."""
    state.backgroundSpeed = 1
    state.groundSpeed = 4
    if state.health != 0:
        state.gravity = 0.12
    else:
        state.gravity = 0
        state.yVelocity = 0


def apply_gravity():
    """Add gravity to the vertical speed and move the player."""
    state.yVelocity += state.gravity
    state.player.move(0,state.yVelocity)

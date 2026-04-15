"""Shared game state.

The original game was one script with ~300 global variables. To split it into
modules without changing behaviour, every one of those globals now lives on the
single `state` object below (`health` became `state.health`, and so on).
"""
from types import SimpleNamespace

import pygame


state = SimpleNamespace()


def init():
    """Create every game variable with its starting value."""
    state.clock = pygame.time.Clock()
    state.all_sprites1 = pygame.sprite.Group()
    state.boundaries = []
    state.background = []
    state.ground = []
    state.character = []
    state.yVelocity = 0
    state.gravity = 0.9  # never used: each level overwrites gravity every frame (physics.py)
    state.backgroundPosition = 799
    state.groundPosition = 790
    state.backgroundSpeed = 1
    state.groundSpeed = 4
    state.health = 10
    state.parkour_enemies = True
    state.countdowned = True
    state.a_collision = False
    state.e_a_collision = False
    state.playerRight = False
    state.playerLeft = False
    state.side_collision = False
    state.defend = False
    state.bottom = False
    state.collision = False
    state.playerUp = False
    state.playerDown = False
    state.extra_gravity = False
    state.enemy1_stop_left = False
    state.enemy1_stop_right = False

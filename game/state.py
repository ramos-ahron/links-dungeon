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
    state.health = 10
    state.parkour_enemies = True

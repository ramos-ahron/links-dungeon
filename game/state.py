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
    state.all_sprites2 = pygame.sprite.Group()
    state.boundaries = []
    state.background = []
    state.ground = []
    state.wall = []
    state.c_wall = []
    state.character = []
    state.spike= []
    state.enemy = []
    state.doors = []
    state.yVelocity = 0
    state.gravity = 0.9  # never used: each level overwrites gravity every frame (physics.py)
    state.backgroundPosition = 799
    state.background_position = 799
    state.groundPosition = 790
    state.ground_position = 790
    state.backgroundSpeed = 1
    state.background_speed = 1
    state.norm_speed = 4
    state.groundSpeed = 4
    state.shield_count = 0
    state.stamina_count = 0
    state.arrows_taken = 0
    state.death_counter = 0
    state.damage_counter = 0
    state.damage_count = 0
    state.over = 0
    state.health = 10
    state.shield = 10
    state.stamina = 10
    state.speed = 2
    state.player_health = 100
    state.player_shield = 100
    state.player_stamina = 100
    state.parkour_enemies = True
    state.countdowned = True
    state.a_collision = False
    state.e_a_collision = False
    state.credit = False
    state.playerRight = False
    state.playerLeft = False
    state.jump = False
    state.attack = False
    state.side_collision = False
    state.defend = False
    state.bottom = False
    state.collision = False
    state.playerUp = False
    state.playerDown = False
    state.facingLeft = False
    state.facingRight = True
    state.extra_gravity = False
    state.spike_collision = False
    state.damage_check = False
    state.enemy1_stop_left = False
    state.enemy1_stop_right = False

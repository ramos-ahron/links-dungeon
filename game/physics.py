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


def scroll_world():
    """Move the world (not the player) left or right while walking, jumping or hanging."""
    if state.playerRight and not state.bottom and not state.playerLeft:
        if not state.collision and not state.attack:
            state.player.imageStartEnd(18,19,10)
        state.facingRight = True
        state.facingLeft = False
        for bound in state.boundaries:
            bound.move(-state.groundSpeed,0)
        for back in state.background:
            back.move(-state.background_speed,0)
        for grounds in state.ground:
            grounds.move(-state.norm_speed,0)
        for walls in state.wall:
            walls.move(-state.norm_speed,0)
        for c_walls in state.c_wall:
            c_walls.move(-state.norm_speed,0)
        for spikes in state.spike:
            spikes.move(-state.norm_speed,0)
        for enemies in state.enemy:
            enemies.move(-state.norm_speed,0)
        # `door` stays on state: the original used this global name both in this loop and outside it.
        for state.door in state.doors:
            state.door.move(-state.norm_speed,0)
    elif state.playerLeft and not state.bottom and not state.playerRight:
        if not state.collision and not state.attack:
            state.player.imageStartEnd(20,21,10)
        state.facingLeft = True
        state.facingRight = False
        for bound in state.boundaries:
            bound.move(state.groundSpeed,0)
        for back in state.background:
            back.move(state.background_speed,0)
        for grounds in state.ground:
            grounds.move(state.norm_speed,0)
        for walls in state.wall:
            walls.move(state.norm_speed,0)
        for c_walls in state.c_wall:
            c_walls.move(state.norm_speed,0)
        for spikes in state.spike:
            spikes.move(state.norm_speed,0)
        for enemies in state.enemy:
            enemies.move(state.norm_speed,0)
        # `door` stays on state: the original used this global name both in this loop and outside it.
        for state.door in state.doors:
            state.door.move(state.norm_speed,0)
    if state.playerLeft and state.bottom and not state.playerRight:
        state.player.imageStartEnd(51,54,5)
        state.facingLeft = True
        state.facingRight = False
        for bound in state.boundaries:
            bound.move(state.background_speed,0)
        for back in state.background:
            back.move(state.background_speed,0)
        for grounds in state.ground:
            grounds.move(state.norm_speed,0)
        for walls in state.wall:
            walls.move(state.norm_speed,0)
        for c_walls in state.c_wall:
            c_walls.move(state.norm_speed,0)
        for spikes in state.spike:
            spikes.move(state.norm_speed,0)
        for enemies in state.enemy:
            enemies.move(state.norm_speed,0)
        # `door` stays on state: the original used this global name both in this loop and outside it.
        for state.door in state.doors:
            state.door.move(state.norm_speed,0)
    elif state.playerRight and state.bottom and not state.playerLeft:
        state.player.imageStartEnd(47,50,5)
        state.facingRight = True
        state.facingLeft = False
        for bound in state.boundaries:
            bound.move(-state.groundSpeed,0)
        for back in state.background:
            back.move(-state.background_speed,0)
        for grounds in state.ground:
            grounds.move(-state.norm_speed,0)
        for walls in state.wall:
            walls.move(-state.norm_speed,0)
        for c_walls in state.c_wall:
            c_walls.move(-state.norm_speed,0)
        for spikes in state.spike:
            spikes.move(-state.norm_speed,0)
        for enemies in state.enemy:
            enemies.move(-state.norm_speed,0)
        # `door` stays on state: the original used this global name both in this loop and outside it.
        for state.door in state.doors:
            state.door.move(-state.norm_speed,0)


def apply_gravity():
    """Add gravity to the vertical speed and move the player."""
    state.yVelocity += state.gravity
    state.player.move(0,state.yVelocity)


def wrap_background():
    """Loop the two background and floor tiles so they scroll forever."""
    if state.back1.getX() < -800:
        state.back1.setPosition(state.background_position, 0)
    if state.back2.getX() < -800:
        state.back2.setPosition(state.background_position, 0)
    if state.back1.getX() > 800:
        state.back1.setPosition(-state.background_position, 0)
    if state.back2.getX() > 800:
        state.back2.setPosition(-state.background_position, 0)
    if state.ground1.getX() < -800:
        state.ground1.setPosition(state.ground_position, 460)
    if state.ground2.getX() < -800:
        state.ground2.setPosition(state.ground_position, 460)
    if state.ground1.getX() > 800:
        state.ground1.setPosition(-state.ground_position, 460)
    if state.ground2.getX() > 800:
        state.ground2.setPosition(-state.ground_position, 460)


def set_boss_room_gravity():
    """Set boss-room gravity (no gravity once the player is dead)."""
    if state.health != 0:
        state.gravity = 0.095
    else:
        state.gravity = 0
        state.yVelocity = 0

"""The player: sprite and animation frames, stats, damage/death, collisions with terrain, attacks.
"""
from game.sprite import Sprite
from game.state import state


def create_player():
    """Create the player sprite with all its animation frames, and the stats panel."""
    state.player = Sprite(50,50,None,"walking_right_00.png")
    state.player.addImage("walking_right_01.png")
    state.player.addImage("walking_right_02.png")
    state.player.addImage("walking_right_03.png")
    state.player.addImage("walking_right_04.png")
    state.player.addImage("walking_right_05.png")
    state.player.addImage("walking_right_06.png")
    state.player.addImage("walking_right_07.png")
    state.player.addImage("walking_right_08.png")
    state.player.addImage("walking_left_00.png")
    state.player.addImage("walking_left_01.png")
    state.player.addImage("walking_left_02.png")
    state.player.addImage("walking_left_03.png")
    state.player.addImage("walking_left_04.png")
    state.player.addImage("walking_left_05.png")
    state.player.addImage("walking_left_06.png")
    state.player.addImage("walking_left_07.png")
    state.player.addImage("walking_left_08.png")
    state.player.addImage("jumping_right_00.png")
    state.player.addImage("jumping_right_01.png")
    state.player.addImage("jumping_left_00.png")
    state.player.addImage("jumping_left_01.png")
    state.player.addImage("left_attack_00.png")
    state.player.addImage("left_attack_01.png")
    state.player.addImage("left_attack_02.png")
    state.player.addImage("left_attack_03.png")
    state.player.addImage("left_attack_04.png")
    state.player.addImage("right_attack_00.png")
    state.player.addImage("right_attack_01.png")
    state.player.addImage("right_attack_02.png")
    state.player.addImage("right_attack_03.png")
    state.player.addImage("right_attack_04.png")
    state.player.addImage("link_idle_00.png")
    state.player.addImage("falling_idle_00.png")
    state.player.addImage("falling_idle_01.png")
    state.player.addImage("climbing_right_00.png")
    state.player.addImage("climbing_right_01.png")
    state.player.addImage("climbing_right_02.png")
    state.player.addImage("climbing_left_00.png")
    state.player.addImage("climbing_left_01.png")
    state.player.addImage("climbing_left_02.png")
    state.player.addImage("climbing_right_02.png")
    state.player.addImage("climbing_right_01.png")
    state.player.addImage("climbing_right_00.png")
    state.player.addImage("climbing_left_02.png")
    state.player.addImage("climbing_left_01.png")
    state.player.addImage("climbing_left_00.png")
    state.player.addImage("hanging_right_00.png")
    state.player.addImage("hanging_right_01.png")
    state.player.addImage("hanging_right_02.png")
    state.player.addImage("hanging_right_03.png")
    state.player.addImage("hanging_left_00.png")
    state.player.addImage("hanging_left_01.png")
    state.player.addImage("hanging_left_02.png")
    state.player.addImage("hanging_left_03.png")
    state.player.addImage("hanging_idle_00.png")
    state.player.addImage("defend_right_00.png")
    state.player.addImage("defend_right_01.png")
    state.player.addImage("defend_right_02.png")
    state.player.addImage("defend_right_03.png")
    state.player.addImage("defend_right_04.png")
    state.player.addImage("defend_right_05.png")
    state.player.addImage("defend_right_06.png")
    state.player.addImage("defend_right_07.png")
    state.player.addImage("defend_right_08.png")
    state.player.addImage("defend_left_00.png")
    state.player.addImage("defend_left_01.png")
    state.player.addImage("defend_left_02.png")
    state.player.addImage("defend_left_03.png")
    state.player.addImage("defend_left_04.png")
    state.player.addImage("defend_left_05.png")
    state.player.addImage("defend_left_06.png")
    state.player.addImage("defend_left_07.png")
    state.player.addImage("defend_left_08.png")
    state.player.addImage("shooting_right_00.png")
    state.player.addImage("shooting_right_01.png")
    state.player.addImage("shooting_right_02.png")
    state.player.addImage("shooting_left_00.png")
    state.player.addImage("shooting_left_01.png")
    state.player.addImage("shooting_left_02.png")
    state.player.addImage("link_death_ani_00.png")
    state.player.addImage("link_death_ani_01.png")
    state.player.addImage("link_death_ani_02.png")
    state.player.addImage("link_death_ani_03.png")
    state.player.addImage("link_death_ani_04.png")
    state.player.addImage("link_damage_left_00.png")
    state.player.addImage("link_damage_right_00.png")
    state.player.setPosition(325,0)
    state.character.append(state.player)


def collide_with_ground():
    """Player vs ground blocks: stop at sides, land on top, jump, defend and attack (sword/bow)."""
    for i in state.ground:
        if (i.getY() <= state.player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= state.player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= state.player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() + i.getWidth() - 10 <= state.player.getX() <= i.getX() + i.getWidth() + 2:
            state.playerLeft = False
        elif (i.getY() <= state.player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= state.player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= state.player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() - 2 <= state.player.getX() + state.player.getWidth() <= i.getX() + 10:
            state.playerRight = False
        elif (i.getX() <= state.player.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= state.player.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= state.player.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= state.player.getY() + state.player.getHeight() <= i.getY() + 10:
            if state.playerLeft:
                state.player.imageStartEnd(9,17,5)
            elif state.playerRight:
                state.player.imageStartEnd(0,8,5)
            state.collision = True
            state.bottom = False
            state.yVelocity = 0
            state.playerDown = False
            if state.jump:
                state.yVelocity = -3
        elif (i.getX() <= state.player.getX() + 25 <= i.getX() + i.getWidth() or i.getX() <= state.player.getX() + 15 <= i.getX() + i.getWidth() or i.getX() <= state.player.getX() + 35 <= i.getX() + i.getWidth()) and i.getY() + i.getHeight() - 10 <= state.player.getY() <= i.getY() + i.getHeight() + 2:
            state.playerUp = False
            state.yVelocity += 1


def collide_with_walls():
    """Player vs normal walls: same rules as the ground."""
    for i in state.wall:
        if (i.getY() <= state.player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= state.player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= state.player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() + i.getWidth() - 10 <= state.player.getX() <= i.getX() + i.getWidth() + 2:
            state.playerLeft = False
        elif (i.getY() <= state.player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= state.player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= state.player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() - 2 <= state.player.getX() + state.player.getWidth() <= i.getX() + 10:
            state.playerRight = False
        elif (i.getX() <= state.player.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= state.player.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= state.player.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= state.player.getY() + state.player.getHeight() <= i.getY() + 10:
            if state.playerLeft:
                state.player.imageStartEnd(9,17,5)
            elif state.playerRight:
                state.player.imageStartEnd(0,8,5)
            state.collision = True
            state.bottom = False
            state.yVelocity = 0
            state.playerDown = False
            if state.jump:
                state.yVelocity = -3
        elif (i.getX() <= state.player.getX() + 25 <= i.getX() + i.getWidth() or i.getX() <= state.player.getX() + 15 <= i.getX() + i.getWidth() or i.getX() <= state.player.getX() + 35 <= i.getX() + i.getWidth()) and i.getY() + i.getHeight() - 10 <= state.player.getY() <= i.getY() + i.getHeight() + 2:
            state.playerUp = False
            state.yVelocity += 1


def update_idle_pose():
    """Pick the idle or defend frame when the player isn't moving."""
    if state.player_health != 0:
        if not state.playerRight and not state.playerLeft and state.bottom and not state.damage_check:
            state.player.setImageIndex(55)
        elif not state.playerRight and not state.playerLeft and not state.bottom and not state.attack and not state.collision and not state.side_collision and not state.damage_check:
            state.player.setImageIndex(55)

"""Boss level: the mace knight fight and the trophy.
"""
import pygame

from game import loop, physics, player
from game.sprite import Sprite
from game.loop import add_text
from game.state import state


def setup_boss_room():
    """Create the boss, its attack ranges and the boss-room variables."""
    state.maces = []
    state.chains = []
    state.o_chains = []
    state.chained = []
    state.arrows = []
    state.boss = Sprite(100,100,None, "mace_knight_right_idle.png")
    state.boss.addImage("mace_knight_left_idle.png")
    state.boss.addImage("boss_walking_right_00.png")
    state.boss.addImage("boss_walking_right_01.png")
    state.boss.addImage("boss_walking_right_02.png")
    state.boss.addImage("boss_walking_left_00.png")
    state.boss.addImage("boss_walking_left_01.png")
    state.boss.addImage("boss_walking_left_02.png")
    state.boss.addImage("boss_attack_left_00.png")
    state.boss.addImage("boss_attack_left_01.png")
    state.boss.addImage("boss_attack_left_02.png")
    state.boss.addImage("boss_attack_left_03.png")
    state.boss.addImage("boss_attack_right_00.png")
    state.boss.addImage("boss_attack_right_01.png")
    state.boss.addImage("boss_attack_right_02.png")
    state.boss.addImage("boss_attack_right_03.png")
    state.boss.addImage("mace_knight_idle.png")
    state.boss.addImage("boss_death_animation_00.png")
    state.boss.addImage("boss_death_animation_01.png")
    state.boss.addImage("boss_death_animation_02.png")
    state.boss.addImage("boss_death_animation_03.png")
    state.boss.addImage("boss_death_animation_04.png")
    state.boss.addImage("boss_death_animation_05.png")
    state.boss.addImage("boss_death_animation_06.png")
    state.boss.setPosition(300,360)
    state.boss_clock = pygame.time.Clock()
    state.t_yVelocity = 0
    state.boss_count1 = 0
    state.boss_death_animation = 0
    state.mace_attack_count = 0
    state.mace_stop = 0
    state.mace_speed = 0
    state.chain_position = 15
    state.winner_text = 0
    state.chain_position1 = 0
    state.chain_appearance = 0
    state.chain_appearance1 = 0
    state.damage_count = 0
    state.damage_count1 = 0
    state.damage_count2 = 0
    state.damage_check_count = 0
    state.chain_distance = 10
    state.chain_distance1 = 10
    state.chain_attack_count = 0
    state.mace_attempts = 0
    state.boss_fighting_animation = 0
    state.boss_death_animation = 0
    state.player_win_count = 0
    state.chain_speed = 0
    state.chain_count = 0
    state.weapon = 1
    state.shield = 10
    state.stamina = 10
    state.player_shield = 100
    state.player_stamina = 100
    state.boss_health = 625
    state.boss_facing_left = False
    state.trophy_up = False
    state.boss_facing_right = False
    state.boss_battle_start = False
    state.mace_rebound = False
    state.mace_reattack = False
    state.chain_appeared = False
    state.chain_rebound = False
    state.boss_range_collision = False
    state.mace_away = False
    state.chain_away = False
    state.not_mace = False
    state.attack = False
    state.damage_check = False
    state.winner = False
    state.a_collision = False
    state.boss_range1 = Sprite(50,100,[255,0,0])
    state.boss_range2 = Sprite(50,100,[255,0,0])
    state.boss_range3 = Sprite(75,100,[0,0,255])
    state.boss_range4 = Sprite(75,100,[0,0,255])
    state.boss_range5 = Sprite(100,100,[0,255,0])
    state.boss_range6 = Sprite(100,100,[0,255,0])
    state.boss_range7 = Sprite(50,100,[255,0,0])
    state.boss_range8 = Sprite(50,100,[255,0,0])
    state.boss_body = Sprite(50,75,[0,255,0])
    state.player.setPosition(0,410)
    state.ground1.setPosition(0, 460)
    state.bound7.setPosition(-300,0)
    state.bound8.setPosition(800,0)
    state.all_sprites3.add(state.back3,state.ground1,state.boss,state.player)


def update_boss_ranges():
    """Keep the boss's attack and detection boxes around it."""
    if state.boss_health != 0:
        state.boss_range1.setPosition(state.boss.getX() - 25,state.boss.getY())
        state.boss_range2.setPosition(state.boss.getX() + state.boss.getWidth() - 25, state.boss.getY())
        state.boss_range3.setPosition(state.boss.getX() - 100,state.boss.getY())
        state.boss_range4.setPosition(state.boss.getX() + state.boss.getWidth() + 25,state.boss.getY())
        state.boss_range5.setPosition(state.boss.getX() - 200,state.boss.getY())
        state.boss_range6.setPosition(state.boss.getX() + state.boss.getWidth() + 100,state.boss.getY())
        state.boss_range7.setPosition(state.boss.getX() - 250,state.boss.getY())
        state.boss_range8.setPosition(state.boss.getX() + state.boss.getWidth() + 200,state.boss.getY())
        state.boss_body.setPosition(state.boss.getX() + 20, state.boss.getY() + 25)


def draw():
    """Draw the boss room, the player's stat bars and the boss health bar."""
    state.screen.fill([0, 0, 0])
    state.all_sprites3.draw(state.screen)
    pygame.draw.rect(state.screen,[255,0,0],[27,10,state.player_health,15])
    pygame.draw.rect(state.screen,[211,211,211],[27,25,state.player_shield,15])
    pygame.draw.rect(state.screen,[0,0,255],[27,43,state.player_stamina,15])
    state.all_sprites2.draw(state.screen)
    if state.boss_health > 0:
        pygame.draw.rect(state.screen,[0,0,0],[150,30,625,40])
        pygame.draw.rect(state.screen,[255,0,0],[150,30,state.boss_health,40])
    add_text(str(state.health) + " / 10",[57,10],24,[255,255,255])
    add_text(str(state.shield) + " / 10",[57,27],24,[255,0,0])
    add_text(str(state.stamina) + " / 10",[57,45],23,[255,255,255])
    pygame.display.update()


def reset_frame_flags():
    """Clear the per-frame collision flags."""
    state.collision = False
    state.defend = False
    state.bottom = False
    state.side_collision = False
    state.enemy1_stop_left = False
    state.enemy1_stop_right = False
    state.boss_range_collision = False
    state.mace_reattack = True
    state.a_collision = False


def check_room_bounds():
    """Stop the player at the edges of the boss room."""
    if state.player.collision(state.bound3):
        state.playerLeft = False
    elif state.player.collision(state.bound4):
        state.playerRight = False


def face_player():
    """Turn the boss toward the player, block the player, start the fight on the first hit."""
    if state.player.getX() + (state.player.getWidth() / 2) > state.boss.getX() + (state.boss.getWidth() / 2):
        state.boss_facing_right = True
        state.boss_facing_left = False
        if not state.boss_battle_start:
            state.boss.setImageIndex(0)
    elif state.player.getX() + (state.player.getWidth() / 2) <= state.boss.getX() + (state.boss.getWidth() / 2):
        state.boss_facing_left = True
        state.boss_facing_right = False
        if not state.boss_battle_start:
            state.boss.setImageIndex(1)
    if state.boss_health > 0:
        if state.boss.getY() <= state.player.getY() - 10 <= state.boss.getY() + state.boss.getHeight() and state.boss.getX() + state.boss.getWidth() - 20 <= state.player.getX() <= state.boss.getX() + state.boss.getWidth() - 10:
            state.playerLeft = False
        elif state.boss.getY() <= state.player.getY() - 10  <= state.boss.getY() + state.boss.getHeight() and state.boss.getX() + 10 <= state.player.getX() + state.player.getWidth() <= state.boss.getX() + 20:
            state.playerRight = False
    if (state.boss.collision(state.player_range1) or state.boss.collision(state.player_range2)) and state.attack and not state.boss_battle_start:
        state.boss_battle_start = True


def update_boss_death():
    """Boss death animation, then drop the trophy."""
    if state.boss_health < 0:
        state.boss_health = 0
    if state.boss_health == 0:
        state.boss_death_animation += 1
        if state.boss_death_animation == 1:
            state.boss.setImageIndex(17)
        if state.boss_death_animation == 15:
            state.boss.setImageIndex(18)
        if state.boss_death_animation == 30:
            state.boss.setImageIndex(19)
        if state.boss_death_animation == 45:
            state.boss.setImageIndex(20)
        if state.boss_death_animation == 60:
            state.boss.setImageIndex(21)
        if state.boss_death_animation == 75:
            state.boss.setImageIndex(22)
        if state.boss_death_animation == 90:
            state.boss.setImageIndex(23)
        if state.boss_death_animation == 105:
            state.all_sprites3.remove(state.boss)
            state.trophy = Sprite(50,50,None,"trophy_texture_01.png")
            state.trophy.setPosition(state.boss.getX(), state.boss.getY())
            state.all_sprites3.add(state.trophy)
    if state.health == 0:
        state.boss.setImageIndex(16)


def update_boss_attacks():
    """Boss AI: mace swing up close, walk toward the player, chain grab, mace throw from far."""
    if state.boss_health != 0 and state.health != 0:
        if state.boss_battle_start:
            if state.player.collision(state.boss_range1) and not state.player.collision(state.boss_range3) and not state.mace_away and not state.chain_away:
                state.boss_fighting_animation += 1
                if state.boss_fighting_animation == 1:
                    state.boss.setImageIndex(8)
                if state.boss_fighting_animation == 5:
                    state.boss.setImageIndex(9)
                if state.boss_fighting_animation == 10:
                    state.boss.setImageIndex(10)
                if state.boss_fighting_animation == 15:
                    state.boss.setImageIndex(11)
                    if state.player_shield > 0:
                        state.player_shield -= 30
                        state.shield -= 3
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
                    state.damage_check = True
                if state.boss_fighting_animation == 20:
                    state.boss.setImageIndex(1)
                if state.boss_fighting_animation == 45:
                    state.boss_fighting_animation = 0
                state.not_mace = True
            elif state.player.collision(state.boss_range2) and not state.player.collision(state.boss_range4) and not state.mace_away and not state.chain_away:
                state.boss_fighting_animation += 1
                if state.boss_fighting_animation == 1:
                    state.boss.setImageIndex(12)
                if state.boss_fighting_animation == 5:
                    state.boss.setImageIndex(13)
                if state.boss_fighting_animation == 10:
                    state.boss.setImageIndex(14)
                if state.boss_fighting_animation == 15:
                    state.boss.setImageIndex(15)
                    if state.player_shield > 0:
                        state.player_shield -= 30
                        state.shield -= 3
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
                    state.damage_check = True
                if state.boss_fighting_animation == 20:
                    state.boss.setImageIndex(0)
                if state.boss_fighting_animation == 45:
                    state.boss_fighting_animation = 0
                state.not_mace = True
            elif not state.player.collision(state.boss_range1) or not state.player.collision(state.boss_range2) and not state.mace_away and not state.chain_away:
                state.boss_fighting_animation = 0
            if state.player.collision(state.boss_range3) and not state.player.collision(state.boss_range5) and not state.mace_away and not state.chain_away:
                state.boss.move(-3,0)
                state.boss.imageStartEnd(5,7,5)
                state.not_mace = True
            elif state.player.collision(state.boss_range4) and not state.player.collision(state.boss_range6) and not state.mace_away and not state.chain_away:
                state.boss.move(3,0)
                state.boss.imageStartEnd(2,4,5)
                state.not_mace = True
            if state.player.collision(state.boss_range5) and not state.mace_away:
                state.chain_attack_count += 1
                if state.boss_facing_left:
                    if state.chain_attack_count < 0:
                        state.boss.move(-2,0)
                        state.boss.imageStartEnd(5,7,5)
                    if state.chain_attack_count == 1:
                        state.chain = Sprite(20,20,None, "chain_texture_00.png")
                        state.chain.setPosition(state.boss_body.getX(), state.boss_body.getY() + 40)
                        state.chain_speed = -5
                        state.chain.xSpeed = state.chain_speed
                        state.chained.append(state.chain)
                        state.all_sprites3.add(state.chain)
                        state.boss.setImageIndex(1)
                        state.chain_away = True
            if state.player.collision(state.boss_range6) and not state.mace_away:
                state.chain_attack_count += 1
                if state.boss_facing_right:
                    if state.chain_attack_count < 0:
                        state.boss.move(2,0)
                        state.boss.imageStartEnd(2,4,5)
                    if state.chain_attack_count == 1:
                        state.chain = Sprite(20,20,None, "chain_texture_00.png")
                        state.chain.setPosition(state.boss_body.getX() + state.boss_body.getWidth() , state.boss_body.getY() + 40)
                        state.chain_speed = 5
                        state.chain.xSpeed = state.chain_speed
                        state.chained.append(state.chain)
                        state.all_sprites3.add(state.chain)
                        state.boss.setImageIndex(0)
                        state.chain_away = True
            if state.mace_reattack and not state.player.collision(state.boss_range1) and not state.player.collision(state.boss_range2) and not state.player.collision(state.boss_range3) and not state.player.collision(state.boss_range4) and not state.player.collision(state.boss_range5) and not state.player.collision(state.boss_range6) and not state.chain_away:
                state.mace_attack_count += 1
                if state.boss_facing_left:
                    if state.mace_attack_count == 1:
                        state.mace = Sprite(36,36,None,"mace_texture_left.png")
                        state.mace.setPosition(state.boss_body.getX() , state.boss_body.getY() + 25)
                        state.mace_speed = -5
                        state.mace.xSpeed = state.mace_speed
                        state.maces.append(state.mace)
                        state.all_sprites3.add(state.mace)
                        state.boss.setImageIndex(1)
                        state.damage_chack1 = 0
                        state.mace_reattack = False
                        state.mace_away = True
                    if state.mace_attack_count >= 20 and state.mace_attack_count <= 80:
                        state.boss.move(-2,0)
                        state.boss.imageStartEnd(5,7,5)
                if state.boss_facing_right:
                    if state.mace_attack_count == 1:
                        state.mace = Sprite(36,36,None,"mace_texture_right.png")
                        state.mace.setPosition(state.boss_body.getX() + state.boss_body.getWidth(), state.boss_body.getY() + 25)
                        state.mace_speed = 5
                        state.mace.xSpeed = state.mace_speed
                        state.maces.append(state.mace)
                        state.all_sprites3.add(state.mace)
                        state.damage_check1 = 0
                        state.boss.setImageIndex(0)
                        state.mace_reattack = False
                        state.mace_away = True
                    if state.mace_attack_count >= 20 and state.mace_attack_count <= 80:
                        state.boss.move(2,0)
                        state.boss.imageStartEnd(2,4,5)


def player_on_floor():
    """Player vs boss-room floor: land, jump, defend and attack the boss."""
    for i in state.ground:
        if (i.getX() <= state.player.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= state.player.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= state.player.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= state.player.getY() + state.player.getHeight() <= i.getY() + 10:
            if state.playerLeft:
                state.player.imageStartEnd(9,17,5)
                if not state.attack:
                    state.player_count = 0
            elif state.playerRight:
                state.player.imageStartEnd(0,8,5)
                if not state.attack:
                    state.player_count = 0
            state.collision = True
            state.bottom = False
            state.yVelocity = 0
            state.playerDown = False
            if state.jump:
                state.yVelocity = -3
                if not state.attack:
                    state.player_count = 0
            if state.defend:
                if state.facingLeft:
                    state.player.setImageIndex(65)
                if state.facingRight:
                    state.player.setImageIndex(56)
                if not state.attack:
                    state.player_count = 0
            if state.attack and not state.winner:
                state.player_count += 1
                state.jump = False
                state.playerRight = False
                state.playerLeft = False
                if state.weapon == 1:
                    if state.facingLeft:
                        if state.player_count == 1:
                            state.player.setImageIndex(22)
                        if state.player_count == 10:
                            state.player.setImageIndex(23)
                        if state.player_count == 20:
                            state.player.setImageIndex(24)
                        if state.player_count == 30:
                           state.player.setImageIndex(25)
                        if state.player_count == 40:
                            state.player.setImageIndex(26)
                            if state.player_range1.collision(state.boss):
                                state.boss_health -= 10
                            state.player_count = 0
                            state.attack = False
                    if state.facingRight:
                        if state.player_count == 1:
                            state.player.setImageIndex(27)
                        if state.player_count == 10:
                            state.player.setImageIndex(28)
                        if state.player_count == 20:
                            state.player.setImageIndex(29)
                        if state.player_count == 30:
                           state.player.setImageIndex(30)
                        if state.player_count == 40:
                            state.player.setImageIndex(31)
                            if state.player_range2.collision(state.boss):
                                state.boss_health -= 10
                            state.player_count = 0
                            state.attack = False
                if state.weapon == 2:
                    if state.stamina > 0:
                        if state.facingLeft:
                            if state.player_count == 1:
                                state.player.setImageIndex(77)
                            if state.player_count == 15:
                                state.player.setImageIndex(78)
                            if state.player_count == 30:
                                state.player.setImageIndex(79)
                                state.player_count = 0
                                state.attack = False
                                state.arrow = Sprite(30,12,None,"arrow_left_00.png")
                                state.arrow.xSpeed = -state.groundSpeed - 2
                                state.arrow.setPosition(state.player.getX() - 30, state.player.getY() + (state.player.getWidth() / 2) - 5)
                                state.arrows.append(state.arrow)
                                state.all_sprites3.add(state.arrow)
                                state.player_stamina -= 10
                                state.stamina_count = 0
                                state.stamina -= 1
                        if state.facingRight:
                            if state.player_count == 1:
                                state.player.setImageIndex(74)
                            if state.player_count == 15:
                                state.player.setImageIndex(75)
                            if state.player_count == 30:
                                state.player.setImageIndex(76)
                                state.player_count = 0
                                state.attack = False
                                state.arrow = Sprite(30,12,None,"arrow_right_00.png")
                                state.arrow.xSpeed = state.groundSpeed + 2
                                state.arrow.setPosition(state.player.getX() + state.player.getWidth(), state.player.getY() + (state.player.getWidth() / 2) - 5)
                                state.arrows.append(state.arrow)
                                state.all_sprites3.add(state.arrow)
                                state.player_stamina -= 10
                                state.stamina -= 1
                                state.stamina_count = 0
                    else:
                        state.player_count = 0
                        state.attack = False


def move_player():
    """Walk the player (in the boss room the player moves, not the world)."""
    if state.playerRight and not state.bottom and not state.playerLeft:
        if not state.collision and not state.attack:
            state.player.imageStartEnd(18,19,10)
        state.facingRight = True
        state.facingLeft = False
        state.player.move(4,0)
    elif state.playerLeft and not state.bottom and not state.playerRight:
        if not state.collision and not state.attack:
            state.player.imageStartEnd(20,21,10)
        state.facingLeft = True
        state.facingRight = False
        state.player.move(-4,0)


def drop_trophy():
    """Let the trophy fall to the floor."""
    if state.boss_health == 0 and state.health != 0 and state.boss_death_animation > 105:
        state.t_yVelocity += state.gravity
        state.trophy.move(0,state.t_yVelocity)
        if state.trophy.collision(state.ground1):
            state.t_yVelocity = 0


def update_player_arrows():
    """Move the player's arrows; damage the boss (and start the fight) on hit."""
    # `arrow` stays on state: the original used this global name both in this loop and outside it.
    for state.arrow in state.arrows:
        state.arrow.move(state.arrow.xSpeed,0)
        if state.arrow.collision(state.bound5) or state.arrow.collision(state.bound6):
            state.all_sprites3.remove(state.arrow)
            state.arrow.move(0, 0)
            state.arrow.setPosition(0, 0)
            state.arrows.remove(state.arrow)
        if state.arrow.collision(state.boss):
            if not state.boss_battle_start:
                state.boss_battle_start = True
            state.boss_health -= 10
            state.all_sprites3.remove(state.arrow)
            state.arrow.move(0, 0)
            state.arrow.setPosition(0, 0)
            state.arrows.remove(state.arrow)


def update_chain_grab():
    """Chain attack: fly out, pull the player back, return to the boss."""
    # `chain` stays on state: the original used this global name both in this loop and outside it.
    for state.chain in state.chained:
        state.chain.move(state.chain.xSpeed,0)
        if state.chain.getX() + state.chain.getWidth() < state.boss_body.getX() and state.boss_facing_left:
            state.chain_appearance1 += 1
            if state.chain_appearance1 == 2:
                state.other_chain = Sprite(20,20,None,"chain_texture_00.png")
                state.other_chain.setPosition(state.chain.getX() + state.chain.getWidth() + state.chain_position1,state.chain.getY())
                state.o_chains.append(state.other_chain)
                state.all_sprites3.add(state.other_chain)
                state.chain_position1 += 15
                state.chain_appearance1 = 0
                if state.other_chain.getX() + state.other_chain.getWidth() > state.boss_body.getX():
                    state.chain_position1 -= 15
        if state.chain.getX() > state.boss_body.getX() + state.boss_body.getWidth() and state.boss_facing_right:
            state.chain_appearance1 += 1
            if state.chain_appearance1 == 2:
                state.other_chain = Sprite(20,20,None,"chain_texture_00.png")
                state.other_chain.setPosition(state.chain.getX() + state.chain_position1, state.chain.getY())
                state.o_chains.append(state.other_chain)
                state.all_sprites3.add(state.other_chain)
                state.chain_position1 -= 15
                state.chain_appearance1 = 0
                if state.other_chain.getX() < state.boss_body.getX() + state.boss_body.getWidth():
                    state.chain_position1 += 15
        if state.chain.collision(state.boss_range7) or state.chain.collision(state.boss_range8):
            state.chain.xSpeed = 0
            state.chain_speed *= -1
            state.chain.xSpeed = state.chain_speed
            state.chain_rebound = True
        if state.chain.collision(state.player):
            state.playerLeft = False
            state.playerRight = False
            state.jump = False
            state.chain_count += 1
            if state.chain_count == 1:
                if not state.chain_rebound:
                    state.chain.xSpeed = 0
                    state.chain_speed *= -1
                    state.chain.xSpeed = state.chain_speed
                    state.chain_rebound = True
                state.damage_count += 1
                if state.damage_count == 1:
                    if state.player_shield > 0:
                        state.player_shield -= 20
                        state.shield -= 2
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
                state.damage_check = True
            state.player.move(state.chain.xSpeed,0)
        if state.chain.collision(state.boss_body) and state.chain_rebound:
            state.chain.xSpeed = 0
            state.chained.remove(state.chain)
            state.all_sprites3.remove(state.chain)
            state.chain_rebound = False
            state.chain_away = False
            state.chain_attack_count = -60
            state.chain_position1 = 0
            state.chain_count = 0
            state.damage_count = 0
            for i in state.o_chains:
                state.all_sprites3.remove(i)
                state.o_chains.remove(i)


def update_mace():
    """Thrown mace: fly out trailing chain links, wait at the wall, come back."""
    # `mace` stays on state: the original used this global name both in this loop and outside it.
    for state.mace in state.maces:
        state.mace.move(state.mace.xSpeed,0)
        if state.mace.getX() + state.mace.getWidth() < state.boss_body.getX() and state.boss_facing_left:
            state.chain_appearance += 1
            if state.chain_appearance == 3:
                state.chain = Sprite(20,20,None, "chain_texture_00.png")
                state.chain.setPosition(state.mace.getX() + state.mace.getWidth() + state.chain_position - state.chain_distance, state.mace.getY() + 10)
                state.chains.append(state.chain)
                state.all_sprites3.add(state.chain)
                state.chain_position += 15
                state.chain_appearance = 0
                state.chain_appeared = True
                if state.chain.getX() + state.chain.getWidth() > state.boss_body.getX():
                    state.chain_position -= 15
        if state.mace.getX() > state.boss_body.getX() + state.boss_body.getWidth() and state.boss_facing_right:
            state.chain_appearance += 1
            if state.chain_appearance == 3:
                state.chain = Sprite(20,20,None,"chain_texture_00.png")
                state.chain.setPosition(state.mace.getX() - state.chain_position - state.chain_distance, state.mace.getY() + 10)
                state.chains.append(state.chain)
                state.all_sprites3.add(state.chain)
                state.chain_position += 15
                state.chain_appearance = 0
                state.chain_appeared = True
                if state.chain.getX()  < state.boss_body.getX() + state.boss_body.getWidth():
                    state.chain_position -= 15
        if state.mace.collision(state.player):
            state.damage_count1 += 1
            if state.damage_count1 == 1:
                if state.player_shield > 0:
                    state.player_shield -= 20
                    state.shield -= 2
                else:
                    if state.health != 0:
                        state.player_health -= 10
                        state.health -= 1
                state.shield_count = 0
                state.damage_check = True
        if state.mace.collision(state.bound7) or state.mace.collision(state.bound8):
            state.mace.xSpeed = 0
            state.mace_stop += 1
            if state.mace_stop == 120:
                state.damage_count1 = 0
                state.mace.xSpeed = state.mace_speed * -1
                state.mace_rebound = True
                state.mace_reattack = False
        if state.mace.collision(state.boss_body) and state.mace_rebound:
            state.mace.xSpeed = 0
            state.maces.remove(state.mace)
            state.all_sprites3.remove(state.mace)
            state.mace_rebound = False
            state.mace_reattack = False
            state.mace_away = False
            if not state.not_mace:
                state.mace_attack_count = -60
            elif state.not_mace:
                state.mace_attack_count = 0
            state.mace_stop = 0
            state.damage_count1 = 0
            state.chain_position = 0
            state.chain_distance = 10
            for i in state.chains:
                state.all_sprites3.remove(i)
                state.chains.remove(i)


def update_trailing_chains():
    """Move the chain links that trail behind the mace and the chain grab."""
    # `chain` stays on state: the original used this global name both in this loop and outside it.
    for state.chain in state.chains:
        state.chain.move(state.mace.xSpeed,0)
        if state.chain.collision(state.boss_body) and state.chain_appeared:
            state.all_sprites3.remove(state.chain)
            state.chains.remove(state.chain)
    for o_chain in state.o_chains:
        o_chain.move(state.chain_speed,0)
        if o_chain.collision(state.boss_body) and state.chain_rebound:
            state.all_sprites3.remove(o_chain)
            state.o_chains.remove(o_chain)


def pick_up_trophy():
    """Swap the player for the trophy-holding sprite."""
    if state.boss_health == 0 and state.trophy_up and state.health != 0:
        if state.player.collision(state.trophy):
            state.player_win_count += 1
            if state.player_win_count == 1:
                state.all_sprites3.remove(state.player)
                state.all_sprites3.remove(state.trophy)
                state.player_win = Sprite(75,75,None,"player_trophy_00.png")
                state.player_win.setPosition(state.player.getX(),state.player.getY() - 25)
                state.all_sprites3.add(state.player_win)


def rebuild_draw_group():
    """Between attacks: clear projectiles, rebuild what gets drawn, handle winning and the death animation."""
    if not state.chain_away and not state.mace_away:
        # `chain` stays on state: the original used this global name both in this loop and outside it.
        for state.chain in state.chains:
            state.all_sprites3.remove(state.chains)
            state.chains.remove(state.chain)
        for o_chain in state.o_chains:
            state.all_sprites3.remove(state.chains)
            state.o_chains.remove(o_chain)
        # `mace` stays on state: the original used this global name both in this loop and outside it.
        for state.mace in state.maces:
            state.all_sprites3.remove(state.mace)
            state.maces.remove(state.mace)
        # `chain` stays on state: the original used this global name both in this loop and outside it.
        for state.chain in state.chained:
            state.all_sprites3.remove(state.chain)
            state.chained.remove(state.chain)
        for sprites in state.all_sprites3:
            state.all_sprites3.remove(sprites)
        state.all_sprites3.add(state.back3,state.ground1,state.boss,state.arrows)
        if state.health != 0 and state.boss_health != 0:
            state.all_sprites3.add(state.player)
        if state.health == 0 and state.boss_health != 0 and state.death_counter <= 75:
            state.all_sprites3.add(state.player)
        if state.boss_health == 0 and state.boss_death_animation > 105:
            state.all_sprites3.remove(state.boss)
            state.all_sprites3.add(state.trophy)
        if state.boss_health == 0 and not state.trophy_up and state.health != 0:
            state.all_sprites3.add(state.player)
        if state.boss_health == 0 and state.trophy_up and state.health != 0:
            if state.player.collision(state.trophy):
                state.winner = True
        if state.winner:
            state.winner_text += 1
            state.all_sprites3.remove(state.player)
            state.all_sprites3.remove(state.trophy)
            state.all_sprites3.add(state.back3,state.ground1,state.arrows,state.player_win)
        if state.health == 0:
            state.playerLeft = False
            state.playerRight = False
            state.playerUp = False
            state.playerDown = False
            state.playerUp = False
            state.jump = False
            state.attack = False
            state.death_counter += 1
            if state.death_counter == 1:
                state.player.setImageIndex(80)
            if state.death_counter == 15:
                state.player.setImageIndex(81)
            if state.death_counter == 30:
                state.player.setImageIndex(82)
            if state.death_counter == 45:
                state.player.setImageIndex(83)
            if state.death_counter == 60:
                state.player.setImageIndex(84)
            if state.death_counter == 75:
                state.all_sprites3.remove(state.player)


def handle_events():
    """Keyboard and mouse input for the boss room."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.boss_battle = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                state.playerRight = True
            if event.key == pygame.K_a:
                state.playerLeft = True
            if event.key == pygame.K_SPACE:
                state.jump = True
            if event.key == pygame.K_w:
                state.playerUp = True
            elif event.key == pygame.K_s:
                state.playerDown = True
            if event.key == pygame.K_t:
                state.trophy_up = True
            if event.key == pygame.K_1:
                state.weapon = 1
            if event.key == pygame.K_2:
                state.weapon = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                state.playerRight = False
            if event.key == pygame.K_a:
                state.playerLeft = False
            if event.key == pygame.K_SPACE:
                state.jump = False
            if event.key == pygame.K_w:
                state.playerUp = False
            elif event.key == pygame.K_s:
                state.playerDown = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            state.attack = True


def setup():
    """Build the level (runs once, before the loop)."""
    setup_boss_room()


def frame():
    """One frame of the level, in the exact order of the original loop body."""
    player.update_attack_ranges()
    update_boss_ranges()
    physics.set_boss_room_gravity()
    player.tick_regen_counters()
    draw()
    reset_frame_flags()
    player.update_stats_boss_room()
    player.reset_attack_counter()
    check_room_bounds()
    face_player()
    update_boss_death()
    update_boss_attacks()
    player_on_floor()
    physics.apply_gravity()
    move_player()
    player.update_idle_pose()
    drop_trophy()
    player.cancel_attack_in_air()
    update_player_arrows()
    update_chain_grab()
    update_mace()
    update_trailing_chains()
    player.update_damage_flash_boss_room()
    pick_up_trophy()
    rebuild_draw_group()
    player.reset_attack_counter()
    pygame.display.flip()
    handle_events()


def run():
    """Run the level until its flag turns off (door entered, boss beaten, or window closed)."""
    loop.run(state.boss_clock, 70, lambda: state.boss_battle, frame)

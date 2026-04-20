"""The 8 parkour-level enemies: sprites, animation helpers, AI and their arrows.
"""
from game.sprite import Sprite
from game.colors import GREEN, RED, BLUE
from game.state import state


def enemy_death_left(count,name,group):
    """Enemy death animation while facing left; `count` is the frame counter."""
    if count == 1:
        name.setImageIndex(4)
    if count == 15:
        name.setImageIndex(5)
    if count == 30:
        name.setImageIndex(6)
    if count == 45:
        name.setImageIndex(7)
    if count == 60:
        count = 0
        group.remove(name)


def enemy_death_right(count,name,group):
    """Enemy death animation while facing right; `count` is the frame counter."""
    if count == 1:
        name.setImageIndex(16)
    if count == 15:
        name.setImageIndex(17)
    if count == 30:
        name.setImageIndex(18)
    if count == 45:
        name.setImageIndex(19)
    if count == 60:
        count = 0
        group.remove(name)


def enemy_shoot_left(count,name,arrow_group,group):
    """Enemy bow animation facing left; fires an arrow on frame 30."""
    if count == 1:
        name.setImageIndex(1)
    if count == 15:
        name.setImageIndex(2)
    if count == 30:
        name.setImageIndex(3)
        e_arrow = Sprite(30,12,None,"arrow_left_00.png")
        e_arrow.xSpeed = -state.groundSpeed - 2
        e_arrow.setPosition(name.getX() - 30, name.getY() + (name.getWidth() / 2) - 5)
        arrow_group.append(e_arrow)
        group.add(arrow_group)
    if count == 45:
        name.setImageIndex(24)
    if count == 85:
        count = 0


def enemy_shoot_right(count,name,arrow_group,group):
    """Enemy bow animation facing right; fires an arrow on frame 30."""
    if count == 1:
        name.setImageIndex(13)
    if count == 15:
        name.setImageIndex(14)
    if count == 30:
        name.setImageIndex(15)
        e_arrow = Sprite(30,12,None,"arrow_right_00.png")
        e_arrow.xSpeed = state.groundSpeed + 2
        e_arrow.setPosition(name.getX() + name.getWidth(), name.getY() + (name.getWidth() / 2) - 5)
        arrow_group.append(e_arrow)
        group.add(arrow_group)
    if count == 45:
        name.setImageIndex(27)
    if count == 85:
        count = 0


def enemy_attack_right(count,name):
    """Enemy sword animation (player on its left side); `count` is the frame counter."""
    if count == 1:
        name.setImageIndex(8)
    if count == 10:
        name.setImageIndex(9)
    if count == 20:
        name.setImageIndex(10)
    if count == 30:
        name.setImageIndex(11)
    if count == 40:
        name.setImageIndex(24)
    if count == 90:
        count = 0


def enemy_attack_left(count,name):
    """Enemy sword animation (player on its right side); `count` is the frame counter."""
    if count == 1:
        name.setImageIndex(20)
    if count == 10:
        name.setImageIndex(21)
    if count == 20:
        name.setImageIndex(22)
    if count == 30:
        name.setImageIndex(23)
    if count == 40:
        name.setImageIndex(27)
    if count == 90:
        count = 0


def create_enemies():
    """Create the 8 enemies and load their animation frames."""
    state.enemy1 = Sprite(50,50,None,"enemy_walking_left_00.png")
    state.enemy2 = Sprite(50,50,None,"enemy_walking_left_00.png")
    state.enemy3 = Sprite(50,50,None,"enemy_walking_left_00.png")
    state.enemy4 = Sprite(50,50,None,"enemy_walking_left_00.png")
    state.enemy5 = Sprite(50,50,None,"enemy_walking_left_00.png")
    state.enemy6 = Sprite(50,50,None,"enemy_walking_left_00.png")
    state.enemy7 = Sprite(50,50,None,"enemy_walking_left_00.png")
    state.enemy8 = Sprite(50,50,None,"enemy_walking_left_00.png")
    state.enemy1.setPosition(4000,410)
    state.enemy2.setPosition(4200,410)
    state.enemy3.setPosition(2000,410)
    state.enemy4.setPosition(5700,410)
    state.enemy5.setPosition(5900,410)
    state.enemy6.setPosition(7400,410)
    state.enemy7.setPosition(7600,410)
    state.enemy8.setPosition(7800,410)
    state.enemy.append(state.enemy1)
    state.enemy.append(state.enemy2)
    state.enemy.append(state.enemy3)
    state.enemy.append(state.enemy4)
    state.enemy.append(state.enemy5)
    state.enemy.append(state.enemy6)
    state.enemy.append(state.enemy7)
    state.enemy.append(state.enemy8)
    for enemies in state.enemy:
        enemies.addImage("enemy_left_arrow_01.png")
        enemies.addImage("enemy_left_arrow_02.png")
        enemies.addImage("enemy_left_arrow_03.png")
        enemies.addImage("enemy_left_dying_00.png")
        enemies.addImage("enemy_left_dying_01.png")
        enemies.addImage("enemy_left_dying_02.png")
        enemies.addImage("enemy_left_dying_03.png")
        enemies.addImage("enemy_left_sword_00.png")
        enemies.addImage("enemy_left_sword_01.png")
        enemies.addImage("enemy_left_sword_02.png")
        enemies.addImage("enemy_left_sword_03.png")
        enemies.addImage("enemy_right_arrow_00.png")
        enemies.addImage("enemy_right_arrow_01.png")
        enemies.addImage("enemy_right_arrow_02.png")
        enemies.addImage("enemy_right_arrow_03.png")
        enemies.addImage("enemy_right_dying_00.png")
        enemies.addImage("enemy_right_dying_01.png")
        enemies.addImage("enemy_right_dying_02.png")
        enemies.addImage("enemy_right_dying_03.png")
        enemies.addImage("enemy_right_sword_00.png")
        enemies.addImage("enemy_right_sword_01.png")
        enemies.addImage("enemy_right_sword_02.png")
        enemies.addImage("enemy_right_sword_03.png")
        enemies.addImage("enemy_walking_left_00.png")
        enemies.addImage("enemy_walking_left_01.png")
        enemies.addImage("enemy_walking_left_02.png")
        enemies.addImage("enemy_walking_right_00.png")
        enemies.addImage("enemy_walking_right_01.png")
        enemies.addImage("enemy_walking_right_02.png")


def create_ranges():
    """Create each enemy's detection boxes (sword reach, chase zone, bow zone)."""
    state.enemy1_range1 = Sprite(50,50,RED)
    state.enemy1_range2 = Sprite(50,50,RED)
    state.enemy1_range3 = Sprite(100,200,BLUE)
    state.enemy1_range4 = Sprite(100,200,BLUE)
    state.enemy1_range5 = Sprite(950,550,GREEN)
    state.enemy2_range1 = Sprite(50,50,RED)
    state.enemy2_range2 = Sprite(50,50,RED)
    state.enemy2_range3 = Sprite(100,200,BLUE)
    state.enemy2_range4 = Sprite(100,200,BLUE)
    state.enemy2_range5 = Sprite(950,550,GREEN)
    state.enemy3_range1 = Sprite(50,50,RED)
    state.enemy3_range2 = Sprite(50,50,RED)
    state.enemy3_range3 = Sprite(100,200,BLUE)
    state.enemy3_range4 = Sprite(100,200,BLUE)
    state.enemy3_range5 = Sprite(950,550,GREEN)
    state.enemy4_range1 = Sprite(50,50,RED)
    state.enemy4_range2 = Sprite(50,50,RED)
    state.enemy4_range3 = Sprite(100,200,BLUE)
    state.enemy4_range4 = Sprite(100,200,BLUE)
    state.enemy4_range5 = Sprite(950,550,GREEN)
    state.enemy5_range1 = Sprite(50,50,RED)
    state.enemy5_range2 = Sprite(50,50,RED)
    state.enemy5_range3 = Sprite(100,200,BLUE)
    state.enemy5_range4 = Sprite(100,200,BLUE)
    state.enemy5_range5 = Sprite(950,550,GREEN)
    state.enemy6_range1 = Sprite(50,50,RED)
    state.enemy6_range2 = Sprite(50,50,RED)
    state.enemy6_range3 = Sprite(100,200,BLUE)
    state.enemy6_range4 = Sprite(100,200,BLUE)
    state.enemy6_range5 = Sprite(950,550,GREEN)
    state.enemy7_range1 = Sprite(50,50,RED)
    state.enemy7_range2 = Sprite(50,50,RED)
    state.enemy7_range3 = Sprite(100,200,BLUE)
    state.enemy7_range4 = Sprite(100,200,BLUE)
    state.enemy7_range5 = Sprite(950,550,GREEN)
    state.enemy8_range1 = Sprite(50,50,RED)
    state.enemy8_range2 = Sprite(50,50,RED)
    state.enemy8_range3 = Sprite(100,200,BLUE)
    state.enemy8_range4 = Sprite(100,200,BLUE)
    state.enemy8_range5 = Sprite(950,550,GREEN)


def face_dead_player():
    """Once the player is dead, every enemy turns to face them."""
    for enemies in state.enemy:
        if state.health == 0:
            if state.player.getX() < enemies.getX():
                enemies.setImageIndex(0)
            if state.player.getX() > enemies.getX():
                enemies.setImageIndex(27)


def update_enemy1():
    """Enemy 1 AI: block on terrain, shoot from far, chase when near, sword when adjacent, die at 0 health."""
    for i in state.ground:
        if (i.getX() <= state.enemy1.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= state.enemy1.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= state.enemy1.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= state.enemy1.getY() + state.player.getHeight() <= i.getY() + 10:
            state.enemy_attack = True
    for walls in state.wall:
        if state.enemy1.collision(walls):
            if (walls.getY() <= state.enemy1.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy1.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy1.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= state.enemy1.getX() + state.enemy1.getWidth() <= walls.getX() + 10:
                state.enemy1_stop_left = True
            if (walls.getY() <= state.enemy1.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy1.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy1.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= state.enemy1.getX() <= walls.getX() + walls.getWidth() + 2:
                state.enemy1_stop_right = True
    for c_walls in state.c_wall:
        if state.enemy1.collision(c_walls):
            if (c_walls.getY() <= state.enemy1.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy1.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy1.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= state.enemy1.getX() + state.enemy1.getWidth() <= c_walls.getX() + 10:
                state.enemy1_stop_left = True
            if (c_walls.getY() <= state.enemy1.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy1.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy1.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= state.enemy1.getX() <= c_walls.getX() + c_walls.getWidth() + 2:
                state.enemy1_stop_right = True
    for spikes in state.spike:
        if state.enemy1.collision(spikes):
            if (spikes.getY() <= state.enemy1.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy1.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy1.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= state.enemy1.getX() + state.enemy1.getWidth() <= spikes.getX() + 10:
                state.enemy1_stop_left = True
            if (spikes.getY() <= state.enemy1.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy1.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy1.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= state.enemy1.getX() <= spikes.getX() + spikes.getWidth() + 2:
                state.enemy1_stop_right = True
    state.enemy1_range1.setPosition(state.enemy1.getX() - 50, state.enemy1.getY())
    state.enemy1_range2.setPosition(state.enemy1.getX() + state.enemy1.getWidth(), state.enemy1.getY())
    state.enemy1_range3.setPosition(state.enemy1.getX() - 160,state.enemy1.getY() - state.enemy1.getWidth() - 30)
    state.enemy1_range4.setPosition(state.enemy1.getX() + 110, state.enemy1.getY() - state.enemy1.getWidth() - 30)
    state.enemy1_range5.setPosition(state.enemy1.getX() - 425, state.enemy1.getY() - 410)
    if state.enemy1_health > 0:
        if state.enemy1.getY() <= state.player.getY() + 25 <= state.enemy1.getY() + state.enemy1.getHeight() and state.enemy1.getX() + state.enemy1.getWidth() - 10 <= state.player.getX() <= state.enemy1.getX() + state.enemy1.getWidth() + 2:
            state.playerLeft = False
        elif state.enemy1.getY() <= state.player.getY() + 25 <= state.enemy1.getY() + state.enemy1.getHeight() and state.enemy1.getX() - 2 <= state.player.getX() + state.player.getWidth() <= state.enemy1.getX() + 10:
            state.playerRight = False
    if state.enemy1_health <= 0:
        state.enemy1_health = 0
    if state.enemy1_health == 0:
        state.enemy1_death_ani += 1
        if state.enemy_facing_left:
            enemy_death_left(state.enemy1_death_ani,state.enemy1,state.all_sprites1)
        elif state.enemy_facing_right:
            enemy_death_right(state.enemy1_death_ani,state.enemy1,state.all_sprites1)
    if state.enemy1_health > 0 and state.health != 0:
        if state.enemy_attack:
            state.enemy1_count += 1
            if not state.player.collision(state.enemy1_range3) and not state.player.collision(state.enemy1_range4) and not state.player.collision(state.enemy1_range1) and not state.player.collision(state.enemy1_range2):
                if state.player.getX() < state.enemy1.getX():
                    state.enemy_facing_left = True
                    state.enemy_facing_right = False
                    enemy_shoot_left(state.enemy1_count,state.enemy1,state.enemy_arrows,state.all_sprites1)
                if state.player.getX() > state.enemy1.getX():
                    state.enemy_facing_left = False
                    state.enemy_facing_right = True
                    enemy_shoot_right(state.enemy1_count,state.enemy1,state.enemy_arrows,state.all_sprites1)
            elif state.player.collision(state.enemy1_range3) or state.player.collision(state.enemy1_range4):
                if state.player.collision(state.enemy1_range3):
                    state.enemy_facing_left = True
                    state.enemy_facing_right = False
                    if not state.enemy1_stop_right:
                        state.enemy1.move(-3,0)
                    state.enemy1.imageStartEnd(24,26,10)
                if state.player.collision(state.enemy1_range4):
                    state.enemy_facing_left = False
                    state.enemy_facing_right = True
                    if not state.enemy1_stop_left:
                        state.enemy1.move(3,0)
                    state.enemy1.imageStartEnd(27,29,10)
                state.enemy1_count = 0
            elif state.player.collision(state.enemy1_range1):
                enemy_attack_right(state.enemy1_count,state.enemy1)
                if state.enemy1_count == 30:
                    state.damage_check = True
                    if state.player_shield > 0:
                        state.player_shield -= 20
                        state.shield -= 2
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
            elif state.player.collision(state.enemy1_range2):
                enemy_attack_left(state.enemy1_count,state.enemy1)
                if state.enemy1_count == 30:
                    state.damage_check = True
                    if state.player_shield > 0:
                        state.player_shield -= 20
                        state.shield -= 2
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
            if state.enemy1_count == 90:
                state.enemy1_count = 0


def update_enemy2():
    """Enemy 2 AI: block on terrain, shoot from far, chase when near, sword when adjacent, die at 0 health."""
    for i in state.ground:
        if (i.getX() <= state.enemy2.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= state.enemy2.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= state.enemy2.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= state.enemy2.getY() + state.player.getHeight() <= i.getY() + 10:
            state.enemy_attack = True
    for walls in state.wall:
        if state.enemy2.collision(walls):
            if (walls.getY() <= state.enemy2.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy2.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy2.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= state.enemy2.getX() + state.enemy2.getWidth() <= walls.getX() + 10:
                state.enemy2_stop_left = True
            if (walls.getY() <= state.enemy2.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy2.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy2.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= state.enemy2.getX() <= walls.getX() + walls.getWidth() + 2:
                state.enemy2_stop_right = True
    for c_walls in state.c_wall:
        if state.enemy2.collision(c_walls):
            if (c_walls.getY() <= state.enemy2.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy2.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy2.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= state.enemy2.getX() + state.enemy2.getWidth() <= c_walls.getX() + 10:
                state.enemy2_stop_left = True
            if (c_walls.getY() <= state.enemy2.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy2.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy2.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= state.enemy2.getX() <= c_walls.getX() + c_walls.getWidth() + 2:
                state.enemy2_stop_right = True
    for spikes in state.spike:
        if state.enemy2.collision(spikes):
            if (spikes.getY() <= state.enemy2.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy2.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy2.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= state.enemy2.getX() + state.enemy2.getWidth() <= spikes.getX() + 10:
                state.enemy2_stop_left = True
            if (spikes.getY() <= state.enemy2.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy2.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy2.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= state.enemy2.getX() <= spikes.getX() + spikes.getWidth() + 2:
                state.enemy2_stop_right = True
    state.enemy2_range1.setPosition(state.enemy2.getX() - 50, state.enemy2.getY())
    state.enemy2_range2.setPosition(state.enemy2.getX() + state.enemy2.getWidth(), state.enemy2.getY())
    state.enemy2_range3.setPosition(state.enemy2.getX() - 160,state.enemy2.getY() - state.enemy2.getWidth() - 30)
    state.enemy2_range4.setPosition(state.enemy2.getX() + 110, state.enemy2.getY() - state.enemy2.getWidth() - 30)
    state.enemy2_range5.setPosition(state.enemy2.getX() - 425, state.enemy2.getY() - 410)
    if state.enemy2_health > 0:
        if state.enemy2.getY() <= state.player.getY() + 25 <= state.enemy2.getY() + state.enemy2.getHeight() and state.enemy2.getX() + state.enemy2.getWidth() - 10 <= state.player.getX() <= state.enemy2.getX() + state.enemy2.getWidth() + 2:
            state.playerLeft = False
        elif state.enemy2.getY() <= state.player.getY() + 25 <= state.enemy2.getY() + state.enemy2.getHeight() and state.enemy2.getX() - 2 <= state.player.getX() + state.player.getWidth() <= state.enemy2.getX() + 10:
            state.playerRight = False
    if state.enemy2_health <= 0:
        state.enemy2_health = 0
    if state.enemy2_health == 0:
        state.enemy2_death_ani += 1
        if state.enemy_facing_left:
            enemy_death_left(state.enemy2_death_ani,state.enemy2,state.all_sprites1)
        elif state.enemy_facing_right:
            enemy_death_right(state.enemy2_death_ani,state.enemy2,state.all_sprites1)
    if state.enemy2_health > 0 and state.health != 0:
        if state.enemy_attack:
            state.enemy2_count += 1
            if not state.player.collision(state.enemy2_range3) and not state.player.collision(state.enemy2_range4) and not state.player.collision(state.enemy2_range1) and not state.player.collision(state.enemy2_range2):
                if state.player.getX() < state.enemy2.getX():
                    state.enemy_facing_left = True
                    state.enemy_facing_right = False
                    enemy_shoot_left(state.enemy2_count,state.enemy2,state.enemy_arrows,state.all_sprites1)
                if state.player.getX() > state.enemy2.getX():
                    state.enemy_facing_left = False
                    state.enemy_facing_right = True
                    enemy_shoot_right(state.enemy2_count,state.enemy2,state.enemy_arrows,state.all_sprites1)
            elif state.player.collision(state.enemy2_range3) or state.player.collision(state.enemy2_range4):
                if state.player.collision(state.enemy2_range3):
                    state.enemy_facing_left = True
                    state.enemy_facing_right = False
                    if not state.enemy2_stop_right:
                        state.enemy2.move(-3,0)
                    state.enemy2.imageStartEnd(24,26,10)
                if state.player.collision(state.enemy2_range4):
                    state.enemy_facing_left = False
                    state.enemy_facing_right = True
                    if not state.enemy2_stop_left:
                        state.enemy2.move(3,0)
                    state.enemy2.imageStartEnd(27,29,10)
                state.enemy2_count = 0
            elif state.player.collision(state.enemy2_range1):
                enemy_attack_right(state.enemy2_count,state.enemy2)
                if state.enemy2_count == 30:
                    state.damage_check = True
                    if state.player_shield > 0:
                        state.player_shield -= 20
                        state.shield -= 2
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
            elif state.player.collision(state.enemy2_range2):
                enemy_attack_left(state.enemy2_count,state.enemy2)
                if state.enemy2_count == 30:
                    state.damage_check = True
                    if state.player_shield > 0:
                        state.player_shield -= 20
                        state.shield -= 2
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
            if state.enemy2_count == 90:
                state.enemy2_count = 0


def update_enemy3():
    """Enemy 3 AI: block on terrain, shoot from far, chase when near, sword when adjacent, die at 0 health."""
    for i in state.ground:
        if (i.getX() <= state.enemy3.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= state.enemy3.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= state.enemy3.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= state.enemy3.getY() + state.player.getHeight() <= i.getY() + 10:
            state.enemy_attack = True
    for walls in state.wall:
        if state.enemy3.collision(walls):
            if (walls.getY() <= state.enemy3.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy3.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy3.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= state.enemy3.getX() + state.enemy3.getWidth() <= walls.getX() + 10:
                state.enemy3_stop_left = True
            if (walls.getY() <= state.enemy3.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy3.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy3.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= state.enemy3.getX() <= walls.getX() + walls.getWidth() + 2:
                state.enemy3_stop_right = True
    for c_walls in state.c_wall:
        if state.enemy3.collision(c_walls):
            if (c_walls.getY() <= state.enemy3.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy3.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy3.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= state.enemy3.getX() + state.enemy3.getWidth() <= c_walls.getX() + 10:
                state.enemy3_stop_left = True
            if (c_walls.getY() <= state.enemy3.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy3.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy3.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= state.enemy3.getX() <= c_walls.getX() + c_walls.getWidth() + 2:
                state.enemy3_stop_right = True
    for spikes in state.spike:
        if state.enemy3.collision(spikes):
            if (spikes.getY() <= state.enemy3.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy3.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy3.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= state.enemy3.getX() + state.enemy3.getWidth() <= spikes.getX() + 10:
                state.enemy3_stop_left = True
            if (spikes.getY() <= state.enemy3.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy3.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy3.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= state.enemy3.getX() <= spikes.getX() + spikes.getWidth() + 2:
                state.enemy3_stop_right = True
    state.enemy3_range1.setPosition(state.enemy3.getX() - 50, state.enemy3.getY())
    state.enemy3_range2.setPosition(state.enemy3.getX() + state.enemy3.getWidth(), state.enemy3.getY())
    state.enemy3_range3.setPosition(state.enemy3.getX() - 160,state.enemy3.getY() - state.enemy3.getWidth() - 30)
    state.enemy3_range4.setPosition(state.enemy3.getX() + 110, state.enemy3.getY() - state.enemy3.getWidth() - 30)
    state.enemy3_range5.setPosition(state.enemy3.getX() - 425, state.enemy3.getY() - 410)
    if state.enemy3_health > 0:
        if state.enemy3.getY() <= state.player.getY() + 25 <= state.enemy3.getY() + state.enemy3.getHeight() and state.enemy3.getX() + state.enemy3.getWidth() - 10 <= state.player.getX() <= state.enemy3.getX() + state.enemy3.getWidth() + 2:
            state.playerLeft = False
        elif state.enemy3.getY() <= state.player.getY() + 25 <= state.enemy3.getY() + state.enemy3.getHeight() and state.enemy3.getX() - 2 <= state.player.getX() + state.player.getWidth() <= state.enemy3.getX() + 10:
            state.playerRight = False
    if state.enemy3_health <= 0:
        state.enemy3_health = 0
    if state.enemy3_health == 0:
        state.enemy3_death_ani += 1
        if state.enemy_facing_left:
            enemy_death_left(state.enemy3_death_ani,state.enemy3,state.all_sprites1)
        elif state.enemy_facing_right:
            enemy_death_right(state.enemy3_death_ani,state.enemy3,state.all_sprites1)
    if state.enemy3_health > 0 and state.health != 0:
        if state.enemy_attack:
            state.enemy3_count += 1
            if not state.player.collision(state.enemy3_range3) and not state.player.collision(state.enemy3_range4) and not state.player.collision(state.enemy3_range1) and not state.player.collision(state.enemy3_range2):
                if state.player.getX() < state.enemy3.getX():
                    state.enemy_facing_left = True
                    state.enemy_facing_right = False
                    enemy_shoot_left(state.enemy3_count,state.enemy3,state.enemy_arrows,state.all_sprites1)
                if state.player.getX() > state.enemy3.getX():
                    state.enemy_facing_left = False
                    state.enemy_facing_right = True
                    enemy_shoot_right(state.enemy3_count,state.enemy3,state.enemy_arrows,state.all_sprites1)
            elif state.player.collision(state.enemy3_range3) or state.player.collision(state.enemy3_range4):
                if state.player.collision(state.enemy3_range3):
                    state.enemy_facing_left = True
                    state.enemy_facing_right = False
                    if not state.enemy3_stop_right:
                        state.enemy3.move(-3,0)
                    state.enemy3.imageStartEnd(24,26,10)
                if state.player.collision(state.enemy3_range4):
                    state.enemy_facing_left = False
                    state.enemy_facing_right = True
                    if not state.enemy3_stop_left:
                        state.enemy3.move(3,0)
                    state.enemy3.imageStartEnd(27,29,10)
                state.enemy3_count = 0
            elif state.player.collision(state.enemy3_range1):
                enemy_attack_right(state.enemy3_count,state.enemy3)
                if state.enemy3_count == 30:
                    state.damage_check = True
                    if state.player_shield > 0:
                        state.player_shield -= 20
                        state.shield -= 2
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
            elif state.player.collision(state.enemy3_range2):
                enemy_attack_left(state.enemy3_count,state.enemy3)
                if state.enemy3_count == 30:
                    state.damage_check = True
                    if state.player_shield > 0:
                        state.player_shield -= 20
                        state.shield -= 2
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
            if state.enemy3_count == 90:
                state.enemy3_count = 0


def update_enemy4():
    """Enemy 4 AI: block on terrain, shoot from far, chase when near, sword when adjacent, die at 0 health."""
    for i in state.ground:
        if (i.getX() <= state.enemy4.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= state.enemy4.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= state.enemy4.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= state.enemy4.getY() + state.player.getHeight() <= i.getY() + 10:
            state.enemy_attack = True
    for walls in state.wall:
        if state.enemy4.collision(walls):
            if (walls.getY() <= state.enemy4.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy4.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy4.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= state.enemy4.getX() + state.enemy4.getWidth() <= walls.getX() + 10:
                state.enemy4_stop_left = True
            if (walls.getY() <= state.enemy4.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy4.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy4.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= state.enemy4.getX() <= walls.getX() + walls.getWidth() + 2:
                state.enemy4_stop_right = True
    for c_walls in state.c_wall:
        if state.enemy4.collision(c_walls):
            if (c_walls.getY() <= state.enemy4.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy4.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy4.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= state.enemy4.getX() + state.enemy4.getWidth() <= c_walls.getX() + 10:
                state.enemy4_stop_left = True
            if (c_walls.getY() <= state.enemy4.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy4.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy4.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= state.enemy4.getX() <= c_walls.getX() + c_walls.getWidth() + 2:
                state.enemy4_stop_right = True
    for spikes in state.spike:
        if state.enemy4.collision(spikes):
            if (spikes.getY() <= state.enemy4.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy4.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy4.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= state.enemy4.getX() + state.enemy4.getWidth() <= spikes.getX() + 10:
                state.enemy4_stop_left = True
            if (spikes.getY() <= state.enemy4.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy4.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy4.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= state.enemy4.getX() <= spikes.getX() + spikes.getWidth() + 2:
                state.enemy4_stop_right = True
    state.enemy4_range1.setPosition(state.enemy4.getX() - 50, state.enemy4.getY())
    state.enemy4_range2.setPosition(state.enemy4.getX() + state.enemy4.getWidth(), state.enemy4.getY())
    state.enemy4_range3.setPosition(state.enemy4.getX() - 160,state.enemy4.getY() - state.enemy4.getWidth() - 30)
    state.enemy4_range4.setPosition(state.enemy4.getX() + 110, state.enemy4.getY() - state.enemy4.getWidth() - 30)
    state.enemy4_range5.setPosition(state.enemy4.getX() - 425, state.enemy4.getY() - 410)
    if state.enemy4_health > 0:
        if state.enemy4.getY() <= state.player.getY() + 25 <= state.enemy4.getY() + state.enemy4.getHeight() and state.enemy4.getX() + state.enemy4.getWidth() - 10 <= state.player.getX() <= state.enemy4.getX() + state.enemy4.getWidth() + 2:
            state.playerLeft = False
        elif state.enemy4.getY() <= state.player.getY() + 25 <= state.enemy4.getY() + state.enemy4.getHeight() and state.enemy4.getX() - 2 <= state.player.getX() + state.player.getWidth() <= state.enemy4.getX() + 10:
            state.playerRight = False
    if state.enemy4_health <= 0:
        state.enemy4_health = 0
    if state.enemy4_health == 0:
        state.enemy4_death_ani += 1
        if state.enemy_facing_left:
            enemy_death_left(state.enemy4_death_ani,state.enemy4,state.all_sprites1)
        elif state.enemy_facing_right:
            enemy_death_right(state.enemy4_death_ani,state.enemy4,state.all_sprites1)
    if state.enemy4_health > 0 and state.health != 0:
        if state.enemy_attack:
            state.enemy4_count += 1
            if not state.player.collision(state.enemy4_range3) and not state.player.collision(state.enemy4_range4) and not state.player.collision(state.enemy4_range1) and not state.player.collision(state.enemy4_range2):
                if state.player.getX() < state.enemy4.getX():
                    state.enemy_facing_left = True
                    state.enemy_facing_right = False
                    enemy_shoot_left(state.enemy4_count,state.enemy4,state.enemy_arrows,state.all_sprites1)
                if state.player.getX() > state.enemy4.getX():
                    state.enemy_facing_left = False
                    state.enemy_facing_right = True
                    enemy_shoot_right(state.enemy4_count,state.enemy4,state.enemy_arrows,state.all_sprites1)
            elif state.player.collision(state.enemy4_range3) or state.player.collision(state.enemy4_range4):
                if state.player.collision(state.enemy4_range3):
                    state.enemy_facing_left = True
                    state.enemy_facing_right = False
                    if not state.enemy4_stop_right:
                        state.enemy4.move(-3,0)
                    state.enemy4.imageStartEnd(24,26,10)
                if state.player.collision(state.enemy4_range4):
                    state.enemy_facing_left = False
                    state.enemy_facing_right = True
                    if not state.enemy4_stop_left:
                        state.enemy4.move(3,0)
                    state.enemy4.imageStartEnd(27,29,10)
                state.enemy4_count = 0
            elif state.player.collision(state.enemy4_range1):
                enemy_attack_right(state.enemy4_count,state.enemy4)
                if state.enemy4_count == 30:
                    state.damage_check = True
                    if state.player_shield > 0:
                        state.player_shield -= 20
                        state.shield -= 2
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
            elif state.player.collision(state.enemy4_range2):
                enemy_attack_left(state.enemy4_count,state.enemy4)
                if state.enemy4_count == 30:
                    state.damage_check = True
                    if state.player_shield > 0:
                        state.player_shield -= 20
                        state.shield -= 2
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
            if state.enemy4_count == 90:
                state.enemy4_count = 0


def update_enemy5():
    """Enemy 5 AI: block on terrain, shoot from far, chase when near, sword when adjacent, die at 0 health."""
    for i in state.ground:
        if (i.getX() <= state.enemy5.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= state.enemy5.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= state.enemy5.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= state.enemy5.getY() + state.player.getHeight() <= i.getY() + 10:
            state.enemy_attack = True
    for walls in state.wall:
        if state.enemy5.collision(walls):
            if (walls.getY() <= state.enemy5.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy5.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy5.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= state.enemy5.getX() + state.enemy5.getWidth() <= walls.getX() + 10:
                state.enemy5_stop_left = True
            if (walls.getY() <= state.enemy5.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy5.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= state.enemy5.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= state.enemy5.getX() <= walls.getX() + walls.getWidth() + 2:
                state.enemy5_stop_right = True
    for c_walls in state.c_wall:
        if state.enemy5.collision(c_walls):
            if (c_walls.getY() <= state.enemy5.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy5.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy5.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= state.enemy5.getX() + state.enemy5.getWidth() <= c_walls.getX() + 10:
                state.enemy5_stop_left = True
            if (c_walls.getY() <= state.enemy5.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy5.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= state.enemy5.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= state.enemy5.getX() <= c_walls.getX() + c_walls.getWidth() + 2:
                state.enemy5_stop_right = True
    for spikes in state.spike:
        if state.enemy5.collision(spikes):
            if (spikes.getY() <= state.enemy5.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy5.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy5.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= state.enemy5.getX() + state.enemy5.getWidth() <= spikes.getX() + 10:
                state.enemy5_stop_left = True
            if (spikes.getY() <= state.enemy5.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy5.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= state.enemy5.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= state.enemy5.getX() <= spikes.getX() + spikes.getWidth() + 2:
                state.enemy5_stop_right = True
    state.enemy5_range1.setPosition(state.enemy5.getX() - 50, state.enemy5.getY())
    state.enemy5_range2.setPosition(state.enemy5.getX() + state.enemy5.getWidth(), state.enemy5.getY())
    state.enemy5_range3.setPosition(state.enemy5.getX() - 160,state.enemy5.getY() - state.enemy5.getWidth() - 30)
    state.enemy5_range4.setPosition(state.enemy5.getX() + 110, state.enemy5.getY() - state.enemy5.getWidth() - 30)
    state.enemy5_range5.setPosition(state.enemy5.getX() - 425, state.enemy5.getY() - 410)
    if state.enemy5_health > 0:
        if state.enemy5.getY() <= state.player.getY() + 25 <= state.enemy5.getY() + state.enemy5.getHeight() and state.enemy5.getX() + state.enemy5.getWidth() - 10 <= state.player.getX() <= state.enemy5.getX() + state.enemy5.getWidth() + 2:
            state.playerLeft = False
        elif state.enemy5.getY() <= state.player.getY() + 25 <= state.enemy5.getY() + state.enemy5.getHeight() and state.enemy5.getX() - 2 <= state.player.getX() + state.player.getWidth() <= state.enemy5.getX() + 10:
            state.playerRight = False
    if state.enemy5_health <= 0:
        state.enemy5_health = 0
    if state.enemy5_health == 0:
        state.enemy5_death_ani += 1
        if state.enemy_facing_left:
            enemy_death_left(state.enemy5_death_ani,state.enemy5,state.all_sprites1)
        elif state.enemy_facing_right:
            enemy_death_right(state.enemy5_death_ani,state.enemy5,state.all_sprites1)
    if state.enemy5_health > 0 and state.health != 0:
        if state.enemy_attack:
            state.enemy5_count += 1
            if not state.player.collision(state.enemy5_range3) and not state.player.collision(state.enemy5_range4) and not state.player.collision(state.enemy5_range1) and not state.player.collision(state.enemy5_range2):
                if state.player.getX() < state.enemy5.getX():
                    state.enemy_facing_left = True
                    state.enemy_facing_right = False
                    enemy_shoot_left(state.enemy5_count,state.enemy5,state.enemy_arrows,state.all_sprites1)
                if state.player.getX() > state.enemy5.getX():
                    state.enemy_facing_left = False
                    state.enemy_facing_right = True
                    enemy_shoot_right(state.enemy5_count,state.enemy5,state.enemy_arrows,state.all_sprites1)
            elif state.player.collision(state.enemy5_range3) or state.player.collision(state.enemy5_range4):
                if state.player.collision(state.enemy5_range3):
                    state.enemy_facing_left = True
                    state.enemy_facing_right = False
                    if not state.enemy5_stop_right:
                        state.enemy5.move(-3,0)
                    state.enemy5.imageStartEnd(24,26,10)
                if state.player.collision(state.enemy5_range4):
                    state.enemy_facing_left = False
                    state.enemy_facing_right = True
                    if not state.enemy5_stop_left:
                        state.enemy5.move(3,0)
                    state.enemy5.imageStartEnd(27,29,10)
                state.enemy5_count = 0
            elif state.player.collision(state.enemy5_range1):
                enemy_attack_right(state.enemy5_count,state.enemy5)
                if state.enemy5_count == 30:
                    state.damage_check = True
                    if state.player_shield > 0:
                        state.player_shield -= 20
                        state.shield -= 2
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
            elif state.player.collision(state.enemy5_range2):
                enemy_attack_left(state.enemy5_count,state.enemy5)
                if state.enemy5_count == 30:
                    state.damage_check = True
                    if state.player_shield > 0:
                        state.player_shield -= 20
                        state.shield -= 2
                    else:
                        if state.health != 0:
                            state.player_health -= 10
                            state.health -= 1
                    state.shield_count = 0
            if state.enemy5_count == 90:
                state.enemy5_count = 0


def update_enemy_arrows():
    """Move enemy arrows; remove them on terrain, damage the player they hit."""
    for e_arrows in state.enemy_arrows:
        e_arrows.move(e_arrows.xSpeed,0)
        for grounds in state.ground:
            if e_arrows.collision(grounds):
                state.all_sprites1.remove(e_arrows)
                state.enemy_arrows.remove(e_arrows)
                e_arrows.move(0,0)
                e_arrows.setPosition(0,0)
        for walls in state.wall:
            if e_arrows.collision(walls):
                state.all_sprites1.remove(e_arrows)
                state.enemy_arrows.remove(e_arrows)
                e_arrows.move(0,0)
                e_arrows.setPosition(0,0)
        for c_walls in state.c_wall:
            if e_arrows.collision(c_walls):
                state.all_sprites1.remove(e_arrows)
                state.enemy_arrows.remove(e_arrows)
                e_arrows.move(0,0)
                e_arrows.setPosition(0,0)
        for spikes in state.spike:
            if e_arrows.collision(spikes):
                state.all_sprites1.remove(e_arrows)
                state.enemy_arrows.remove(e_arrows)
                e_arrows.move(0,0)
                e_arrows.setPosition(0,0)
        if e_arrows.collision(state.player) and state.health != 0:
            state.damage_check = True
            state.all_sprites1.remove(e_arrows)
            state.enemy_arrows.remove(e_arrows)
            e_arrows.move(0,0)
            e_arrows.setPosition(0,0)
            if state.player_shield > 0:
                state.player_shield -= 10
                state.shield -= 1
            else:
                if state.health != 0:
                    state.player_health -= 10
                    state.health -= 1
            state.shield_count = 0

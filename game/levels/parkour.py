"""Normal level: the parkour course with enemies, ending at the boss-room door.
"""
import pygame

from game import enemies, loop, physics, player
from game.sprite import Sprite
from game.colors import PINK
from game.loop import add_text
from game.state import state


def build_background():
    """Create the side boundaries, scrolling backgrounds and floor."""
    state.bound1 = Sprite(300, 550, PINK)
    state.bound2 = Sprite(300, 550, PINK)
    state.bound3 = Sprite(300, 550, PINK)
    state.bound4 = Sprite(300, 550, PINK)
    state.bound5 = Sprite(300, 550, PINK)
    state.bound6 = Sprite(300, 550, PINK)
    state.bound7 = Sprite(300, 550, PINK)
    state.bound8 = Sprite(300, 550, PINK)
    state.bound1.setPosition(-500,0)
    state.bound2.setPosition(9000,0)
    state.bound3.setPosition(-300,0)
    state.bound4.setPosition(800,0)
    state.bound5.setPosition(-600,0)
    state.bound6.setPosition(1100,0)
    state.boundaries.append(state.bound1)
    state.boundaries.append(state.bound2)
    state.back1 = Sprite(800, 550, None, "background1.jpg")
    state.back2 = Sprite(800, 550, None, "background1.jpg")
    state.back2.setPosition(800, 0)
    state.background.append(state.back1)
    state.background.append(state.back2)
    state.ground1 = Sprite(800, 90, None,"floor.png")
    state.ground2 = Sprite(800, 90, None, "floor.png")
    state.ground3 = Sprite(400, 50, None, "wall_texture_05.png")
    state.ground4 = Sprite(400, 50, None, "wall_texture_05.png")
    state.ground1.setPosition(0, 460)
    state.ground2.setPosition(800, 460)
    state.ground3.setPosition(1075, 125)
    state.ground4.setPosition(2330, 130)
    state.ground.append(state.ground1)
    state.ground.append(state.ground2)
    state.ground.append(state.ground3)
    state.ground.append(state.ground4)


def build_terrain():
    """Place the walls, climbable (vine) walls and spikes of the parkour course."""
    state.wall1 = Sprite(100, 50, None, "wall_texture_00.png")
    state.wall2 = Sprite(50, 100, None, "wall_texture_06.png")
    state.wall3 = Sprite(100, 50, None, "wall_texture_00.png")
    state.wall4 = Sprite(50, 80, None, "wall_texture_02.png")
    state.wall5 = Sprite(50, 50, None, "wall_texture_03.png")
    state.wall6 = Sprite(50, 25, None, "wall_texture_04.png")
    state.wall7 = Sprite(100,50, None, "wall_texture_00.png")
    state.wall8 = Sprite(100,50, None, "wall_texture_00.png")
    state.wall9 = Sprite(100,50, None, "wall_texture_00.png")
    state.wall10 = Sprite(100,50, None, "wall_texture_00.png")
    state.wall11 = Sprite(50,125, None, "wall_texture_01.png")
    state.wall12 = Sprite(50,125, None, "wall_texture_01.png")
    state.wall13 = Sprite(50,125, None, "wall_texture_01.png")
    state.wall14 = Sprite(50,30,None, "wall_texture_04.png")
    state.wall15 = Sprite(50,75,None, "wall_texture_02.png")
    state.wall1.setPosition(650, 410)
    state.wall2.setPosition(825, 360)
    state.wall3.setPosition(950, 410)
    state.wall4.setPosition(2200, 380)
    state.wall5.setPosition(2030, 290)
    state.wall6.setPosition(2200, 210)
    state.wall7.setPosition(3000, 410)
    state.wall8.setPosition(3200, 410)
    state.wall9.setPosition(3400, 410)
    state.wall10.setPosition(3600, 410)
    state.wall11.setPosition(4850, 335)
    state.wall12.setPosition(5000, 335)
    state.wall13.setPosition(5150, 335)
    state.wall14.setPosition(6900,430)
    state.wall15.setPosition(7500,385)
    state.wall.append(state.wall1)
    state.wall.append(state.wall2)
    state.wall.append(state.wall3)
    state.wall.append(state.wall4)
    state.wall.append(state.wall5)
    state.wall.append(state.wall6)
    state.wall.append(state.wall7)
    state.wall.append(state.wall8)
    state.wall.append(state.wall9)
    state.wall.append(state.wall10)
    state.wall.append(state.wall11)
    state.wall.append(state.wall12)
    state.wall.append(state.wall13)
    state.wall.append(state.wall14)
    state.c_wall1 = Sprite(50, 175, None, "c_wall_texture_08.png")
    state.c_wall2 = Sprite(50, 335, None, "c_wall_texture_01.png")
    state.c_wall3 = Sprite(50, 25, None, "c_wall_texture_02.png")
    state.c_wall4 = Sprite(50, 15, None, "c_wall_texture_03.png")
    state.c_wall5 = Sprite(50, 15, None, "c_wall_texture_03.png")
    state.c_wall6 = Sprite(50, 50, None, "c_wall_texture_04.png")
    state.c_wall7 = Sprite(50, 335, None, "c_wall_texture_01.png")
    state.c_wall8 = Sprite(50, 125, None, "c_wall_texture_00.png")
    state.c_wall9 = Sprite(50,125, None, "c_wall_texture_00.png")
    state.c_wall10 = Sprite(50,160,None, "c_wall_texture_05.png")
    state.c_wall11 = Sprite(50,225,None, "c_wall_texture_06.png")
    state.c_wall12 = Sprite(750,50,None, "c_wall_texture_07.png")
    state.c_wall13 = Sprite(50,225,None, "c_wall_texture_06.png")
    state.c_wall1.setPosition(1025, 125)
    state.c_wall2.setPosition(1425, 125)
    state.c_wall3.setPosition(2200, 355)
    state.c_wall4.setPosition(2030, 280)
    state.c_wall5.setPosition(2200, 195)
    state.c_wall6.setPosition(2280, 130)
    state.c_wall7.setPosition(2700, 130)
    state.c_wall8.setPosition(4700, 335)
    state.c_wall9.setPosition(5300,335)
    state.c_wall10.setPosition(6300,300)
    state.c_wall11.setPosition(6125,30)
    state.c_wall12.setPosition(6175,30)
    state.c_wall13.setPosition(6925,30)
    state.c_wall.append(state.c_wall1)
    state.c_wall.append(state.c_wall2)
    state.c_wall.append(state.c_wall3)
    state.c_wall.append(state.c_wall4)
    state.c_wall.append(state.c_wall5)
    state.c_wall.append(state.c_wall6)
    state.c_wall.append(state.c_wall7)
    state.c_wall.append(state.c_wall8)
    state.c_wall.append(state.c_wall9)
    state.c_wall.append(state.c_wall10)
    state.c_wall.append(state.c_wall11)
    state.c_wall.append(state.c_wall12)
    state.c_wall.append(state.c_wall13)
    state.spike1 = Sprite(100,25,None,"spikes_texture_00.png")
    state.spike2 = Sprite(100,25,None,"spikes_texture_00.png")
    state.spike3 = Sprite(100,25,None,"spikes_texture_00.png")
    state.spike4 = Sprite(100,25,None,"spikes_texture_00.png")
    state.spike5 = Sprite(100,25,None,"spikes_texture_00.png")
    state.spike6 = Sprite(100,25,None,"spikes_texture_00.png")
    state.spike7 = Sprite(100,25,None,"spikes_texture_00.png")
    state.spike8 = Sprite(500,25,None, "spikes_texture_01.png")
    state.spike1.setPosition(3100,435)
    state.spike2.setPosition(3300,435)
    state.spike3.setPosition(3500,435)
    state.spike4.setPosition(4750,435)
    state.spike5.setPosition(4900,435)
    state.spike6.setPosition(5050,435)
    state.spike7.setPosition(5200,435)
    state.spike8.setPosition(6350,435)
    state.spike.append(state.spike1)
    state.spike.append(state.spike2)
    state.spike.append(state.spike3)
    state.spike.append(state.spike4)
    state.spike.append(state.spike5)
    state.spike.append(state.spike6)
    state.spike.append(state.spike7)
    state.spike.append(state.spike8)


def fill_draw_groups():
    """Put the level sprites into the groups that get drawn each frame."""
    state.all_sprites1.add(state.boundaries,state.background,state.ground,state.wall,state.c_wall,state.spike,state.enemy,state.stat_background,state.player)
    state.all_sprites2.add(state.player_stats)


def draw():
    """Draw the level, the player's stat bars and the enemy health bars."""
    state.screen.fill([0, 0, 0])
    state.all_sprites1.draw(state.screen)
    pygame.draw.rect(state.screen,[255,0,0],[27,10,state.player_health,15])
    pygame.draw.rect(state.screen,[211,211,211],[27,25,state.player_shield,15])
    pygame.draw.rect(state.screen,[0,0,255],[27,43,state.player_stamina,15])
    state.all_sprites2.draw(state.screen)
    add_text(str(state.health) + " / 10",[57,10],24,[255,255,255])
    add_text(str(state.shield) + " / 10",[57,27],24,[255,0,0])
    add_text(str(state.stamina) + " / 10",[57,45],23,[255,255,255])
    if state.enemy1_health > 0:
        pygame.draw.rect(state.screen,[0,0,0],[state.enemy1.getX(),state.enemy1.getY() - 30, 50, 8])
        pygame.draw.rect(state.screen,[255,0,0],[state.enemy1.getX() ,state.enemy1.getY() - 30, state.enemy1_health,8])
    if state.enemy2_health > 0:
        pygame.draw.rect(state.screen,[0,0,0],[state.enemy2.getX(),state.enemy2.getY() - 30, 50, 8])
        pygame.draw.rect(state.screen,[255,0,0],[state.enemy2.getX() ,state.enemy1.getY() - 30, state.enemy2_health,8])
    if state.enemy3_health > 0:
        pygame.draw.rect(state.screen,[0,0,0],[state.enemy3.getX(),state.enemy3.getY() - 30, 50, 8])
        pygame.draw.rect(state.screen,[255,0,0],[state.enemy3.getX() ,state.enemy1.getY() - 30, state.enemy3_health,8])
    if state.enemy4_health > 0:
        pygame.draw.rect(state.screen,[0,0,0],[state.enemy4.getX(),state.enemy4.getY() - 30, 50, 8])
        pygame.draw.rect(state.screen,[255,0,0],[state.enemy4.getX() ,state.enemy1.getY() - 30, state.enemy4_health,8])
    if state.enemy5_health > 0:
        pygame.draw.rect(state.screen,[0,0,0],[state.enemy5.getX(),state.enemy5.getY() - 30, 50, 8])
        pygame.draw.rect(state.screen,[255,0,0],[state.enemy5.getX() ,state.enemy1.getY() - 30, state.enemy5_health,8])
    pygame.display.update()


def reset_frame_flags():
    """Clear the per-frame collision flags."""
    state.a_collision = False
    state.e_a_collision = False
    state.collision = False
    state.defend = False
    state.bottom = False
    state.side_collision = False
    state.enemy1_stop_left = False
    state.enemy1_stop_right = False


def check_level_bounds():
    """Stop the player at the left and right ends of the level."""
    if state.player.collision(state.bound1):
        state.playerLeft = False
    elif state.player.collision(state.bound2):
        state.playerRight = False


def handle_events():
    """Keyboard and mouse input for the parkour level."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state.parkour_enemies = False
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
    build_background()
    player.create_player()
    build_terrain()
    enemies.create_enemies()
    player.create_attack_ranges()
    enemies.create_ranges()
    fill_draw_groups()


def frame():
    """One frame of the level, in the exact order of the original loop body."""
    player.update_attack_ranges()
    physics.reset_speeds_and_gravity()
    player.tick_regen_counters()
    draw()
    reset_frame_flags()
    player.update_stats()
    player.update_death()
    player.reset_attack_counter()
    check_level_bounds()
    player.reset_spike_counter()
    player.update_damage_flash()
    player.collide_with_ground()
    player.collide_with_walls()
    player.collide_with_climbable_walls()
    player.collide_with_spikes()
    enemies.face_dead_player()
    enemies.update_enemy1()
    enemies.update_enemy2()
    enemies.update_enemy3()
    enemies.update_enemy4()
    enemies.update_enemy5()
    player.lower_shield_when_hanging()
    physics.scroll_world()
    player.update_idle_pose()
    player.cancel_attack_in_air()
    player.cancel_bow_without_stamina()
    player.update_arrows()
    enemies.update_enemy_arrows()
    physics.apply_gravity()
    physics.wrap_background()
    pygame.display.flip()
    handle_events()


def run():
    """Run the level until its flag turns off (door entered, boss beaten, or window closed)."""
    loop.run(state.clock, 70, lambda: state.parkour_enemies, frame)

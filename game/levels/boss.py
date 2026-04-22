"""Boss level: the mace knight fight and the trophy.
"""
import pygame

from game import loop, physics, player
from game.sprite import Sprite
from game.loop import add_text
from game.state import state


def setup_boss_room():
    """Create the boss, its attack ranges and the boss-room variables."""
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
    state.boss_count1 = 0
    state.damage_count = 0
    state.damage_count2 = 0
    state.weapon = 1
    state.shield = 10
    state.stamina = 10
    state.player_shield = 100
    state.player_stamina = 100
    state.boss_health = 625
    state.boss_facing_left = False
    state.boss_facing_right = False
    state.boss_battle_start = False
    state.mace_reattack = False
    state.boss_range_collision = False
    state.mace_away = False
    state.chain_away = False
    state.attack = False
    state.damage_check = False
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


def rebuild_draw_group():
    """Between attacks: clear projectiles, rebuild what gets drawn, handle winning and the death animation."""
    if not state.chain_away and not state.mace_away:
        for sprites in state.all_sprites3:
            state.all_sprites3.remove(sprites)
        state.all_sprites3.add(state.back3,state.ground1,state.boss,state.arrows)
        if state.health != 0 and state.boss_health != 0:
            state.all_sprites3.add(state.player)


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
    player_on_floor()
    physics.apply_gravity()
    move_player()
    player.update_idle_pose()
    player.cancel_attack_in_air()
    rebuild_draw_group()
    player.reset_attack_counter()
    pygame.display.flip()
    handle_events()


def run():
    """Run the level until its flag turns off (door entered, boss beaten, or window closed)."""
    loop.run(state.boss_clock, 70, lambda: state.boss_battle, frame)

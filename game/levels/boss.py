"""Boss level: the mace knight fight and the trophy.
"""
import pygame

from game import loop, physics, player
from game.loop import add_text
from game.state import state


def setup_boss_room():
    """Create the boss, its attack ranges and the boss-room variables."""
    state.arrows = []
    state.boss_clock = pygame.time.Clock()
    state.boss_count1 = 0
    state.damage_count = 0
    state.damage_count2 = 0
    state.weapon = 1
    state.shield = 10
    state.stamina = 10
    state.player_shield = 100
    state.player_stamina = 100
    state.mace_reattack = False
    state.boss_range_collision = False
    state.attack = False
    state.damage_check = False
    state.a_collision = False
    state.player.setPosition(0,410)
    state.ground1.setPosition(0, 460)
    state.bound7.setPosition(-300,0)
    state.bound8.setPosition(800,0)
    state.all_sprites3.add(state.back3,state.ground1,state.player)


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
    physics.set_boss_room_gravity()
    player.tick_regen_counters()
    draw()
    reset_frame_flags()
    player.update_stats_boss_room()
    player.reset_attack_counter()
    check_room_bounds()
    player_on_floor()
    physics.apply_gravity()
    move_player()
    player.update_idle_pose()
    player.cancel_attack_in_air()
    player.reset_attack_counter()
    pygame.display.flip()
    handle_events()


def run():
    """Run the level until its flag turns off (door entered, boss beaten, or window closed)."""
    loop.run(state.boss_clock, 70, lambda: state.boss_battle, frame)

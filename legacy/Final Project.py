import pygame, time
from Sprite import Sprite
pygame.init()
#-----Screen-----
screen = pygame.display.set_mode([800, 550])
screen.fill([0, 0, 0])
pygame.display.set_caption("Link's Dungeon")
#-----Functions-----
def add_text(my_text,position,size,color): # This functions is to add a text on screen
    my_font = pygame.font.SysFont(None,size)
    text = my_font.render(my_text, True,color)
    screen.blit(text,position)
def enemy_death_left(count,name,group): # This function is for when the enemy dies while facing left
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
def enemy_death_right(count,name,group): # This function is for when the enemy dies while facing right
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
def enemy_shoot_left(count,name,arrow_group,group): # This fuction is for the enemy's animation for shooting while facing left
    if count == 1:
        name.setImageIndex(1)
    if count == 15:
        name.setImageIndex(2)
    if count == 30:
        name.setImageIndex(3)
        e_arrow = Sprite(30,12,None,"arrow_left_00.png")
        e_arrow.xSpeed = -groundSpeed - 2
        e_arrow.setPosition(name.getX() - 30, name.getY() + (name.getWidth() / 2) - 5)
        arrow_group.append(e_arrow)
        group.add(arrow_group)
    if count == 45:
        name.setImageIndex(24)
    if count == 85:
        count = 0
def enemy_shoot_right(count,name,arrow_group,group): # This fuction is for the enemy's animation for shooting while facing right
    if count == 1:
        name.setImageIndex(13)
    if count == 15:
        name.setImageIndex(14)
    if count == 30:
        name.setImageIndex(15)
        e_arrow = Sprite(30,12,None,"arrow_right_00.png")
        e_arrow.xSpeed = groundSpeed + 2
        e_arrow.setPosition(name.getX() + name.getWidth(), name.getY() + (name.getWidth() / 2) - 5)
        arrow_group.append(e_arrow)
        group.add(arrow_group)
    if count == 45:
        name.setImageIndex(27)
    if count == 85:
        count = 0
def enemy_attack_right(count,name): # This function is for the enemy's animation when attacking with the sword while facing right
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
def enemy_attack_left(count,name): # This function is for the enemy's animation when attacking with the sword while facing left
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
def countdown(start): # This is for the countdown before at the start of the game
    for i in range(start,0,-1):
        screen.fill([0,0,0])
        add_text(str(i),[400,225],100,[255,255,255])
        pygame.display.flip()
        time.sleep(1)
    screen.fill([0,0,0])
    add_text("ENJOY!!!",[275,225],100,[255,255,255])
    pygame.display.flip()
    time.sleep(1)
# -----Colors-----
PINK = [255, 192, 203]
PURPLE = [128, 0, 128]
GREEN = [0, 255, 0]
RED = [255, 0, 0]
BLUE = [0, 0, 255]
YELLOW = [255, 255, 102]
BROWN = [150,75,0]
BLACK = [0,0,0]
#-----FPS-----
clock = pygame.time.Clock()
#-----Sprite Lists-----
all_sprites1 = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
all_sprites3 = pygame.sprite.Group()
#-----Lists-----
boundaries = []
background = []
ground = []
wall = []
c_wall = []
character = []
spike= []
enemy = []
doors = []
arrows  = []
enemy_arrows = []
#-----Variables-----
yVelocity = 0
gravity = 0.1
weapon = 1
backgroundPosition = 799
background_position = 799
groundPosition = 790
ground_position = 790
backgroundSpeed = 1
background_speed = 1
norm_speed = 4
groundSpeed = 4
player_count = 0
shield_count = 0
stamina_count = 0
arrows_taken = 0
door_count = 0
door_appearance = 0
enemy1_count = 0
enemy1_death_ani = 0
enemy1_health = 50
enemy2_count = 0
enemy2_death_ani = 0
enemy2_health = 50
enemy3_count = 0
enemy3_death_ani = 0
enemy3_health = 50
enemy4_count = 0
enemy4_death_ani = 0
enemy4_health = 50
enemy5_count = 0
enemy5_death_ani = 0
enemy5_health = 50
enemy6_count = 0
enemy6_death_ani = 0
enemy6_health = 50
enemy7_count = 0
enemy7_death_ani = 0
enemy7_health = 50
enemy8_count = 0
enemy8_death_ani = 0
enemy8_health = 50
death_counter = 0
damage_counter = 0
damage_count = 0
over = 0
health = 10
shield = 10
stamina = 10
speed = 2
player_health = 100
player_shield = 100
player_stamina = 100
#-----Booleans-----
parkour_enemies = False
boss_battle = True
countdowned = True
a_collision = False
e_a_collision = False
credit = False
playerRight = False
playerLeft = False
jump = False
attack = False
side_collision = False
defend = False
bottom = False
collision = False
enter = False
playerUp = False
enemy_move = False
enemy_facing_left = True
enemy_facing_right = False
playerDown = False
facingLeft = False
facingRight = True
enemy_attack = False
extra_gravity = False
spike_collision = False
damage_check = False
enemy1_stop_left = False
enemy1_stop_right = False
enemy2_stop_left = False
enemy2_stop_right = False
enemy3_stop_left = False
enemy3_stop_right = False
enemy4_stop_left = False
enemy4_stop_right = False
enemy5_stop_left = False
enemy5_stop_right = False
enemy6_stop_left = False
enemy6_stop_right = False
enemy7_stop_left = False
enemy7_stop_right = False
enemy8_stop_left = False
enemy8_stop_right = False
#-----Sprites-----
bound1 = Sprite(300, 550, PINK)
bound2 = Sprite(300, 550, PINK)
bound3 = Sprite(300,550,PINK)
bound4 = Sprite(300,550,PINK)
bound5 = Sprite(300,550,PINK)
bound6 = Sprite(300,550,PINK)
bound7 = Sprite(300,550,PINK)
bound8 = Sprite(300,550,PINK)
bound1.setPosition(-500,0)
bound2.setPosition(9000,0)
bound3.setPosition(-300,0)
bound4.setPosition(800,0)
bound5.setPosition(-600,0)
bound6.setPosition(1100,0)
boundaries.append(bound1)
boundaries.append(bound2)
back1 = Sprite(800, 550, None, "background1.jpg")
back2 = Sprite(800, 550, None, "background1.jpg")
back3 = Sprite(800, 550, None, "background2.png")
back2.setPosition(800, 0)
background.append(back1)
background.append(back2)
ground1 = Sprite(800, 90, None,"floor.png")
ground2 = Sprite(800, 90, None, "floor.png")
ground3 = Sprite(400, 50, None, "wall_texture_05.png")
ground4 = Sprite(400, 50, None, "wall_texture_05.png")
ground1.setPosition(0, 460)
ground2.setPosition(800, 460)
ground3.setPosition(1075, 125)
ground4.setPosition(2330, 130)
ground.append(ground1)
ground.append(ground2)
ground.append(ground3)
ground.append(ground4)
player = Sprite(50,50,None,"walking_right_00.png") 
player.addImage("walking_right_01.png") 
player.addImage("walking_right_02.png") 
player.addImage("walking_right_03.png") 
player.addImage("walking_right_04.png") 
player.addImage("walking_right_05.png") 
player.addImage("walking_right_06.png") 
player.addImage("walking_right_07.png") 
player.addImage("walking_right_08.png") 
player.addImage("walking_left_00.png") 
player.addImage("walking_left_01.png") 
player.addImage("walking_left_02.png") 
player.addImage("walking_left_03.png") 
player.addImage("walking_left_04.png") 
player.addImage("walking_left_05.png") 
player.addImage("walking_left_06.png") 
player.addImage("walking_left_07.png") 
player.addImage("walking_left_08.png") 
player.addImage("jumping_right_00.png") 
player.addImage("jumping_right_01.png") 
player.addImage("jumping_left_00.png") 
player.addImage("jumping_left_01.png")
player.addImage("left_attack_00.png") 
player.addImage("left_attack_01.png") 
player.addImage("left_attack_02.png") 
player.addImage("left_attack_03.png") 
player.addImage("left_attack_04.png") 
player.addImage("right_attack_00.png") 
player.addImage("right_attack_01.png") 
player.addImage("right_attack_02.png") 
player.addImage("right_attack_03.png") 
player.addImage("right_attack_04.png") 
player.addImage("link_idle_00.png") 
player.addImage("falling_idle_00.png") 
player.addImage("falling_idle_01.png")
player.addImage("climbing_right_00.png") 
player.addImage("climbing_right_01.png") 
player.addImage("climbing_right_02.png")
player.addImage("climbing_left_00.png") 
player.addImage("climbing_left_01.png") 
player.addImage("climbing_left_02.png")
player.addImage("climbing_right_02.png")
player.addImage("climbing_right_01.png") 
player.addImage("climbing_right_00.png") 
player.addImage("climbing_left_02.png") 
player.addImage("climbing_left_01.png") 
player.addImage("climbing_left_00.png") 
player.addImage("hanging_right_00.png")
player.addImage("hanging_right_01.png") 
player.addImage("hanging_right_02.png") 
player.addImage("hanging_right_03.png") 
player.addImage("hanging_left_00.png") 
player.addImage("hanging_left_01.png") 
player.addImage("hanging_left_02.png") 
player.addImage("hanging_left_03.png") 
player.addImage("hanging_idle_00.png") 
player.addImage("defend_right_00.png") 
player.addImage("defend_right_01.png")
player.addImage("defend_right_02.png") 
player.addImage("defend_right_03.png") 
player.addImage("defend_right_04.png") 
player.addImage("defend_right_05.png") 
player.addImage("defend_right_06.png")
player.addImage("defend_right_07.png") 
player.addImage("defend_right_08.png") 
player.addImage("defend_left_00.png") 
player.addImage("defend_left_01.png") 
player.addImage("defend_left_02.png") 
player.addImage("defend_left_03.png")
player.addImage("defend_left_04.png") 
player.addImage("defend_left_05.png") 
player.addImage("defend_left_06.png")
player.addImage("defend_left_07.png") 
player.addImage("defend_left_08.png")
player.addImage("shooting_right_00.png") 
player.addImage("shooting_right_01.png") 
player.addImage("shooting_right_02.png") 
player.addImage("shooting_left_00.png") 
player.addImage("shooting_left_01.png")
player.addImage("shooting_left_02.png") 
player.addImage("link_death_ani_00.png") 
player.addImage("link_death_ani_01.png") 
player.addImage("link_death_ani_02.png") 
player.addImage("link_death_ani_03.png") 
player.addImage("link_death_ani_04.png") 
player.addImage("link_damage_left_00.png") 
player.addImage("link_damage_right_00.png") 
player_stats = Sprite(134,68,None,"player_stats.png")
stat_background = Sprite(134,68,BLACK)
player.setPosition(325,0)
character.append(player)
wall1 = Sprite(100, 50, None, "wall_texture_00.png")
wall2 = Sprite(50, 125, None, "wall_texture_01.png")
wall3 = Sprite(100, 50, None, "wall_texture_00.png")
wall4 = Sprite(50, 80, None, "wall_texture_02.png")
wall5 = Sprite(50, 50, None, "wall_texture_03.png")
wall6 = Sprite(50, 25, None, "wall_texture_04.png")
wall7 = Sprite(100,50, None, "wall_texture_00.png")
wall8 = Sprite(100,50, None, "wall_texture_00.png")
wall9 = Sprite(100,50, None, "wall_texture_00.png")
wall10 = Sprite(100,50, None, "wall_texture_00.png")
wall11 = Sprite(50,125, None, "wall_texture_01.png")
wall12 = Sprite(50,125, None, "wall_texture_01.png")
wall13 = Sprite(50,125, None, "wall_texture_01.png")
wall14 = Sprite(50,75,None, "wall_texture_02.png")
wall15 = Sprite(50,75,None, "wall_texture_02.png")
wall1.setPosition(650, 410)
wall2.setPosition(825, 335)
wall3.setPosition(950, 410)
wall4.setPosition(2200, 380)
wall5.setPosition(2030, 290)
wall6.setPosition(2200, 210)
wall7.setPosition(3000, 410)
wall8.setPosition(3200, 410)
wall9.setPosition(3400, 410)
wall10.setPosition(3600, 410)
wall11.setPosition(4850, 335)
wall12.setPosition(5000, 335)
wall13.setPosition(5150, 335)
wall14.setPosition(7000,385)
wall15.setPosition(7500,385)
wall.append(wall1)
wall.append(wall2)
wall.append(wall3)
wall.append(wall4)
wall.append(wall5)
wall.append(wall6)
wall.append(wall7)
wall.append(wall8)
wall.append(wall9)
wall.append(wall10)
wall.append(wall11)
wall.append(wall12)
wall.append(wall13)
c_wall1 = Sprite(50, 125, None, "c_wall_texture_00.png")
c_wall2 = Sprite(50, 335, None, "c_wall_texture_01.png")
c_wall3 = Sprite(50, 25, None, "c_wall_texture_02.png")
c_wall4 = Sprite(50, 15, None, "c_wall_texture_03.png")
c_wall5 = Sprite(50, 15, None, "c_wall_texture_03.png")
c_wall6 = Sprite(50, 50, None, "c_wall_texture_04.png")
c_wall7 = Sprite(50, 335, None, "c_wall_texture_01.png")
c_wall8 = Sprite(50, 125, None, "c_wall_texture_00.png")
c_wall9 = Sprite(50,125, None, "c_wall_texture_00.png")
c_wall10 = Sprite(50,160,None, "c_wall_texture_05.png")
c_wall11 = Sprite(50,225,None, "c_wall_texture_06.png")
c_wall12 = Sprite(750,50,None, "c_wall_texture_07.png")
c_wall13 = Sprite(50,225,None, "c_wall_texture_06.png")
c_wall1.setPosition(1025, 125)
c_wall2.setPosition(1425, 125)
c_wall3.setPosition(2200, 355)
c_wall4.setPosition(2030, 280)
c_wall5.setPosition(2200, 195)
c_wall6.setPosition(2280, 130)
c_wall7.setPosition(2700, 130)
c_wall8.setPosition(4700, 335)
c_wall9.setPosition(5300,335)
c_wall10.setPosition(6300,300)
c_wall11.setPosition(6125,30)
c_wall12.setPosition(6175,30)
c_wall13.setPosition(6925,30)
c_wall.append(c_wall1)
c_wall.append(c_wall2)
c_wall.append(c_wall3)
c_wall.append(c_wall4)
c_wall.append(c_wall5)
c_wall.append(c_wall6)
c_wall.append(c_wall7)
c_wall.append(c_wall8)
c_wall.append(c_wall9)
c_wall.append(c_wall10)
c_wall.append(c_wall11)
c_wall.append(c_wall12)
c_wall.append(c_wall13)
spike1 = Sprite(100,25,None,"spikes_texture_00.png")
spike2 = Sprite(100,25,None,"spikes_texture_00.png")
spike3 = Sprite(100,25,None,"spikes_texture_00.png")
spike4 = Sprite(100,25,None,"spikes_texture_00.png")
spike5 = Sprite(100,25,None,"spikes_texture_00.png")
spike6 = Sprite(100,25,None,"spikes_texture_00.png")
spike7 = Sprite(100,25,None,"spikes_texture_00.png")
spike8 = Sprite(500,25,None, "spikes_texture_01.png")
spike1.setPosition(3100,435)
spike2.setPosition(3300,435)
spike3.setPosition(3500,435)
spike4.setPosition(4750,435)
spike5.setPosition(4900,435)
spike6.setPosition(5050,435)
spike7.setPosition(5200,435)
spike8.setPosition(6350,435)
spike.append(spike1)
spike.append(spike2)
spike.append(spike3)
spike.append(spike4)
spike.append(spike5)
spike.append(spike6)
spike.append(spike7)
spike.append(spike8)
enemy1 = Sprite(50,50,None,"enemy_walking_left_00.png")
enemy2 = Sprite(50,50,None,"enemy_walking_left_00.png")
enemy3 = Sprite(50,50,None,"enemy_walking_left_00.png")
enemy4 = Sprite(50,50,None,"enemy_walking_left_00.png")
enemy5 = Sprite(50,50,None,"enemy_walking_left_00.png")
enemy6 = Sprite(50,50,None,"enemy_walking_left_00.png")
enemy7 = Sprite(50,50,None,"enemy_walking_left_00.png")
enemy8 = Sprite(50,50,None,"enemy_walking_left_00.png")
enemy1.setPosition(4000,410)
enemy2.setPosition(4200,410)
enemy3.setPosition(2000,410)
enemy4.setPosition(5700,410)
enemy5.setPosition(5900,410)
enemy6.setPosition(7400,410)
enemy7.setPosition(7600,410)
enemy8.setPosition(7800,410)
enemy.append(enemy1)
enemy.append(enemy2)
enemy.append(enemy3)
enemy.append(enemy4)
enemy.append(enemy5)
enemy.append(enemy6)
enemy.append(enemy7)
enemy.append(enemy8)
for enemies in enemy:
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
player_range1 = Sprite(30,50,RED)
player_range2 = Sprite(30,50,RED)
enemy1_range1 = Sprite(50,50,RED)
enemy1_range2 = Sprite(50,50,RED)
enemy1_range3 = Sprite(100,200,BLUE)
enemy1_range4 = Sprite(100,200,BLUE)
enemy1_range5 = Sprite(950,550,GREEN)
enemy2_range1 = Sprite(50,50,RED)
enemy2_range2 = Sprite(50,50,RED)
enemy2_range3 = Sprite(100,200,BLUE)
enemy2_range4 = Sprite(100,200,BLUE)
enemy2_range5 = Sprite(950,550,GREEN)
enemy3_range1 = Sprite(50,50,RED)
enemy3_range2 = Sprite(50,50,RED)
enemy3_range3 = Sprite(100,200,BLUE)
enemy3_range4 = Sprite(100,200,BLUE)
enemy3_range5 = Sprite(950,550,GREEN)
enemy4_range1 = Sprite(50,50,RED)
enemy4_range2 = Sprite(50,50,RED)
enemy4_range3 = Sprite(100,200,BLUE)
enemy4_range4 = Sprite(100,200,BLUE)
enemy4_range5 = Sprite(950,550,GREEN)
enemy5_range1 = Sprite(50,50,RED)
enemy5_range2 = Sprite(50,50,RED)
enemy5_range3 = Sprite(100,200,BLUE)
enemy5_range4 = Sprite(100,200,BLUE)
enemy5_range5 = Sprite(950,550,GREEN)
enemy6_range1 = Sprite(50,50,RED)
enemy6_range2 = Sprite(50,50,RED)
enemy6_range3 = Sprite(100,200,BLUE)
enemy6_range4 = Sprite(100,200,BLUE)
enemy6_range5 = Sprite(950,550,GREEN)
enemy7_range1 = Sprite(50,50,RED)
enemy7_range2 = Sprite(50,50,RED)
enemy7_range3 = Sprite(100,200,BLUE)
enemy7_range4 = Sprite(100,200,BLUE)
enemy7_range5 = Sprite(950,550,GREEN)
enemy8_range1 = Sprite(50,50,RED)
enemy8_range2 = Sprite(50,50,RED)
enemy8_range3 = Sprite(100,200,BLUE)
enemy8_range4 = Sprite(100,200,BLUE)
enemy8_range5 = Sprite(950,550,GREEN)
arrow = Sprite(30,12,None,"arrow_right_00.png")
door = Sprite(105,150,None,"door_texture_00.png") 
door.addImage("door_texture_01.png") 
door.addImage("door_texture_02.png") 
door.addImage("door_texture_03.png") 
door.addImage("door_texture_04.png") 
door.addImage("door_texture_05.png") 
door.setPosition(7000,310)
door_background = Sprite(105,150,None, "door_texture_06.png")
door_background.setPosition(7000,310)
doors.append(door_background)
doors.append(door)
all_sprites1.add(boundaries,background,ground,wall,c_wall,spike,enemy,stat_background,player)
all_sprites2.add(player_stats)
print("""
This game is made by:
    Ahron Ramos

Objective:
    Kill all the Enemies and defeat the Boss

Parkour Details:
    normal wall - you can't climb it and you can't go into it. You can only walk on it
    wall w/ vines - you can climb up and down and sideways in it
    spikes - it deals damage to you whenever you collide with it

    *there's no fall damage unless you fall on spikes*

Player Stats details:
    red bar - health (doesn't regenerate)
    white bar - shield (regenerates)
    blue bar - ammo/ stamina (regenarates, only available for bow n arrow)

Controls:
    Change Weapons:
        1 - sword
        2 - bow n arrow

    Movement:
        w - climb up
        s - climb down
        a - move left
        d - move right
        space bar - jump

    Attacks:
        use mouse to attack
        
    Others:
        o - enter the boss room
        t - pick up trophy
""")
if countdowned:
    countdown(3)
while parkour_enemies:
    clock.tick(60)
    if enemy1_health == 0 and enemy2_health == 0 and enemy3_health == 0 and enemy4_health == 0 and enemy5_health == 0 and enemy6_health == 0 and enemy7_health == 0 and enemy8_health == 0:
        door_appearance += 1
        if door_appearance == 75:
            for i in all_sprites1:
                all_sprites1.remove(i)
            all_sprites1.add(boundaries,background,ground,wall,c_wall,spike,stat_background,doors,player)
    if player.collision(door) and enter:
        door_count += 1
        playerLeft = False
        playerRight = False
        jump = False
#-----Door Animation-----
        if door_count == 1:
            door.setImageIndex(0)
        if door_count == 15:
            door.setImageIndex(1)
        if door_count == 30:
            door.setImageIndex(2)
        if door_count == 45:
            door.setImageIndex(3)
        if door_count == 60:
            door.setImageIndex(4)
        if door_count == 75:
            door.setImageIndex(5)
        if door_count == 150:
            parkour_enemies = False
            boss_battle = True
#-----Range Positions-----
    player_range1.setPosition(player.getX() - 30, player.getY())
    player_range2.setPosition(player.getX() + player.getWidth(),player.getY())
#-----Variables-----
    backgroundSpeed = 1
    groundSpeed = 4
    if health != 0:
        gravity = 0.08
    else:
        gravity = 0
        yVelocity = 0
#-----Counts-----
    shield_count += 1
    stamina_count += 1
    screen.fill([0, 0, 0])
    all_sprites1.draw(screen)
#-----Player Stats Display-----
    pygame.draw.rect(screen,[255,0,0],[27,10,player_health,15])
    pygame.draw.rect(screen,[211,211,211],[27,25,player_shield,15])
    pygame.draw.rect(screen,[0,0,255],[27,43,player_stamina,15])
    all_sprites2.draw(screen)
    add_text(str(health) + " / 10",[57,10],24,[255,255,255])
    add_text(str(shield) + " / 10",[57,27],24,[255,0,0])
    add_text(str(stamina) + " / 10",[57,45],23,[255,255,255])
#-----Enemy Health Display-----
    if enemy1_health > 0:
        pygame.draw.rect(screen,[0,0,0],[enemy1.getX(),enemy1.getY() - 30, 50, 8])
        pygame.draw.rect(screen,[255,0,0],[enemy1.getX() ,enemy1.getY() - 30, enemy1_health,8])
    if enemy2_health > 0:
        pygame.draw.rect(screen,[0,0,0],[enemy2.getX(),enemy2.getY() - 30, 50, 8])
        pygame.draw.rect(screen,[255,0,0],[enemy2.getX() ,enemy1.getY() - 30, enemy2_health,8])
    if enemy3_health > 0:
        pygame.draw.rect(screen,[0,0,0],[enemy3.getX(),enemy3.getY() - 30, 50, 8])
        pygame.draw.rect(screen,[255,0,0],[enemy3.getX() ,enemy1.getY() - 30, enemy3_health,8])
    if enemy4_health > 0:
        pygame.draw.rect(screen,[0,0,0],[enemy4.getX(),enemy4.getY() - 30, 50, 8])
        pygame.draw.rect(screen,[255,0,0],[enemy4.getX() ,enemy1.getY() - 30, enemy4_health,8])
    if enemy5_health > 0:
        pygame.draw.rect(screen,[0,0,0],[enemy5.getX(),enemy5.getY() - 30, 50, 8])
        pygame.draw.rect(screen,[255,0,0],[enemy5.getX() ,enemy1.getY() - 30, enemy5_health,8])
    if enemy6_health > 0:
        pygame.draw.rect(screen,[0,0,0],[enemy6.getX(),enemy6.getY() - 30, 50, 8])
        pygame.draw.rect(screen,[255,0,0],[enemy6.getX() ,enemy1.getY() - 30, enemy6_health,8])
    if enemy7_health > 0:
        pygame.draw.rect(screen,[0,0,0],[enemy7.getX(),enemy7.getY() - 30, 50, 8])
        pygame.draw.rect(screen,[255,0,0],[enemy7.getX() ,enemy1.getY() - 30, enemy7_health,8])
    if enemy8_health > 0:
        pygame.draw.rect(screen,[0,0,0],[enemy8.getX(),enemy8.getY() - 30, 50, 8])
        pygame.draw.rect(screen,[255,0,0],[enemy8.getX() ,enemy1.getY() - 30, enemy8_health,8])    
    pygame.display.update()
#-----Booleans-----
    a_collision = False
    e_a_collision = False
    collision = False
    defend = False
    bottom = False
    side_collision = False
    enemy1_stop_left = False
    enemy1_stop_right = False
#-----Player Stats-----
    if player_health <= 0:
        player_health = 0
        health = 0
    if player_stamina <= 0:
        player_stamina = 0
        stamina = 0
    if player_shield <= 0:
        player_shield = 0
        shield = 0
    if player_health >= 100:
        player_health = 100
        health = 10
    if player_stamina >= 100:
        player_stamina = 100
        stamina = 10
    if player_shield >= 100:
        player_shield = 100
        shield = 10
    if health != 0:
        if stamina_count >= 300:
            if stamina != 10:
                player_stamina += 10
                stamina += 1
            stamina_count = 120
        if shield_count >= 300:
            if shield != 10:
                player_shield += 10
                shield += 1
            shield_count = 180
#-----Player Death Animation-----
    if health == 0:
        playerLeft = False
        playerRight = False
        playerUp = False
        playerDown = False
        playerUp = False
        jump = False
        attack = False
        death_counter += 1
        if death_counter == 1:
            player.setImageIndex(80)
        if death_counter == 15:
            player.setImageIndex(81)
        if death_counter == 30:
            player.setImageIndex(82)
        if death_counter == 45:
            player.setImageIndex(83)
        if death_counter == 60:
            player.setImageIndex(84)
        if death_counter == 75:
            all_sprites1.remove(player)
            print("""Good Try!

Please Try Again!!!""")
    if not attack:
        player_count = 0
#-----Player Boundaries-----
    if player.collision(bound1):
        playerLeft = False
    elif player.collision(bound2):
        playerRight = False
#-----Spike Code-----
    for spikes in spike:
        if not player.collision(spikes):
            damage_counter = 0
#-----Player Damaged Animation-----
    if damage_check and health != 0:
        damage_count += 1
        if facingLeft:
            if damage_count == 1:
                player.setImageIndex(85)
            if damage_count == 15:
                damage_count = 0
                damage_check = False
        if facingRight:
            if damage_count == 1:
                player.setImageIndex(86)
            if damage_count == 15:
                damage_count = 0
                damage_check = False
#-----Ground Code-----
    for i in ground:
#-----Ground Boundaries-----
        if (i.getY() <= player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() + i.getWidth() - 10 <= player.getX() <= i.getX() + i.getWidth() + 2: 
            playerLeft = False
        elif (i.getY() <= player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() - 2 <= player.getX() + player.getWidth() <= i.getX() + 10:
            playerRight = False
#-----Player Movement Animation-----
        elif (i.getX() <= player.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= player.getY() + player.getHeight() <= i.getY() + 10:
            if playerLeft:
                player.imageStartEnd(9,17,5)
            elif playerRight:
                player.imageStartEnd(0,8,5)
            collision = True
            bottom = False
            yVelocity = 0
            playerDown = False
            if jump:
                yVelocity = -3
            if defend:
                playerRight = False
                playerLeft = False
                if facingLeft:
                    player.setImageIndex(65)
                if facingRight:
                    player.setImageIndex(56)
#-----Player Attacks-----
            if attack:
                if health != 0:
                    player_count += 1
                    jump = False
                    playerRight = False
                    playerLeft = False
                    if weapon == 1:
                        if facingLeft:
                            if player_count == 1:
                                player.setImageIndex(22)
                            if player_count == 10:
                                player.setImageIndex(23)
                            if player_count == 20:
                                player.setImageIndex(24)
                            if player_count == 30:
                               player.setImageIndex(25)
                            if player_count == 40:
                                player.setImageIndex(26)
                                if player_range1.collision(enemy1):
                                    enemy1_health -= 10
                                if player_range1.collision(enemy2):
                                    enemy2_health -= 10
                                if player_range1.collision(enemy3):
                                    enemy3_health -= 10
                                if player_range1.collision(enemy4):
                                    enemy4_health -= 10
                                if player_range1.collision(enemy5):
                                    enemy5_health -= 10
                                if player_range1.collision(enemy6):
                                    enemy6_health -= 10
                                if player_range1.collision(enemy7):
                                    enemy7_health -= 10
                                if player_range1.collision(enemy8):
                                    enemy8_health -= 10
                                player_count = 0
                                attack = False
                        if facingRight:
                            if player_count == 1:
                                player.setImageIndex(27)
                            if player_count == 10:
                                player.setImageIndex(28)
                            if player_count == 20:
                                player.setImageIndex(29)
                            if player_count == 30:
                               player.setImageIndex(30)
                            if player_count == 40:
                                player.setImageIndex(31)
                                if player_range2.collision(enemy1):
                                    enemy1_health -= 10
                                if player_range2.collision(enemy2):
                                    enemy2_health -= 10
                                if player_range2.collision(enemy3):
                                    enemy3_health -= 10
                                if player_range2.collision(enemy4):
                                    enemy4_health -= 10
                                if player_range2.collision(enemy5):
                                    enemy5_health -= 10
                                if player_range2.collision(enemy6):
                                    enemy6_health -= 10
                                if player_range2.collision(enemy7):
                                    enemy7_health -= 10
                                if player_range2.collision(enemy8):
                                    enemy8_health -= 10
                                player_count = 0
                                attack = False
                    if weapon == 2:
                        if stamina > 0:
                            if facingLeft:
                                if player_count == 1:
                                    player.setImageIndex(77)
                                if player_count == 15:
                                    player.setImageIndex(78)
                                if player_count == 30:
                                    player.setImageIndex(79)
                                    player_count = 0
                                    attack = False
                                    arrow = Sprite(30,12,None,"arrow_left_00.png")
                                    arrow.xSpeed = -groundSpeed - 2
                                    arrow.setPosition(player.getX() - 30, player.getY() + (player.getWidth() / 2) - 5)
                                    arrows.append(arrow)
                                    all_sprites1.add(arrow)
                                    player_stamina -= 10
                                    stamina_count = 0
                                    stamina -= 1
                            if facingRight:
                                if player_count == 1:
                                    player.setImageIndex(74)
                                if player_count == 15:
                                    player.setImageIndex(75)
                                if player_count == 30:
                                    player.setImageIndex(76)
                                    player_count = 0
                                    attack = False
                                    arrow = Sprite(30,12,None,"arrow_right_00.png")
                                    arrow.xSpeed = groundSpeed + 2
                                    arrow.setPosition(player.getX() + player.getWidth(), player.getY() + (player.getWidth() / 2) - 5)
                                    arrows.append(arrow)
                                    all_sprites1.add(arrow)
                                    player_stamina -= 10
                                    stamina -= 1
                                    stamina_count = 0
                        else:
                            player_count = 0
                            attack = False
        elif (i.getX() <= player.getX() + 25 <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 15 <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 35 <= i.getX() + i.getWidth()) and i.getY() + i.getHeight() - 10 <= player.getY() <= i.getY() + i.getHeight() + 2: 
            playerUp = False
            yVelocity += 1
#-----Wall Code-----
    for i in wall:
#-----Wall Boundaries
        if (i.getY() <= player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() + i.getWidth() - 10 <= player.getX() <= i.getX() + i.getWidth() + 2:
            playerLeft = False
        elif (i.getY() <= player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() - 2 <= player.getX() + player.getWidth() <= i.getX() + 10: 
            playerRight = False
#-----Player Movement-----
        elif (i.getX() <= player.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= player.getY() + player.getHeight() <= i.getY() + 10: 
            if playerLeft:
                player.imageStartEnd(9,17,5)
            elif playerRight:
                player.imageStartEnd(0,8,5)
            collision = True
            bottom = False
            yVelocity = 0
            playerDown = False
            if jump:
                yVelocity = -3
            if defend:
                playerRight = False
                playerLeft = False
                if facingLeft:
                    player.setImageIndex(65)
                if facingRight:
                    player.setImageIndex(56)
#-----Player Attacks-----
            if attack:
                if health != 0:
                    player_count += 1
                    jump = False
                    playerRight = False
                    playerLeft = False
                    if weapon == 1:
                        if facingLeft:
                            if player_count == 1:
                                player.setImageIndex(22)
                            if player_count == 10:
                                player.setImageIndex(23)
                            if player_count == 20:
                                player.setImageIndex(24)
                            if player_count == 30:
                               player.setImageIndex(25)
                            if player_count == 40:
                                player.setImageIndex(26)
                                if player_range1.collision(enemy1):
                                    enemy1_health -= 10
                                if player_range1.collision(enemy2):
                                    enemy2_health -= 10
                                if player_range1.collision(enemy3):
                                    enemy3_health -= 10
                                if player_range1.collision(enemy4):
                                    enemy4_health -= 10
                                if player_range1.collision(enemy5):
                                    enemy5_health -= 10
                                if player_range1.collision(enemy6):
                                    enemy6_health -= 10
                                if player_range1.collision(enemy7):
                                    enemy7_health -= 10
                                if player_range1.collision(enemy8):
                                    enemy8_health -= 10
                                player_count = 0
                                attack = False
                        if facingRight:
                            if player_count == 1:
                                player.setImageIndex(27)
                            if player_count == 10:
                                player.setImageIndex(28)
                            if player_count == 20:
                                player.setImageIndex(29)
                            if player_count == 30:
                               player.setImageIndex(30)
                            if player_count == 40:
                                player.setImageIndex(31)
                                if player_range2.collision(enemy1):
                                    enemy1_health -= 10
                                if player_range2.collision(enemy2):
                                    enemy2_health -= 10
                                if player_range2.collision(enemy3):
                                    enemy3_health -= 10
                                if player_range2.collision(enemy4):
                                    enemy4_health -= 10
                                if player_range2.collision(enemy5):
                                    enemy5_health -= 10
                                if player_range2.collision(enemy6):
                                    enemy6_health -= 10
                                if player_range2.collision(enemy7):
                                    enemy7_health -= 10
                                if player_range2.collision(enemy8):
                                    enemy8_health -= 10
                                player_count = 0
                                attack = False
                    if weapon == 2:
                        if player_stamina > 0:
                            if facingLeft:
                                if player_count == 1:
                                    player.setImageIndex(77)
                                if player_count == 15:
                                    player.setImageIndex(78)
                                if player_count == 30:
                                    player.setImageIndex(79)
                                    player_count = 0
                                    attack = False
                                    arrow = Sprite(30,12,None,"arrow_left_00.png")
                                    arrow.xSpeed = -groundSpeed - 2
                                    arrow.setPosition(player.getX() - 30, player.getY() + (player.getWidth() / 2) - 5)
                                    arrows.append(arrow)
                                    all_sprites1.add(arrow)
                                    player_stamina -= 10
                                    stamina_count = 0
                                    stamina -= 1
                            if facingRight:
                                if player_count == 1:
                                    player.setImageIndex(74)
                                if player_count == 15:
                                    player.setImageIndex(75)
                                if player_count == 30:
                                    player.setImageIndex(76)
                                    player_count = 0
                                    attack = False
                                    arrow = Sprite(30,12,None,"arrow_right_00.png")
                                    arrow.xSpeed = groundSpeed + 2
                                    arrow.setPosition(player.getX() + player.getWidth(), player.getY() + (player.getWidth() / 2) - 5)
                                    arrows.append(arrow)
                                    all_sprites1.add(arrow)
                                    player_stamina -= 10
                                    stamina -= 1
                                    stamina_count = 0
                        else:
                            player_count = 0
                            attack = False
        elif (i.getX() <= player.getX() + 25 <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 15 <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 35 <= i.getX() + i.getWidth()) and i.getY() + i.getHeight() - 10 <= player.getY() <= i.getY() + i.getHeight() + 2: 
            playerUp = False
            yVelocity += 1
#-----Climbable Wall Code-----
    for i in c_wall:
        if (i.getY() <= player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() + i.getWidth() - 10 <= player.getX() <= i.getX() + i.getWidth() + 2:
#-----Player Climbing-----
            bottom = False
            collision = True
            playerLeft = False
            side_collision = True
            gravity = 0
            yVelocity = 0
            if playerUp:
                yVelocity = -2.5
                player.imageStartEnd(38,40,5)
            if playerDown:
                player.move(0,2)
                player.imageStartEnd(44,46,5)
            if not playerUp and not playerDown:
                player.setImageIndex(38)
        elif (i.getY() <= player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() - 2 <= player.getX() + player.getWidth() <= i.getX() + 10: 
#-----Player Climbing-----
            bottom = False
            side_collision = True
            collision = True
            playerRight = False
            gravity = 0
            yVelocity = 0
            if playerUp:
                player.imageStartEnd(35,37,5)
                yVelocity = -2.5
            if playerDown:
                player.move(0,2)
                player.imageStartEnd(41,43,5)
            if not playerUp and not playerDown:
                player.setImageIndex(35)
        elif (i.getX() <= player.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 35  <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 15  <= i.getX() + i.getWidth()) and i.getY() - 2 <= player.getY() + player.getHeight() <= i.getY() + 10: 
#-----Player Walking-----
            if playerLeft:
                player.imageStartEnd(9,17,5)
            elif playerRight:
                player.imageStartEnd(0,8,5)
            collision = True
            bottom = False
            yVelocity = 0
            playerDown = False
            if jump:
                yVelocity = -3
            if defend:
                playerRight = False
                playerLeft = False
                if facingLeft:
                    player.setImageIndex(65)
                if facingRight:
                    player.setImageIndex(56)
#-----Player Attacks-----
            if attack:
                if health != 0:
                    player_count += 1
                    jump = False
                    playerRight = False
                    playerLeft = False
                    if weapon == 1:
                        if facingLeft:
                            if player_count == 1:
                                player.setImageIndex(22)
                            if player_count == 10:
                                player.setImageIndex(23)
                            if player_count == 20:
                                player.setImageIndex(24)
                            if player_count == 30:
                               player.setImageIndex(25)
                            if player_count == 40:
                                player.setImageIndex(26)
                                if player_range1.collision(enemy1):
                                    enemy1_health -= 10
                                player_count = 0
                                attack = False
                        if facingRight:
                            if player_count == 1:
                                player.setImageIndex(27)
                            if player_count == 10:
                                player.setImageIndex(28)
                            if player_count == 20:
                                player.setImageIndex(29)
                            if player_count == 30:
                               player.setImageIndex(30)
                            if player_count == 40:
                                player.setImageIndex(31)
                                if player_range2.collision(enemy1):
                                    enemy1_health -= 10
                                player_count = 0
                                attack = False
                    if weapon == 2:
                        if stamina > 0:
                            if facingLeft:
                                if player_count == 1:
                                    player.setImageIndex(77)
                                if player_count == 15:
                                    player.setImageIndex(78)
                                if player_count == 30:
                                    player.setImageIndex(79)
                                    player_count = 0
                                    attack = False
                                    arrow = Sprite(30,12,None,"arrow_left_00.png")
                                    arrow.xSpeed = -groundSpeed - 2
                                    arrow.setPosition(player.getX() - 30, player.getY() + (player.getWidth() / 2) - 5)
                                    arrows.append(arrow)
                                    all_sprites1.add(arrow)
                                    player_stamina -= 5
                                    stamina_count = 0
                                    stamina -= 1
                            if facingRight:
                                if player_count == 1:
                                    player.setImageIndex(74)
                                if player_count == 15:
                                    player.setImageIndex(75)
                                if player_count == 30:
                                    player.setImageIndex(76)
                                    player_count = 0
                                    attack = False
                                    arrow = Sprite(30,12,None,"arrow_right_00.png")
                                    arrow.xSpeed = groundSpeed + 2
                                    arrow.setPosition(player.getX() + player.getWidth(), player.getY() + (player.getWidth() / 2) - 5)
                                    arrows.append(arrow)
                                    all_sprites1.add(arrow)
                                    player_stamina -= 5
                                    stamina -= 1
                                    stamina_count = 0
                        else:
                            player_count = 0
                            attack = False
        elif (i.getX() <= player.getX() + 25 <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 15 <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 35 <= i.getX() + i.getWidth()) and i.getY() + i.getHeight() - 10 <= player.getY() <= i.getY() + i.getHeight() + 2: 
            playerUp = False
            gravity = 0
            yVelocity = 0
            bottom = True
            collision = True        
            if playerDown:
                player.move(0,2)
#-----Spike Code-----
    for i in spike:
        if player.collision(i):
            damage_counter += 1
            shield_count = 0
            spike_collision = True
            damage_check = True
            if player_shield > 0:
                if damage_counter == 1:
                        player_shield -= 10
                        shield -= 1
            else:
                if health != 0:
                    if damage_counter == 1:
                        player_health -= 10
                        health -= 1
            if (i.getY() <= player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() + i.getWidth() - 10 <= player.getX() <= i.getX() + i.getWidth() + 2: 
                playerLeft = False
                player.move(10,0)
            elif (i.getY() <= player.getY() + 25 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 15 <= i.getY() + i.getHeight() or i.getY() <= player.getY() + 35 <= i.getY() + i.getHeight()) and i.getX() - 2 <= player.getX() + player.getWidth() <= i.getX() + 10: 
                playerRight = False
            elif (i.getX() <= player.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= player.getY() + player.getHeight() <= i.getY() + 10:
                yVelocity = -2
#-----Enemies Code-----
    for enemies in enemy:
        if health == 0:
            if player.getX() < enemies.getX():
                enemies.setImageIndex(0)
            if player.getX() > enemies.getX():
                enemies.setImageIndex(27)  
#-----Enemy Boundaries-----
    for i in ground:
        if (i.getX() <= enemy1.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= enemy1.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= enemy1.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= enemy1.getY() + player.getHeight() <= i.getY() + 10: 
            enemy_attack = True
    for walls in wall:
        if enemy1.collision(walls):
            if (walls.getY() <= enemy1.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy1.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy1.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= enemy1.getX() + enemy1.getWidth() <= walls.getX() + 10:
                enemy1_stop_left = True
            if (walls.getY() <= enemy1.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy1.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy1.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= enemy1.getX() <= walls.getX() + walls.getWidth() + 2: 
                enemy1_stop_right = True
    for c_walls in c_wall:
        if enemy1.collision(c_walls):
            if (c_walls.getY() <= enemy1.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy1.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy1.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= enemy1.getX() + enemy1.getWidth() <= c_walls.getX() + 10: 
                enemy1_stop_left = True
            if (c_walls.getY() <= enemy1.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy1.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy1.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= enemy1.getX() <= c_walls.getX() + c_walls.getWidth() + 2: 
                enemy1_stop_right = True
    for spikes in spike:
        if enemy1.collision(spikes):
            if (spikes.getY() <= enemy1.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy1.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy1.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= enemy1.getX() + enemy1.getWidth() <= spikes.getX() + 10: 
                enemy1_stop_left = True
            if (spikes.getY() <= enemy1.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy1.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy1.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= enemy1.getX() <= spikes.getX() + spikes.getWidth() + 2: 
                enemy1_stop_right = True
#-----Enemy Ranges-----
    enemy1_range1.setPosition(enemy1.getX() - 50, enemy1.getY())
    enemy1_range2.setPosition(enemy1.getX() + enemy1.getWidth(), enemy1.getY())
    enemy1_range3.setPosition(enemy1.getX() - 160,enemy1.getY() - enemy1.getWidth() - 30)
    enemy1_range4.setPosition(enemy1.getX() + 110, enemy1.getY() - enemy1.getWidth() - 30)
    enemy1_range5.setPosition(enemy1.getX() - 425, enemy1.getY() - 410)
#-----Player Boundaries-----
    if enemy1_health > 0:
        if enemy1.getY() <= player.getY() + 25 <= enemy1.getY() + enemy1.getHeight() and enemy1.getX() + enemy1.getWidth() - 10 <= player.getX() <= enemy1.getX() + enemy1.getWidth() + 2:
            playerLeft = False
        elif enemy1.getY() <= player.getY() + 25 <= enemy1.getY() + enemy1.getHeight() and enemy1.getX() - 2 <= player.getX() + player.getWidth() <= enemy1.getX() + 10:
            playerRight = False
#-----Enemy Death Animation-----
    if enemy1_health <= 0:
        enemy1_health = 0
    if enemy1_health == 0:
        enemy1_death_ani += 1
        if enemy_facing_left:
            enemy_death_left(enemy1_death_ani,enemy1,all_sprites1)
        elif enemy_facing_right:
            enemy_death_right(enemy1_death_ani,enemy1,all_sprites1)
#-----Enemy Attacks-----
    if enemy1_health > 0 and health != 0:
        if enemy_attack:
            enemy1_count += 1
            if not player.collision(enemy1_range3) and not player.collision(enemy1_range4) and not player.collision(enemy1_range1) and not player.collision(enemy1_range2):
                if player.getX() < enemy1.getX():
                    enemy_facing_left = True
                    enemy_facing_right = False
                    enemy_shoot_left(enemy1_count,enemy1,enemy_arrows,all_sprites1)
                if player.getX() > enemy1.getX():
                    enemy_facing_left = False
                    enemy_facing_right = True
                    enemy_shoot_right(enemy1_count,enemy1,enemy_arrows,all_sprites1)
            elif player.collision(enemy1_range3) or player.collision(enemy1_range4):
                if player.collision(enemy1_range3):
                    enemy_facing_left = True
                    enemy_facing_right = False
                    if not enemy1_stop_right:
                        enemy1.move(-3,0)
                    enemy1.imageStartEnd(24,26,10)
                if player.collision(enemy1_range4):
                    enemy_facing_left = False
                    enemy_facing_right = True
                    if not enemy1_stop_left:
                        enemy1.move(3,0)
                    enemy1.imageStartEnd(27,29,10)
                enemy1_count = 0
            elif player.collision(enemy1_range1):
                enemy_attack_right(enemy1_count,enemy1)
                if enemy1_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0                      
            elif player.collision(enemy1_range2):
                enemy_attack_left(enemy1_count,enemy1)
                if enemy1_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0          
            if enemy1_count == 90:
                enemy1_count = 0
#-----Enemy Boundaries-----
    for i in ground:
        if (i.getX() <= enemy2.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= enemy2.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= enemy2.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= enemy2.getY() + player.getHeight() <= i.getY() + 10: 
            enemy_attack = True
    for walls in wall:
        if enemy2.collision(walls):
            if (walls.getY() <= enemy2.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy2.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy2.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= enemy2.getX() + enemy2.getWidth() <= walls.getX() + 10: 
                enemy2_stop_left = True
            if (walls.getY() <= enemy2.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy2.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy2.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= enemy2.getX() <= walls.getX() + walls.getWidth() + 2: 
                enemy2_stop_right = True
    for c_walls in c_wall:
        if enemy2.collision(c_walls):
            if (c_walls.getY() <= enemy2.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy2.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy2.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= enemy2.getX() + enemy2.getWidth() <= c_walls.getX() + 10: 
                enemy2_stop_left = True
            if (c_walls.getY() <= enemy2.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy2.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy2.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= enemy2.getX() <= c_walls.getX() + c_walls.getWidth() + 2: 
                enemy2_stop_right = True
    for spikes in spike:
        if enemy2.collision(spikes):
            if (spikes.getY() <= enemy2.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy2.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy2.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= enemy2.getX() + enemy2.getWidth() <= spikes.getX() + 10: 
                enemy2_stop_left = True
            if (spikes.getY() <= enemy2.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy2.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy2.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= enemy2.getX() <= spikes.getX() + spikes.getWidth() + 2: 
                enemy2_stop_right = True
#-----Enemy Ranges-----
    enemy2_range1.setPosition(enemy2.getX() - 50, enemy2.getY())
    enemy2_range2.setPosition(enemy2.getX() + enemy2.getWidth(), enemy2.getY())
    enemy2_range3.setPosition(enemy2.getX() - 160,enemy2.getY() - enemy2.getWidth() - 30)
    enemy2_range4.setPosition(enemy2.getX() + 110, enemy2.getY() - enemy2.getWidth() - 30)
    enemy2_range5.setPosition(enemy2.getX() - 425, enemy2.getY() - 410)
#-----Player Boundaries-----
    if enemy2_health > 0:
        if enemy2.getY() <= player.getY() + 25 <= enemy2.getY() + enemy2.getHeight() and enemy2.getX() + enemy2.getWidth() - 10 <= player.getX() <= enemy2.getX() + enemy2.getWidth() + 2:
            playerLeft = False
        elif enemy2.getY() <= player.getY() + 25 <= enemy2.getY() + enemy2.getHeight() and enemy2.getX() - 2 <= player.getX() + player.getWidth() <= enemy2.getX() + 10:
            playerRight = False
#-----Enemy Death Animation-----
    if enemy2_health <= 0:
        enemy2_health = 0
    if enemy2_health == 0:
        enemy2_death_ani += 1
        if enemy_facing_left:
            enemy_death_left(enemy2_death_ani,enemy2,all_sprites1)
        elif enemy_facing_right:
            enemy_death_right(enemy2_death_ani,enemy2,all_sprites1)
#-----Enemy Attacks-----
    if enemy2_health > 0 and health != 0:
        if enemy_attack:
            enemy2_count += 1
            if not player.collision(enemy2_range3) and not player.collision(enemy2_range4) and not player.collision(enemy2_range1) and not player.collision(enemy2_range2):
                if player.getX() < enemy2.getX():
                    enemy_facing_left = True
                    enemy_facing_right = False
                    enemy_shoot_left(enemy2_count,enemy2,enemy_arrows,all_sprites1)
                if player.getX() > enemy2.getX():
                    enemy_facing_left = False
                    enemy_facing_right = True
                    enemy_shoot_right(enemy2_count,enemy2,enemy_arrows,all_sprites1)
            elif player.collision(enemy2_range3) or player.collision(enemy2_range4):
                if player.collision(enemy2_range3):
                    enemy_facing_left = True
                    enemy_facing_right = False
                    if not enemy2_stop_right:
                        enemy2.move(-3,0)
                    enemy2.imageStartEnd(24,26,10)
                if player.collision(enemy2_range4):
                    enemy_facing_left = False
                    enemy_facing_right = True
                    if not enemy2_stop_left:
                        enemy2.move(3,0)
                    enemy2.imageStartEnd(27,29,10)
                enemy2_count = 0
            elif player.collision(enemy2_range1):
                enemy_attack_right(enemy2_count,enemy2)
                if enemy2_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0                      
            elif player.collision(enemy2_range2):
                enemy_attack_left(enemy2_count,enemy2)
                if enemy2_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0          
            if enemy2_count == 90:
                enemy2_count = 0
#-----Enemy Boundaries
    for i in ground:
        if (i.getX() <= enemy3.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= enemy3.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= enemy3.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= enemy3.getY() + player.getHeight() <= i.getY() + 10:
            enemy_attack = True
    for walls in wall:
        if enemy3.collision(walls):
            if (walls.getY() <= enemy3.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy3.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy3.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= enemy3.getX() + enemy3.getWidth() <= walls.getX() + 10: 
                enemy3_stop_left = True
            if (walls.getY() <= enemy3.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy3.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy3.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= enemy3.getX() <= walls.getX() + walls.getWidth() + 2: 
                enemy3_stop_right = True
    for c_walls in c_wall:
        if enemy3.collision(c_walls):
            if (c_walls.getY() <= enemy3.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy3.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy3.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= enemy3.getX() + enemy3.getWidth() <= c_walls.getX() + 10: 
                enemy3_stop_left = True
            if (c_walls.getY() <= enemy3.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy3.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy3.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= enemy3.getX() <= c_walls.getX() + c_walls.getWidth() + 2: 
                enemy3_stop_right = True
    for spikes in spike:
        if enemy3.collision(spikes):
            if (spikes.getY() <= enemy3.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy3.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy3.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= enemy3.getX() + enemy3.getWidth() <= spikes.getX() + 10: 
                enemy3_stop_left = True
            if (spikes.getY() <= enemy3.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy3.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy3.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= enemy3.getX() <= spikes.getX() + spikes.getWidth() + 2: 
                enemy3_stop_right = True
#-----Enemy Ranges-----
    enemy3_range1.setPosition(enemy3.getX() - 50, enemy3.getY())
    enemy3_range2.setPosition(enemy3.getX() + enemy3.getWidth(), enemy3.getY())
    enemy3_range3.setPosition(enemy3.getX() - 160,enemy3.getY() - enemy3.getWidth() - 30)
    enemy3_range4.setPosition(enemy3.getX() + 110, enemy3.getY() - enemy3.getWidth() - 30)
    enemy3_range5.setPosition(enemy3.getX() - 425, enemy3.getY() - 410)
#-----Player Boundaries-----
    if enemy3_health > 0:
        if enemy3.getY() <= player.getY() + 25 <= enemy3.getY() + enemy3.getHeight() and enemy3.getX() + enemy3.getWidth() - 10 <= player.getX() <= enemy3.getX() + enemy3.getWidth() + 2:
            playerLeft = False
        elif enemy3.getY() <= player.getY() + 25 <= enemy3.getY() + enemy3.getHeight() and enemy3.getX() - 2 <= player.getX() + player.getWidth() <= enemy3.getX() + 10:
            playerRight = False
#-----Enemy Death Animation-----
    if enemy3_health <= 0:
        enemy3_health = 0
    if enemy3_health == 0:
        enemy3_death_ani += 1
        if enemy_facing_left:
            enemy_death_left(enemy3_death_ani,enemy3,all_sprites1)
        elif enemy_facing_right:
            enemy_death_right(enemy3_death_ani,enemy3,all_sprites1)
#-----Enemy Attacks-----
    if enemy3_health > 0 and health != 0:
        if enemy_attack:
            enemy3_count += 1
            if not player.collision(enemy3_range3) and not player.collision(enemy3_range4) and not player.collision(enemy3_range1) and not player.collision(enemy3_range2):
                if player.getX() < enemy3.getX():
                    enemy_facing_left = True
                    enemy_facing_right = False
                    enemy_shoot_left(enemy3_count,enemy3,enemy_arrows,all_sprites1)
                if player.getX() > enemy3.getX():
                    enemy_facing_left = False
                    enemy_facing_right = True
                    enemy_shoot_right(enemy3_count,enemy3,enemy_arrows,all_sprites1)
            elif player.collision(enemy3_range3) or player.collision(enemy3_range4):
                if player.collision(enemy3_range3):
                    enemy_facing_left = True
                    enemy_facing_right = False
                    if not enemy3_stop_right:
                        enemy3.move(-3,0)
                    enemy3.imageStartEnd(24,26,10)
                if player.collision(enemy3_range4):
                    enemy_facing_left = False
                    enemy_facing_right = True
                    if not enemy3_stop_left:
                        enemy3.move(3,0)
                    enemy3.imageStartEnd(27,29,10)
                enemy3_count = 0
            elif player.collision(enemy3_range1):
                enemy_attack_right(enemy3_count,enemy3)
                if enemy3_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0                      
            elif player.collision(enemy3_range2):
                enemy_attack_left(enemy3_count,enemy3)
                if enemy3_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0          
            if enemy3_count == 90:
                enemy3_count = 0
#-----Enemy Boundaries-----
    for i in ground:
        if (i.getX() <= enemy4.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= enemy4.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= enemy4.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= enemy4.getY() + player.getHeight() <= i.getY() + 10: 
            enemy_attack = True
    for walls in wall:
        if enemy4.collision(walls):
            if (walls.getY() <= enemy4.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy4.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy4.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= enemy4.getX() + enemy4.getWidth() <= walls.getX() + 10: 
                enemy4_stop_left = True
            if (walls.getY() <= enemy4.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy4.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy4.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= enemy4.getX() <= walls.getX() + walls.getWidth() + 2: 
                enemy4_stop_right = True
    for c_walls in c_wall:
        if enemy4.collision(c_walls):
            if (c_walls.getY() <= enemy4.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy4.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy4.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= enemy4.getX() + enemy4.getWidth() <= c_walls.getX() + 10: 
                enemy4_stop_left = True
            if (c_walls.getY() <= enemy4.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy4.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy4.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= enemy4.getX() <= c_walls.getX() + c_walls.getWidth() + 2: 
                enemy4_stop_right = True
    for spikes in spike:
        if enemy4.collision(spikes):
            if (spikes.getY() <= enemy4.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy4.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy4.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= enemy4.getX() + enemy4.getWidth() <= spikes.getX() + 10: 
                enemy4_stop_left = True
            if (spikes.getY() <= enemy4.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy4.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy4.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= enemy4.getX() <= spikes.getX() + spikes.getWidth() + 2: 
                enemy4_stop_right = True
#-----Enemy Ranges-----
    enemy4_range1.setPosition(enemy4.getX() - 50, enemy4.getY())
    enemy4_range2.setPosition(enemy4.getX() + enemy4.getWidth(), enemy4.getY())
    enemy4_range3.setPosition(enemy4.getX() - 160,enemy4.getY() - enemy4.getWidth() - 30)
    enemy4_range4.setPosition(enemy4.getX() + 110, enemy4.getY() - enemy4.getWidth() - 30)
    enemy4_range5.setPosition(enemy4.getX() - 425, enemy4.getY() - 410)
#-----Player Boundaries-----
    if enemy4_health > 0:
        if enemy4.getY() <= player.getY() + 25 <= enemy4.getY() + enemy4.getHeight() and enemy4.getX() + enemy4.getWidth() - 10 <= player.getX() <= enemy4.getX() + enemy4.getWidth() + 2:
            playerLeft = False
        elif enemy4.getY() <= player.getY() + 25 <= enemy4.getY() + enemy4.getHeight() and enemy4.getX() - 2 <= player.getX() + player.getWidth() <= enemy4.getX() + 10:
            playerRight = False
#-----Enemy Death Animation-----
    if enemy4_health <= 0:
        enemy4_health = 0
    if enemy4_health == 0:
        enemy4_death_ani += 1
        if enemy_facing_left:
            enemy_death_left(enemy4_death_ani,enemy4,all_sprites1)
        elif enemy_facing_right:
            enemy_death_right(enemy4_death_ani,enemy4,all_sprites1)
#-----Enemy Attacks-----
    if enemy4_health > 0 and health != 0:
        if enemy_attack:
            enemy4_count += 1
            if not player.collision(enemy4_range3) and not player.collision(enemy4_range4) and not player.collision(enemy4_range1) and not player.collision(enemy4_range2):
                if player.getX() < enemy4.getX():
                    enemy_facing_left = True
                    enemy_facing_right = False
                    enemy_shoot_left(enemy4_count,enemy4,enemy_arrows,all_sprites1)
                if player.getX() > enemy4.getX():
                    enemy_facing_left = False
                    enemy_facing_right = True
                    enemy_shoot_right(enemy4_count,enemy4,enemy_arrows,all_sprites1)
            elif player.collision(enemy4_range3) or player.collision(enemy4_range4):
                if player.collision(enemy4_range3):
                    enemy_facing_left = True
                    enemy_facing_right = False
                    if not enemy4_stop_right:
                        enemy4.move(-3,0)
                    enemy4.imageStartEnd(24,26,10)
                if player.collision(enemy4_range4):
                    enemy_facing_left = False
                    enemy_facing_right = True
                    if not enemy4_stop_left:
                        enemy4.move(3,0)
                    enemy4.imageStartEnd(27,29,10)
                enemy4_count = 0
            elif player.collision(enemy4_range1):
                enemy_attack_right(enemy4_count,enemy4)
                if enemy4_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0                      
            elif player.collision(enemy4_range2):
                enemy_attack_left(enemy4_count,enemy4)
                if enemy4_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0          
            if enemy4_count == 90:
                enemy4_count = 0
#-----Enemy Boundaries-----
    for i in ground:
        if (i.getX() <= enemy5.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= enemy5.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= enemy5.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= enemy5.getY() + player.getHeight() <= i.getY() + 10: 
            enemy_attack = True
    for walls in wall:
        if enemy5.collision(walls):
            if (walls.getY() <= enemy5.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy5.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy5.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= enemy5.getX() + enemy5.getWidth() <= walls.getX() + 10: 
                enemy5_stop_left = True
            if (walls.getY() <= enemy5.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy5.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy5.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= enemy5.getX() <= walls.getX() + walls.getWidth() + 2: 
                enemy5_stop_right = True
    for c_walls in c_wall:
        if enemy5.collision(c_walls):
            if (c_walls.getY() <= enemy5.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy5.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy5.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= enemy5.getX() + enemy5.getWidth() <= c_walls.getX() + 10: 
                enemy5_stop_left = True
            if (c_walls.getY() <= enemy5.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy5.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy5.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= enemy5.getX() <= c_walls.getX() + c_walls.getWidth() + 2:
                enemy5_stop_right = True
    for spikes in spike:
        if enemy5.collision(spikes):
            if (spikes.getY() <= enemy5.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy5.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy5.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= enemy5.getX() + enemy5.getWidth() <= spikes.getX() + 10: 
                enemy5_stop_left = True
            if (spikes.getY() <= enemy5.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy5.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy5.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= enemy5.getX() <= spikes.getX() + spikes.getWidth() + 2: 
                enemy5_stop_right = True
#-----Enemy Ranges-----
    enemy5_range1.setPosition(enemy5.getX() - 50, enemy5.getY())
    enemy5_range2.setPosition(enemy5.getX() + enemy5.getWidth(), enemy5.getY())
    enemy5_range3.setPosition(enemy5.getX() - 160,enemy5.getY() - enemy5.getWidth() - 30)
    enemy5_range4.setPosition(enemy5.getX() + 110, enemy5.getY() - enemy5.getWidth() - 30)
    enemy5_range5.setPosition(enemy5.getX() - 425, enemy5.getY() - 410)
#-----Player Boundaries-----
    if enemy5_health > 0:
        if enemy5.getY() <= player.getY() + 25 <= enemy5.getY() + enemy5.getHeight() and enemy5.getX() + enemy5.getWidth() - 10 <= player.getX() <= enemy5.getX() + enemy5.getWidth() + 2:
            playerLeft = False
        elif enemy5.getY() <= player.getY() + 25 <= enemy5.getY() + enemy5.getHeight() and enemy5.getX() - 2 <= player.getX() + player.getWidth() <= enemy5.getX() + 10:
            playerRight = False
#-----Enemy Death Animation-----
    if enemy5_health <= 0:
        enemy5_health = 0
    if enemy5_health == 0:
        enemy5_death_ani += 1
        if enemy_facing_left:
            enemy_death_left(enemy5_death_ani,enemy5,all_sprites1)
        elif enemy_facing_right:
            enemy_death_right(enemy5_death_ani,enemy5,all_sprites1)
#-----Enemy Attacks-----
    if enemy5_health > 0 and health != 0:
        if enemy_attack:
            enemy5_count += 1
            if not player.collision(enemy5_range3) and not player.collision(enemy5_range4) and not player.collision(enemy5_range1) and not player.collision(enemy5_range2):
                if player.getX() < enemy5.getX():
                    enemy_facing_left = True
                    enemy_facing_right = False
                    enemy_shoot_left(enemy5_count,enemy5,enemy_arrows,all_sprites1)
                if player.getX() > enemy5.getX():
                    enemy_facing_left = False
                    enemy_facing_right = True
                    enemy_shoot_right(enemy5_count,enemy5,enemy_arrows,all_sprites1)
            elif player.collision(enemy5_range3) or player.collision(enemy5_range4):
                if player.collision(enemy5_range3):
                    enemy_facing_left = True
                    enemy_facing_right = False
                    if not enemy5_stop_right:
                        enemy5.move(-3,0)
                    enemy5.imageStartEnd(24,26,10)
                if player.collision(enemy5_range4):
                    enemy_facing_left = False
                    enemy_facing_right = True
                    if not enemy5_stop_left:
                        enemy5.move(3,0)
                    enemy5.imageStartEnd(27,29,10)
                enemy5_count = 0
            elif player.collision(enemy5_range1):
                enemy_attack_right(enemy5_count,enemy5)
                if enemy5_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0                      
            elif player.collision(enemy5_range2):
                enemy_attack_left(enemy5_count,enemy5)
                if enemy5_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0          
            if enemy5_count == 90:
                enemy5_count = 0
#-----Enemy Boundaries-----
    for i in ground:
        if (i.getX() <= enemy6.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= enemy6.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= enemy6.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= enemy6.getY() + player.getHeight() <= i.getY() + 10: 
            enemy_attack = True
    for walls in wall:
        if enemy6.collision(walls):
            if (walls.getY() <= enemy6.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy6.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy6.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= enemy6.getX() + enemy6.getWidth() <= walls.getX() + 10: 
                enemy6_stop_left = True
            if (walls.getY() <= enemy6.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy6.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy6.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= enemy6.getX() <= walls.getX() + walls.getWidth() + 2: 
                enemy6_stop_right = True
    for c_walls in c_wall:
        if enemy6.collision(c_walls):
            if (c_walls.getY() <= enemy6.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy6.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy6.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= enemy6.getX() + enemy6.getWidth() <= c_walls.getX() + 10:
                enemy6_stop_left = True
            if (c_walls.getY() <= enemy6.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy6.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy6.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= enemy6.getX() <= c_walls.getX() + c_walls.getWidth() + 2: 
                enemy6_stop_right = True
    for spikes in spike:
        if enemy6.collision(spikes):
            if (spikes.getY() <= enemy6.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy6.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy6.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= enemy6.getX() + enemy6.getWidth() <= spikes.getX() + 10: 
                enemy6_stop_left = True
            if (spikes.getY() <= enemy6.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy6.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy6.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= enemy6.getX() <= spikes.getX() + spikes.getWidth() + 2: 
                enemy6_stop_right = True
#-----Enemy Ranges-----
    enemy6_range1.setPosition(enemy6.getX() - 50, enemy6.getY())
    enemy6_range2.setPosition(enemy6.getX() + enemy6.getWidth(), enemy6.getY())
    enemy6_range3.setPosition(enemy6.getX() - 160,enemy6.getY() - enemy6.getWidth() - 30)
    enemy6_range4.setPosition(enemy6.getX() + 110, enemy6.getY() - enemy6.getWidth() - 30)
    enemy6_range5.setPosition(enemy6.getX() - 425, enemy6.getY() - 410)
#-----Player Boundaries-----
    if enemy6_health > 0:
        if enemy6.getY() <= player.getY() + 25 <= enemy6.getY() + enemy6.getHeight() and enemy6.getX() + enemy6.getWidth() - 10 <= player.getX() <= enemy6.getX() + enemy6.getWidth() + 2:
            playerLeft = False
        elif enemy6.getY() <= player.getY() + 25 <= enemy6.getY() + enemy6.getHeight() and enemy6.getX() - 2 <= player.getX() + player.getWidth() <= enemy6.getX() + 10:
            playerRight = False
#-----Enemy Death Animation-----
    if enemy6_health <= 0:
        enemy6_health = 0
    if enemy6_health == 0:
        enemy6_death_ani += 1
        if enemy_facing_left:
            enemy_death_left(enemy6_death_ani,enemy6,all_sprites1)
        elif enemy_facing_right:
            enemy_death_right(enemy6_death_ani,enemy6,all_sprites1)
#-----Enemy Attacks-----
    if enemy6_health > 0 and health != 0:
        if enemy_attack:
            enemy6_count += 1
            if not player.collision(enemy6_range3) and not player.collision(enemy6_range4) and not player.collision(enemy6_range1) and not player.collision(enemy6_range2):
                if player.getX() < enemy6.getX():
                    enemy_facing_left = True
                    enemy_facing_right = False
                    enemy_shoot_left(enemy6_count,enemy6,enemy_arrows,all_sprites1)
                if player.getX() > enemy6.getX():
                    enemy_facing_left = False
                    enemy_facing_right = True
                    enemy_shoot_right(enemy6_count,enemy6,enemy_arrows,all_sprites1)
            elif player.collision(enemy6_range3) or player.collision(enemy6_range4):
                if player.collision(enemy6_range3):
                    enemy_facing_left = True
                    enemy_facing_right = False
                    if not enemy6_stop_right:
                        enemy6.move(-3,0)
                    enemy6.imageStartEnd(24,26,10)
                if player.collision(enemy6_range4):
                    enemy_facing_left = False
                    enemy_facing_right = True
                    if not enemy6_stop_left:
                        enemy6.move(3,0)
                    enemy6.imageStartEnd(27,29,10)
                enemy6_count = 0
            elif player.collision(enemy6_range1):
                enemy_attack_right(enemy6_count,enemy6)
                if enemy6_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0                      
            elif player.collision(enemy6_range2):
                enemy_attack_left(enemy6_count,enemy6)
                if enemy6_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0          
            if enemy6_count == 90:
                enemy6_count = 0
#-----Enemy Boundaries-----
    for i in ground:
        if (i.getX() <= enemy7.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= enemy7.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= enemy7.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= enemy7.getY() + player.getHeight() <= i.getY() + 10: 
            enemy_attack = True
    for walls in wall:
        if enemy7.collision(walls):
            if (walls.getY() <= enemy7.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy7.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy7.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= enemy7.getX() + enemy7.getWidth() <= walls.getX() + 10: 
                enemy7_stop_left = True
            if (walls.getY() <= enemy7.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy7.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy7.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= enemy7.getX() <= walls.getX() + walls.getWidth() + 2: 
                enemy7_stop_right = True
    for c_walls in c_wall:
        if enemy7.collision(c_walls):
            if (c_walls.getY() <= enemy7.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy7.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy7.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= enemy7.getX() + enemy7.getWidth() <= c_walls.getX() + 10: 
                enemy7_stop_left = True
            if (c_walls.getY() <= enemy7.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy7.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy7.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= enemy7.getX() <= c_walls.getX() + c_walls.getWidth() + 2: 
                enemy7_stop_right = True
    for spikes in spike:
        if enemy7.collision(spikes):
            if (spikes.getY() <= enemy7.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy7.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy7.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= enemy7.getX() + enemy7.getWidth() <= spikes.getX() + 10: 
                enemy7_stop_left = True
            if (spikes.getY() <= enemy7.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy7.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy7.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= enemy7.getX() <= spikes.getX() + spikes.getWidth() + 2: 
                enemy7_stop_right = True
#-----Enemy Ranges-----
    enemy7_range1.setPosition(enemy7.getX() - 50, enemy7.getY())
    enemy7_range2.setPosition(enemy7.getX() + enemy7.getWidth(), enemy7.getY())
    enemy7_range3.setPosition(enemy7.getX() - 160,enemy7.getY() - enemy7.getWidth() - 30)
    enemy7_range4.setPosition(enemy7.getX() + 110, enemy7.getY() - enemy7.getWidth() - 30)
    enemy7_range5.setPosition(enemy7.getX() - 425, enemy7.getY() - 410)
#-----Player Boundaries-----
    if enemy7_health > 0:
        if enemy7.getY() <= player.getY() + 25 <= enemy7.getY() + enemy7.getHeight() and enemy7.getX() + enemy7.getWidth() - 10 <= player.getX() <= enemy7.getX() + enemy7.getWidth() + 2:
            playerLeft = False
        elif enemy7.getY() <= player.getY() + 25 <= enemy7.getY() + enemy7.getHeight() and enemy7.getX() - 2 <= player.getX() + player.getWidth() <= enemy7.getX() + 10:
            playerRight = False
#-----Enemy Death Animation-----
    if enemy7_health <= 0:
        enemy7_health = 0
    if enemy7_health == 0:
        enemy7_death_ani += 1
        if enemy_facing_left:
            enemy_death_left(enemy7_death_ani,enemy7,all_sprites1)
        elif enemy_facing_right:
            enemy_death_right(enemy7_death_ani,enemy7,all_sprites1)
#-----Enemy Attacks-----
    if enemy7_health > 0 and health != 0:
        if enemy_attack:
            enemy7_count += 1
            if not player.collision(enemy7_range3) and not player.collision(enemy7_range4) and not player.collision(enemy7_range1) and not player.collision(enemy7_range2):
                if player.getX() < enemy7.getX():
                    enemy_facing_left = True
                    enemy_facing_right = False
                    enemy_shoot_left(enemy7_count,enemy7,enemy_arrows,all_sprites1)
                if player.getX() > enemy7.getX():
                    enemy_facing_left = False
                    enemy_facing_right = True
                    enemy_shoot_right(enemy7_count,enemy7,enemy_arrows,all_sprites1)
            elif player.collision(enemy7_range3) or player.collision(enemy7_range4):
                if player.collision(enemy7_range3):
                    enemy_facing_left = True
                    enemy_facing_right = False
                    if not enemy7_stop_right:
                        enemy7.move(-3,0)
                    enemy7.imageStartEnd(24,26,10)
                if player.collision(enemy7_range4):
                    enemy_facing_left = False
                    enemy_facing_right = True
                    if not enemy7_stop_left:
                        enemy7.move(3,0)
                    enemy7.imageStartEnd(27,29,10)
                enemy7_count = 0
            elif player.collision(enemy7_range1):
                enemy_attack_right(enemy7_count,enemy7)
                if enemy7_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0                      
            elif player.collision(enemy7_range2):
                enemy_attack_left(enemy7_count,enemy7)
                if enemy7_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0          
            if enemy7_count == 90:
                enemy7_count = 0
#-----Enemy Boundaries-----
    for i in ground:
        if (i.getX() <= enemy8.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= enemy8.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= enemy8.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= enemy8.getY() + player.getHeight() <= i.getY() + 10: 
            enemy_attack = True
    for walls in wall:
        if enemy8.collision(walls):
            if (walls.getY() <= enemy8.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy8.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy8.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() - 2 <= enemy8.getX() + enemy8.getWidth() <= walls.getX() + 10:
                enemy8_stop_left = True
            if (walls.getY() <= enemy8.getY() + 25 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy8.getY() + 15 <= walls.getY() + walls.getHeight() or walls.getY() <= enemy8.getY() + 35 <= walls.getY() + walls.getHeight()) and walls.getX() + walls.getWidth() - 10 <= enemy8.getX() <= walls.getX() + walls.getWidth() + 2:
                enemy8_stop_right = True
    for c_walls in c_wall:
        if enemy8.collision(c_walls):
            if (c_walls.getY() <= enemy8.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy8.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy8.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() - 2 <= enemy8.getX() + enemy8.getWidth() <= c_walls.getX() + 10: 
                enemy8_stop_left = True
            if (c_walls.getY() <= enemy8.getY() + 25 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy8.getY() + 15 <= c_walls.getY() + c_walls.getHeight() or c_walls.getY() <= enemy8.getY() + 35 <= c_walls.getY() + c_walls.getHeight()) and c_walls.getX() + c_walls.getWidth() - 10 <= enemy8.getX() <= c_walls.getX() + c_walls.getWidth() + 2: 
                enemy8_stop_right = True
    for spikes in spike:
        if enemy8.collision(spikes):
            if (spikes.getY() <= enemy8.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy8.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy8.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() - 2 <= enemy8.getX() + enemy8.getWidth() <= spikes.getX() + 10: 
                enemy8_stop_left = True
            if (spikes.getY() <= enemy8.getY() + 25 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy8.getY() + 15 <= spikes.getY() + spikes.getHeight() or spikes.getY() <= enemy8.getY() + 35 <= spikes.getY() + spikes.getHeight()) and spikes.getX() + spikes.getWidth() - 10 <= enemy8.getX() <= spikes.getX() + spikes.getWidth() + 2: 
                enemy8_stop_right = True
#-----Enemy Ranges-----
    enemy8_range1.setPosition(enemy8.getX() - 50, enemy8.getY())
    enemy8_range2.setPosition(enemy8.getX() + enemy8.getWidth(), enemy8.getY())
    enemy8_range3.setPosition(enemy8.getX() - 160,enemy8.getY() - enemy8.getWidth() - 30)
    enemy8_range4.setPosition(enemy8.getX() + 110, enemy8.getY() - enemy8.getWidth() - 30)
    enemy8_range5.setPosition(enemy8.getX() - 425, enemy8.getY() - 410)
#-----Player Boundaries-----
    if enemy8_health > 0:
        if enemy8.getY() <= player.getY() + 25 <= enemy8.getY() + enemy8.getHeight() and enemy8.getX() + enemy8.getWidth() - 10 <= player.getX() <= enemy8.getX() + enemy8.getWidth() + 2:
            playerLeft = False
        elif enemy8.getY() <= player.getY() + 25 <= enemy8.getY() + enemy8.getHeight() and enemy8.getX() - 2 <= player.getX() + player.getWidth() <= enemy8.getX() + 10:
            playerRight = False
#-----Enemy Death Animation-----
    if enemy8_health <= 0:
        enemy8_health = 0
    if enemy8_health == 0:
        enemy8_death_ani += 1
        if enemy_facing_left:
            enemy_death_left(enemy8_death_ani,enemy8,all_sprites1)
        elif enemy_facing_right:
            enemy_death_right(enemy8_death_ani,enemy8,all_sprites1)
#-----Enemy Attacks-----
    if enemy8_health > 0 and health != 0:
        if enemy_attack:
            enemy8_count += 1
            if not player.collision(enemy8_range3) and not player.collision(enemy8_range4) and not player.collision(enemy8_range1) and not player.collision(enemy8_range2):
                if player.getX() < enemy8.getX():
                    enemy_facing_left = True
                    enemy_facing_right = False
                    enemy_shoot_left(enemy8_count,enemy8,enemy_arrows,all_sprites1)
                if player.getX() > enemy8.getX():
                    enemy_facing_left = False
                    enemy_facing_right = True
                    enemy_shoot_right(enemy8_count,enemy8,enemy_arrows,all_sprites1)
            elif player.collision(enemy8_range3) or player.collision(enemy8_range4):
                if player.collision(enemy8_range3):
                    enemy_facing_left = True
                    enemy_facing_right = False
                    if not enemy8_stop_right:
                        enemy8.move(-3,0)
                    enemy8.imageStartEnd(24,26,10)
                if player.collision(enemy8_range4):
                    enemy_facing_left = False
                    enemy_facing_right = True
                    if not enemy8_stop_left:
                        enemy8.move(3,0)
                    enemy8.imageStartEnd(27,29,10)
                enemy8_count = 0
            elif player.collision(enemy8_range1):
                enemy_attack_right(enemy8_count,enemy8)
                if enemy8_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0                      
            elif player.collision(enemy8_range2):
                enemy_attack_left(enemy8_count,enemy8)
                if enemy8_count == 30:
                    damage_check = True
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0          
            if enemy8_count == 90:
                enemy8_count = 0
    if bottom:
        defend = False
#-----Character's Movement-----
    if playerRight and not bottom and not playerLeft:
        if not collision and not attack:
            player.imageStartEnd(18,19,10)
        facingRight = True
        facingLeft = False
        for bound in boundaries:
            bound.move(-groundSpeed,0)
        for back in background:
            back.move(-background_speed,0)
        for grounds in ground:
            grounds.move(-norm_speed,0)
        for walls in wall:
            walls.move(-norm_speed,0)
        for c_walls in c_wall:
            c_walls.move(-norm_speed,0)
        for spikes in spike:
            spikes.move(-norm_speed,0)
        for enemies in enemy:
            enemies.move(-norm_speed,0)
        for door in doors:
            door.move(-norm_speed,0)
    elif playerLeft and not bottom and not playerRight:
        if not collision and not attack:
            player.imageStartEnd(20,21,10)
        facingLeft = True
        facingRight = False
        for bound in boundaries:
            bound.move(groundSpeed,0)
        for back in background:
            back.move(background_speed,0)
        for grounds in ground:
            grounds.move(norm_speed,0)
        for walls in wall:
            walls.move(norm_speed,0)
        for c_walls in c_wall:
            c_walls.move(norm_speed,0)
        for spikes in spike:
            spikes.move(norm_speed,0)
        for enemies in enemy:
            enemies.move(norm_speed,0)
        for door in doors:
            door.move(norm_speed,0)
    if playerLeft and bottom and not playerRight:
        player.imageStartEnd(51,54,5)
        facingLeft = True
        facingRight = False
        for bound in boundaries:
            bound.move(background_speed,0)
        for back in background:
            back.move(background_speed,0)
        for grounds in ground:
            grounds.move(norm_speed,0)
        for walls in wall:
            walls.move(norm_speed,0)
        for c_walls in c_wall:
            c_walls.move(norm_speed,0)
        for spikes in spike:
            spikes.move(norm_speed,0)
        for enemies in enemy:
            enemies.move(norm_speed,0)
        for door in doors:
            door.move(norm_speed,0)
    elif playerRight and bottom and not playerLeft:
        player.imageStartEnd(47,50,5)
        facingRight = True
        facingLeft = False
        for bound in boundaries:
            bound.move(-groundSpeed,0)
        for back in background:
            back.move(-background_speed,0)
        for grounds in ground:
            grounds.move(-norm_speed,0)
        for walls in wall:
            walls.move(-norm_speed,0)
        for c_walls in c_wall:
            c_walls.move(-norm_speed,0)
        for spikes in spike:
            spikes.move(-norm_speed,0)
        for enemies in enemy:
            enemies.move(-norm_speed,0)
        for door in doors:
            door.move(-norm_speed,0)
    if player_health != 0:
        if not playerRight and not playerLeft and bottom and not damage_check:
            player.setImageIndex(55)
        elif not playerRight and not playerLeft and not bottom and not attack and not collision and not side_collision and not damage_check:
            player.setImageIndex(55)
        if not playerRight and not playerLeft and collision and not side_collision and not bottom and not attack and health != 0 and not damage_check:
            defend = True      
            if facingLeft:
                player.setImageIndex(65)
            if facingRight:
                player.setImageIndex(56)
    if not collision:
        attack = False
        defend = False
    if player_stamina == 0 and stamina == 0 and attack:
        if weapon == 2:
            attack = False
#-----Arrow Code-----
    for arrow in arrows:
        arrow.move(arrow.xSpeed,0)
        for grounds in ground:
            if arrow.collision(grounds):
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
        for walls in wall:
            if arrow.collision(walls):
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
        for c_walls in c_wall:
            if arrow.collision(c_walls):
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
        for spikes in spike:
            if arrow.collision(spikes):
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
        if enemy1_health > 0:
            if arrow.collision(enemy1):
                enemy1_health -= 10
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
        if enemy2_health > 0:
            if arrow.collision(enemy2):
                enemy2_health -= 10
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
        if enemy3_health > 0:
            if arrow.collision(enemy3):
                enemy3_health -= 10
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
        if enemy4_health > 0:
            if arrow.collision(enemy4):
                enemy4_health -= 10
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
        if enemy5_health > 0:
            if arrow.collision(enemy5):
                enemy5_health -= 10
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
        if enemy6_health > 0:
            if arrow.collision(enemy6):
                enemy6_health -= 10
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
        if enemy7_health > 0:
            if arrow.collision(enemy7):
                enemy7_health -= 10
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
        if enemy8_health > 0:
            if arrow.collision(enemy8):
                enemy8_health -= 10
                all_sprites1.remove(arrow)
                arrow.move(0, 0)
                arrow.setPosition(0, 0)
                arrows.remove(arrow)
#-----Enemy Arrow Code-----
    for e_arrows in enemy_arrows:
        e_arrows.move(e_arrows.xSpeed,0)
        for grounds in ground:
            if e_arrows.collision(grounds):
                all_sprites1.remove(e_arrows)
                enemy_arrows.remove(e_arrows)
                e_arrows.move(0,0)
                e_arrows.setPosition(0,0)
        for walls in wall:
            if e_arrows.collision(walls):
                all_sprites1.remove(e_arrows)
                enemy_arrows.remove(e_arrows)
                e_arrows.move(0,0)
                e_arrows.setPosition(0,0)
        for c_walls in c_wall:
            if e_arrows.collision(c_walls):
                all_sprites1.remove(e_arrows)
                enemy_arrows.remove(e_arrows)
                e_arrows.move(0,0)
                e_arrows.setPosition(0,0)
        for spikes in spike:
            if e_arrows.collision(spikes):
                all_sprites1.remove(e_arrows)
                enemy_arrows.remove(e_arrows)
                e_arrows.move(0,0)
                e_arrows.setPosition(0,0)        
        if e_arrows.collision(player) and health != 0:
            damage_check = True
            all_sprites1.remove(e_arrows)
            enemy_arrows.remove(e_arrows)
            e_arrows.move(0,0)
            e_arrows.setPosition(0,0)
            if player_shield > 0:
                player_shield -= 10
                shield -= 1
            else:
                if health != 0:
                    player_health -= 10
                    health -= 1
            shield_count = 0
#-----Player Gravity-----
    yVelocity += gravity
    player.move(0,yVelocity)
#-----Infinite Ground/Background-----
    if back1.getX() < -800:
        back1.setPosition(background_position, 0)
    if back2.getX() < -800:
        back2.setPosition(background_position, 0)
    if back1.getX() > 800:
        back1.setPosition(-background_position, 0)
    if back2.getX() > 800:
        back2.setPosition(-background_position, 0)
    if ground1.getX() < -800:
        ground1.setPosition(ground_position, 460)
    if ground2.getX() < -800:
        ground2.setPosition(ground_position, 460)
    if ground1.getX() > 800:
        ground1.setPosition(-ground_position, 460)
    if ground2.getX() > 800:
        ground2.setPosition(-ground_position, 460)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            parkour_enemies = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                playerRight = True
            if event.key == pygame.K_a:
                playerLeft = True
            if event.key == pygame.K_SPACE:
                jump = True
            if event.key == pygame.K_w:
                playerUp = True
            elif event.key == pygame.K_s:
                playerDown = True
            if event.key == pygame.K_1:
                weapon = 1
            if event.key == pygame.K_2:
                weapon = 2
            if event.key == pygame.K_o:
                enter = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                playerRight = False
            if event.key == pygame.K_a:
                playerLeft = False
            if event.key == pygame.K_SPACE:
                jump = False    
            if event.key == pygame.K_w:
                playerUp = False
            elif event.key == pygame.K_s:
                playerDown = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            attack = True
#-----Lists-----
maces = []
chains = []
o_chains = []
chained = []
arrows = []
#-----Sprites-----
boss = Sprite(100,100,None, "mace_knight_right_idle.png") 
boss.addImage("mace_knight_left_idle.png") 
boss.addImage("boss_walking_right_00.png") 
boss.addImage("boss_walking_right_01.png") 
boss.addImage("boss_walking_right_02.png") 
boss.addImage("boss_walking_left_00.png")
boss.addImage("boss_walking_left_01.png") 
boss.addImage("boss_walking_left_02.png") 
boss.addImage("boss_attack_left_00.png") 
boss.addImage("boss_attack_left_01.png") 
boss.addImage("boss_attack_left_02.png") 
boss.addImage("boss_attack_left_03.png") 
boss.addImage("boss_attack_right_00.png") 
boss.addImage("boss_attack_right_01.png") 
boss.addImage("boss_attack_right_02.png") 
boss.addImage("boss_attack_right_03.png") 
boss.addImage("mace_knight_idle.png")
boss.addImage("boss_death_animation_00.png") 
boss.addImage("boss_death_animation_01.png") 
boss.addImage("boss_death_animation_02.png") 
boss.addImage("boss_death_animation_03.png")
boss.addImage("boss_death_animation_04.png") 
boss.addImage("boss_death_animation_05.png") 
boss.addImage("boss_death_animation_06.png") 
boss.setPosition(300,360)
#-----FPS-----
Clock = pygame.time.Clock()
#-----Variables-----
t_yVelocity = 0
boss_count1 = 0
boss_death_animation = 0
mace_attack_count = 0
mace_stop = 0
mace_speed = 0
chain_position = 15
winner_text = 0
chain_position1 = 0
chain_appearance = 0
chain_appearance1 = 0
damage_count = 0
damage_count1 = 0
damage_count2 = 0
damage_check_count = 0
chain_distance = 10
chain_distance1 = 10
chain_attack_count = 0
mace_attempts = 0
boss_fighting_animation = 0
boss_death_animation = 0
player_win_count = 0
chain_speed = 0
chain_count = 0
weapon = 1
shield = 10
stamina = 10
player_shield = 100
player_stamina = 100
boss_health = 625
#-----Booleans-----
boss_facing_left = False
trophy_up = False
boss_facing_right = False
boss_battle_start = False
mace_rebound = False
mace_reattack = False
chain_appeared = False
chain_rebound = False
boss_range_collision = False
mace_away = False
chain_away = False
not_mace = False
attack = False
damage_check = False
winner = False
a_collision = False
#-----Sprites-----
boss_range1 = Sprite(50,100,[255,0,0])
boss_range2 = Sprite(50,100,[255,0,0]) 
boss_range3 = Sprite(75,100,[0,0,255]) 
boss_range4 = Sprite(75,100,[0,0,255]) 
boss_range5 = Sprite(100,100,[0,255,0])
boss_range6 = Sprite(100,100,[0,255,0]) 
boss_range7 = Sprite(50,100,[255,0,0]) 
boss_range8 = Sprite(50,100,[255,0,0]) 
boss_body = Sprite(50,75,[0,255,0])
player.setPosition(0,410)
ground1.setPosition(0, 460)
bound7.setPosition(-300,0)
bound8.setPosition(800,0)
all_sprites3.add(back3,ground1,boss,player)
if boss_battle:
    print("""
Attack the boss to start the battle

Good Luck!!!""")
while boss_battle:
    Clock.tick(60)
#-----Ranges-----
    player_range1.setPosition(player.getX() - 30, player.getY())
    player_range2.setPosition(player.getX() + player.getWidth(),player.getY())
    if boss_health != 0:
        boss_range1.setPosition(boss.getX() - 25,boss.getY())
        boss_range2.setPosition(boss.getX() + boss.getWidth() - 25, boss.getY())
        boss_range3.setPosition(boss.getX() - 100,boss.getY())
        boss_range4.setPosition(boss.getX() + boss.getWidth() + 25,boss.getY())
        boss_range5.setPosition(boss.getX() - 200,boss.getY())
        boss_range6.setPosition(boss.getX() + boss.getWidth() + 100,boss.getY())
        boss_range7.setPosition(boss.getX() - 250,boss.getY())
        boss_range8.setPosition(boss.getX() + boss.getWidth() + 200,boss.getY())
        boss_body.setPosition(boss.getX() + 20, boss.getY() + 25)
#-----Variables-----
    if health != 0:
        gravity = 0.095
    else:
        gravity = 0
        yVelocity = 0
#-----Count-----
    shield_count += 1
    stamina_count += 1
    screen.fill([0, 0, 0])
    all_sprites3.draw(screen)
    pygame.draw.rect(screen,[255,0,0],[27,10,player_health,15])
    pygame.draw.rect(screen,[211,211,211],[27,25,player_shield,15])
    pygame.draw.rect(screen,[0,0,255],[27,43,player_stamina,15])
    all_sprites2.draw(screen)
    if boss_health > 0:
        pygame.draw.rect(screen,[0,0,0],[150,30,625,40])
        pygame.draw.rect(screen,[255,0,0],[150,30,boss_health,40])
    add_text(str(health) + " / 10",[57,10],24,[255,255,255])
    add_text(str(shield) + " / 10",[57,27],24,[255,0,0])
    add_text(str(stamina) + " / 10",[57,45],23,[255,255,255])
    pygame.display.update()
    collision = False
    defend = False
    bottom = False
    side_collision = False
    enemy1_stop_left = False
    enemy1_stop_right = False
    boss_range_collision = False
    mace_reattack = True
    a_collision = False
#-----Player Stats-----
    if player_health <= 0:
        player_health = 0
        health = 0
    if player_stamina <= 0:
        player_stamina = 0
        stamina = 0
    if player_shield <= 0:
        player_shield = 0
        shield = 0
    if player_health >= 100:
        player_health = 100
        health = 10
    if player_stamina >= 100:
        player_stamina = 100
        stamina = 10
    if player_shield >= 100:
        player_shield = 100
        shield = 10
    if health != 0:
        if stamina_count >= 300:
            if stamina != 10:
                player_stamina += 10
                stamina += 1
            stamina_count = 120
        if shield_count >= 300:
            if shield != 10:
                player_shield += 10
                shield += 1
            shield_count = 120
    if not attack:
        player_count = 0
#-----Player Boundaries-----
    if player.collision(bound3):
        playerLeft = False
    elif player.collision(bound4):
        playerRight = False
    if player.getX() + (player.getWidth() / 2) > boss.getX() + (boss.getWidth() / 2):
        boss_facing_right = True
        boss_facing_left = False
        if not boss_battle_start:
            boss.setImageIndex(0)
    elif player.getX() + (player.getWidth() / 2) <= boss.getX() + (boss.getWidth() / 2):
        boss_facing_left = True
        boss_facing_right = False
        if not boss_battle_start:
            boss.setImageIndex(1)
#-----Player Boundaries-----
    if boss_health > 0:
        if boss.getY() <= player.getY() - 10 <= boss.getY() + boss.getHeight() and boss.getX() + boss.getWidth() - 20 <= player.getX() <= boss.getX() + boss.getWidth() - 10:
            playerLeft = False
        elif boss.getY() <= player.getY() - 10  <= boss.getY() + boss.getHeight() and boss.getX() + 10 <= player.getX() + player.getWidth() <= boss.getX() + 20:
            playerRight = False
    if (boss.collision(player_range1) or boss.collision(player_range2)) and attack and not boss_battle_start:
        boss_battle_start = True
    if boss_health < 0:
        boss_health = 0
#-----Boss Death Animation-----
    if boss_health == 0:
        boss_death_animation += 1
        if boss_death_animation == 1:
            boss.setImageIndex(17)
        if boss_death_animation == 15:
            boss.setImageIndex(18)
        if boss_death_animation == 30:
            boss.setImageIndex(19)
        if boss_death_animation == 45:
            boss.setImageIndex(20)
        if boss_death_animation == 60:
            boss.setImageIndex(21)
        if boss_death_animation == 75:
            boss.setImageIndex(22)
        if boss_death_animation == 90:
            boss.setImageIndex(23)
        if boss_death_animation == 105:
            all_sprites3.remove(boss)
            trophy = Sprite(50,50,None,"trophy_texture_01.png")
            trophy.setPosition(boss.getX(), boss.getY())
            all_sprites3.add(trophy)
#-----Boss Code-----
    if health == 0:
        boss.setImageIndex(16)
    if boss_health != 0 and health != 0:
        if boss_battle_start:
            if player.collision(boss_range1) and not player.collision(boss_range3) and not mace_away and not chain_away:
                boss_fighting_animation += 1
                if boss_fighting_animation == 1:
                    boss.setImageIndex(8)
                if boss_fighting_animation == 5:
                    boss.setImageIndex(9)
                if boss_fighting_animation == 10:
                    boss.setImageIndex(10)
                if boss_fighting_animation == 15:
                    boss.setImageIndex(11)
                    if player_shield > 0:
                        player_shield -= 30
                        shield -= 3
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0
                    damage_check = True
                if boss_fighting_animation == 20:
                    boss.setImageIndex(1)
                if boss_fighting_animation == 45:
                    boss_fighting_animation = 0
                not_mace = True
            elif player.collision(boss_range2) and not player.collision(boss_range4) and not mace_away and not chain_away:
                boss_fighting_animation += 1
                if boss_fighting_animation == 1:
                    boss.setImageIndex(12)
                if boss_fighting_animation == 5:
                    boss.setImageIndex(13)
                if boss_fighting_animation == 10:
                    boss.setImageIndex(14)
                if boss_fighting_animation == 15:
                    boss.setImageIndex(15)
                    if player_shield > 0:
                        player_shield -= 30
                        shield -= 3
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0
                    damage_check = True
                if boss_fighting_animation == 20:
                    boss.setImageIndex(0)
                if boss_fighting_animation == 45:
                    boss_fighting_animation = 0
                not_mace = True
            elif not player.collision(boss_range1) or not player.collision(boss_range2) and not mace_away and not chain_away:
                boss_fighting_animation = 0
            if player.collision(boss_range3) and not player.collision(boss_range5) and not mace_away and not chain_away:
                boss.move(-3,0)
                boss.imageStartEnd(5,7,5)
                not_mace = True
            elif player.collision(boss_range4) and not player.collision(boss_range6) and not mace_away and not chain_away:
                boss.move(3,0)
                boss.imageStartEnd(2,4,5)
                not_mace = True
            if player.collision(boss_range5) and not mace_away:
                chain_attack_count += 1
                if boss_facing_left:
                    if chain_attack_count < 0:
                        boss.move(-2,0)
                        boss.imageStartEnd(5,7,5)
                    if chain_attack_count == 1:
                        chain = Sprite(20,20,None, "chain_texture_00.png")
                        chain.setPosition(boss_body.getX(), boss_body.getY() + 40)
                        chain_speed = -5
                        chain.xSpeed = chain_speed
                        chained.append(chain)
                        all_sprites3.add(chain)
                        boss.setImageIndex(1)
                        chain_away = True
            if player.collision(boss_range6) and not mace_away:
                chain_attack_count += 1
                if boss_facing_right:
                    if chain_attack_count < 0:
                        boss.move(2,0)
                        boss.imageStartEnd(2,4,5)
                    if chain_attack_count == 1:
                        chain = Sprite(20,20,None, "chain_texture_00.png")
                        chain.setPosition(boss_body.getX() + boss_body.getWidth() , boss_body.getY() + 40)
                        chain_speed = 5
                        chain.xSpeed = chain_speed
                        chained.append(chain)
                        all_sprites3.add(chain)
                        boss.setImageIndex(0)
                        chain_away = True
            if mace_reattack and not player.collision(boss_range1) and not player.collision(boss_range2) and not player.collision(boss_range3) and not player.collision(boss_range4) and not player.collision(boss_range5) and not player.collision(boss_range6) and not chain_away:
                mace_attack_count += 1
                if boss_facing_left:
                    if mace_attack_count == 1:
                        mace = Sprite(36,36,None,"mace_texture_left.png")
                        mace.setPosition(boss_body.getX() , boss_body.getY() + 25)
                        mace_speed = -5
                        mace.xSpeed = mace_speed            
                        maces.append(mace)
                        all_sprites3.add(mace)
                        boss.setImageIndex(1)
                        damage_chack1 = 0
                        mace_reattack = False
                        mace_away = True
                    if mace_attack_count >= 20 and mace_attack_count <= 80:
                        boss.move(-2,0)
                        boss.imageStartEnd(5,7,5)
                if boss_facing_right:
                    if mace_attack_count == 1:
                        mace = Sprite(36,36,None,"mace_texture_right.png")
                        mace.setPosition(boss_body.getX() + boss_body.getWidth(), boss_body.getY() + 25)
                        mace_speed = 5
                        mace.xSpeed = mace_speed
                        maces.append(mace)
                        all_sprites3.add(mace)
                        damage_check1 = 0
                        boss.setImageIndex(0)
                        mace_reattack = False
                        mace_away = True
                    if mace_attack_count >= 20 and mace_attack_count <= 80:
                        boss.move(2,0)
                        boss.imageStartEnd(2,4,5)
#-----Player Code-----
    for i in ground:
        if (i.getX() <= player.getX() + 25  <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 15  <= i.getX() + i.getWidth() or i.getX() <= player.getX() + 35  <= i.getX() + i.getWidth()) and i.getY() - 2 <= player.getY() + player.getHeight() <= i.getY() + 10: 
            if playerLeft:
                player.imageStartEnd(9,17,5)
                if not attack:
                    player_count = 0
            elif playerRight:
                player.imageStartEnd(0,8,5)
                if not attack:
                    player_count = 0
            collision = True
            bottom = False
            yVelocity = 0
            playerDown = False
            if jump:
                yVelocity = -3
                if not attack:
                    player_count = 0
            if defend:
                if facingLeft:
                    player.setImageIndex(65)
                if facingRight:
                    player.setImageIndex(56)
                if not attack:
                    player_count = 0
            if attack and not winner:
                player_count += 1
                jump = False
                playerRight = False
                playerLeft = False
                if weapon == 1:
                    if facingLeft:
                        if player_count == 1:
                            player.setImageIndex(22)
                        if player_count == 10:
                            player.setImageIndex(23)
                        if player_count == 20:
                            player.setImageIndex(24)
                        if player_count == 30:
                           player.setImageIndex(25)
                        if player_count == 40:
                            player.setImageIndex(26)
                            if player_range1.collision(boss):
                                boss_health -= 10
                            player_count = 0
                            attack = False
                    if facingRight:
                        if player_count == 1:
                            player.setImageIndex(27)
                        if player_count == 10:
                            player.setImageIndex(28)
                        if player_count == 20:
                            player.setImageIndex(29)
                        if player_count == 30:
                           player.setImageIndex(30)
                        if player_count == 40:
                            player.setImageIndex(31)
                            if player_range2.collision(boss):
                                boss_health -= 10
                            player_count = 0
                            attack = False
                if weapon == 2:
                    if stamina > 0:
                        if facingLeft:
                            if player_count == 1:
                                player.setImageIndex(77)
                            if player_count == 15:
                                player.setImageIndex(78)
                            if player_count == 30:
                                player.setImageIndex(79)
                                player_count = 0
                                attack = False
                                arrow = Sprite(30,12,None,"arrow_left_00.png")
                                arrow.xSpeed = -groundSpeed - 2
                                arrow.setPosition(player.getX() - 30, player.getY() + (player.getWidth() / 2) - 5)
                                arrows.append(arrow)
                                all_sprites3.add(arrow)
                                player_stamina -= 10
                                stamina_count = 0
                                stamina -= 1
                        if facingRight:
                            if player_count == 1:
                                player.setImageIndex(74)
                            if player_count == 15:
                                player.setImageIndex(75)
                            if player_count == 30:
                                player.setImageIndex(76)
                                player_count = 0
                                attack = False
                                arrow = Sprite(30,12,None,"arrow_right_00.png")
                                arrow.xSpeed = groundSpeed + 2
                                arrow.setPosition(player.getX() + player.getWidth(), player.getY() + (player.getWidth() / 2) - 5)
                                arrows.append(arrow)
                                all_sprites3.add(arrow)
                                player_stamina -= 10
                                stamina -= 1
                                stamina_count = 0
                    else:
                        player_count = 0
                        attack = False
#-----Player Gravity-----
    yVelocity += gravity
    player.move(0,yVelocity)
#-----Player Movement-----
    if playerRight and not bottom and not playerLeft:
        if not collision and not attack:
            player.imageStartEnd(18,19,10)
        facingRight = True
        facingLeft = False
        player.move(4,0)
    elif playerLeft and not bottom and not playerRight:
        if not collision and not attack:
            player.imageStartEnd(20,21,10)
        facingLeft = True
        facingRight = False
        player.move(-4,0)
    if player_health != 0:
        if not playerRight and not playerLeft and bottom and not damage_check:
            player.setImageIndex(55)
        elif not playerRight and not playerLeft and not bottom and not attack and not collision and not side_collision and not damage_check:
            player.setImageIndex(55)
        if not playerRight and not playerLeft and collision and not side_collision and not bottom and not attack and health != 0 and not damage_check:
            defend = True      
            if facingLeft:
                player.setImageIndex(65)
            if facingRight:
                player.setImageIndex(56)
#-----Trophy Gravity-----
    if boss_health == 0 and health != 0 and boss_death_animation > 105:
        t_yVelocity += gravity
        trophy.move(0,t_yVelocity)
        if trophy.collision(ground1):
            t_yVelocity = 0
    if not collision:
        attack = False
        defend = False
    for arrow in arrows:
        arrow.move(arrow.xSpeed,0)
        if arrow.collision(bound5) or arrow.collision(bound6):
            all_sprites3.remove(arrow)
            arrow.move(0, 0)
            arrow.setPosition(0, 0)
            arrows.remove(arrow)
        if arrow.collision(boss):
            if not boss_battle_start:
                boss_battle_start = True
            boss_health -= 10
            all_sprites3.remove(arrow)
            arrow.move(0, 0)
            arrow.setPosition(0, 0)
            arrows.remove(arrow)
#-----Chain Animation-----
    for chain in chained:
        chain.move(chain.xSpeed,0)
        if chain.getX() + chain.getWidth() < boss_body.getX() and boss_facing_left:
            chain_appearance1 += 1
            if chain_appearance1 == 2:
                other_chain = Sprite(20,20,None,"chain_texture_00.png")
                other_chain.setPosition(chain.getX() + chain.getWidth() + chain_position1,chain.getY())
                o_chains.append(other_chain)
                all_sprites3.add(other_chain)
                chain_position1 += 15
                chain_appearance1 = 0
                if other_chain.getX() + other_chain.getWidth() > boss_body.getX():
                    chain_position1 -= 15
        if chain.getX() > boss_body.getX() + boss_body.getWidth() and boss_facing_right:
            chain_appearance1 += 1
            if chain_appearance1 == 2:
                other_chain = Sprite(20,20,None,"chain_texture_00.png")
                other_chain.setPosition(chain.getX() + chain_position1, chain.getY())
                o_chains.append(other_chain)
                all_sprites3.add(other_chain)
                chain_position1 -= 15
                chain_appearance1 = 0
                if other_chain.getX() < boss_body.getX() + boss_body.getWidth():
                    chain_position1 += 15
        if chain.collision(boss_range7) or chain.collision(boss_range8):
            chain.xSpeed = 0
            chain_speed *= -1
            chain.xSpeed = chain_speed
            chain_rebound = True
        if chain.collision(player):
            playerLeft = False
            playerRight = False
            jump = False
            chain_count += 1
            if chain_count == 1:
                if not chain_rebound:
                    chain.xSpeed = 0
                    chain_speed *= -1
                    chain.xSpeed = chain_speed
                    chain_rebound = True
                damage_count += 1
                if damage_count == 1:
                    if player_shield > 0:
                        player_shield -= 20
                        shield -= 2
                    else:
                        if health != 0:
                            player_health -= 10
                            health -= 1
                    shield_count = 0
                damage_check = True
            player.move(chain.xSpeed,0)
        if chain.collision(boss_body) and chain_rebound:
            chain.xSpeed = 0
            chained.remove(chain)
            all_sprites3.remove(chain)
            chain_rebound = False
            chain_away = False
            chain_attack_count = -60
            chain_position1 = 0
            chain_count = 0
            damage_count = 0
            for i in o_chains:
                all_sprites3.remove(i)
                o_chains.remove(i)
#-----Mace Chain Animation-----
    for mace in maces:
        mace.move(mace.xSpeed,0)
        if mace.getX() + mace.getWidth() < boss_body.getX() and boss_facing_left:
            chain_appearance += 1
            if chain_appearance == 3:
                chain = Sprite(20,20,None, "chain_texture_00.png")
                chain.setPosition(mace.getX() + mace.getWidth() + chain_position - chain_distance, mace.getY() + 10)
                chains.append(chain)
                all_sprites3.add(chain)
                chain_position += 15
                chain_appearance = 0
                chain_appeared = True
                if chain.getX() + chain.getWidth() > boss_body.getX():
                    chain_position -= 15
        if mace.getX() > boss_body.getX() + boss_body.getWidth() and boss_facing_right:
            chain_appearance += 1
            if chain_appearance == 3:
                chain = Sprite(20,20,None,"chain_texture_00.png")
                chain.setPosition(mace.getX() - chain_position - chain_distance, mace.getY() + 10)
                chains.append(chain)
                all_sprites3.add(chain)
                chain_position += 15
                chain_appearance = 0
                chain_appeared = True
                if chain.getX()  < boss_body.getX() + boss_body.getWidth():
                    chain_position -= 15
        if mace.collision(player):
            damage_count1 += 1
            if damage_count1 == 1:
                if player_shield > 0:
                    player_shield -= 20
                    shield -= 2
                else:
                    if health != 0:
                        player_health -= 10
                        health -= 1
                shield_count = 0
                damage_check = True
        if mace.collision(bound7) or mace.collision(bound8):
            mace.xSpeed = 0
            mace_stop += 1
            if mace_stop == 120:
                damage_count1 = 0
                mace.xSpeed = mace_speed * -1
                mace_rebound = True
                mace_reattack = False
        if mace.collision(boss_body) and mace_rebound:
            mace.xSpeed = 0
            maces.remove(mace)
            all_sprites3.remove(mace)
            mace_rebound = False
            mace_reattack = False
            mace_away = False
            if not not_mace:
                mace_attack_count = -60
            elif not_mace:
                mace_attack_count = 0
            mace_stop = 0
            damage_count1 = 0
            chain_position = 0
            chain_distance = 10
            for i in chains:
                all_sprites3.remove(i)
                chains.remove(i)
    for chain in chains:
        chain.move(mace.xSpeed,0)
        if chain.collision(boss_body) and chain_appeared:
            all_sprites3.remove(chain)
            chains.remove(chain)
    for o_chain in o_chains:
        o_chain.move(chain_speed,0)
        if o_chain.collision(boss_body) and chain_rebound:
            all_sprites3.remove(o_chain)
            o_chains.remove(o_chain)
    if damage_check and health != 0:
        damage_check_count += 1
        if facingLeft:
            if damage_check_count == 1:
                player.setImageIndex(85)
            if damage_check_count == 15:
                damage_check_count = 0
                damage_check = False
        if facingRight:
            if damage_check_count == 1:
                player.setImageIndex(86)
            if damage_check_count == 15:
                damage_check_count = 0
                damage_check = False
    if boss_health == 0 and trophy_up and health != 0:
        if player.collision(trophy):
            player_win_count += 1
            if player_win_count == 1:
                all_sprites3.remove(player)
                all_sprites3.remove(trophy)
                player_win = Sprite(75,75,None,"player_trophy_00.png")
                player_win.setPosition(player.getX(),player.getY() - 25)
                all_sprites3.add(player_win)
    if not chain_away and not mace_away:
        for chain in chains:
            all_sprites3.remove(chains)
            chains.remove(chain)
        for o_chain in o_chains:
            all_sprites3.remove(chains)
            o_chains.remove(o_chain)
        for mace in maces:
            all_sprites3.remove(mace)
            maces.remove(mace)
        for chain in chained:
            all_sprites3.remove(chain)
            chained.remove(chain)
        for sprites in all_sprites3:
            all_sprites3.remove(sprites)
        all_sprites3.add(back3,ground1,boss,arrows)
        if health != 0 and boss_health != 0:          
            all_sprites3.add(player)
        if health == 0 and boss_health != 0 and death_counter <= 75:
            all_sprites3.add(player)
        if boss_health == 0 and boss_death_animation > 105:
            all_sprites3.remove(boss)
            all_sprites3.add(trophy)
        if boss_health == 0 and not trophy_up and health != 0:
            all_sprites3.add(player)
        if boss_health == 0 and trophy_up and health != 0:
            if player.collision(trophy):
                winner = True
        if winner:
            winner_text += 1
            all_sprites3.remove(player)
            all_sprites3.remove(trophy)
            all_sprites3.add(back3,ground1,arrows,player_win)
            if winner_text == 1:
                print("""
Congratulations on beating our game!!!""")
        if health == 0:
            playerLeft = False
            playerRight = False
            playerUp = False
            playerDown = False
            playerUp = False
            jump = False
            attack = False
            death_counter += 1
            if death_counter == 1:
                player.setImageIndex(80)
            if death_counter == 15:
                player.setImageIndex(81)
            if death_counter == 30:
                player.setImageIndex(82)
            if death_counter == 45:
                player.setImageIndex(83)
            if death_counter == 60:
                player.setImageIndex(84)
            if death_counter == 75:
                all_sprites3.remove(player)
                print("""
Good Try!

Please Try Again!!!""")
    if not attack:
        player_count = 0
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            boss_battle = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                playerRight = True
            if event.key == pygame.K_a:
                playerLeft = True
            if event.key == pygame.K_SPACE:
                jump = True
            if event.key == pygame.K_w:
                playerUp = True
            elif event.key == pygame.K_s:
                playerDown = True
            if event.key == pygame.K_t:
                trophy_up = True
            if event.key == pygame.K_1:
                weapon = 1
            if event.key == pygame.K_2:
                weapon = 2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                playerRight = False
            if event.key == pygame.K_a:
                playerLeft = False
            if event.key == pygame.K_SPACE:
                jump = False    
            if event.key == pygame.K_w:
                playerUp = False
            elif event.key == pygame.K_s:
                playerDown = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            attack = True
print("""
This game is made by:
    Ahron Ramos

Thanks for playing my game!!!
""")
pygame.quit()

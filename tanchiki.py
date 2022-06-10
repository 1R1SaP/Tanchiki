from pygame import *
from random import randint
import os
from time import time as timer

import pygame

pygame.init()

img_tank1 = image.load(os.path.join('images', "tank1_up.png"))
img_tank2 = image.load(os.path.join('images', "tank2_up.png"))
img_bullet = image.load(os.path.join('images', "bullet.png"))

win_width = 1024
win_height = 720
display.set_caption("Tanchiki")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(os.path.join('images', 'background1.png')), (win_width, win_height))
stepIndex = 0
step = 1
p1_move = [True, False, False, False]  # ? up, down, left, right
p2_move = [True, False, False, False]  # ? up, down, left, right

stationary = pygame.image.load(os.path.join('images', "tank1_up.png"))
stationary1 = pygame.image.load(os.path.join('images', "tank2_up.png"))
# картинки для анімації
up = [
    image.load(os.path.join('images', "tank1_up.png")),
    image.load(os.path.join('images', "tank1_up_anim.png"))]
down = [
    image.load(os.path.join('images', "tank1_down.png")),
    image.load(os.path.join('images', "tank1_down_anim.png"))]
left = [ 
    image.load(os.path.join('images', "tank1_left.png")),
    image.load(os.path.join('images', "tank1_left_anim.png"))]
right = [
    image.load(os.path.join('images', "tank1_right.png")),
    image.load(os.path.join('images', "tank1_right_anim.png"))]


up1 = [
    image.load(os.path.join('images', "tank2_up.png")),
    image.load(os.path.join('images', "tank2_up_anim.png"))]
down1 = [
    image.load(os.path.join('images', "tank2_down.png")),
    image.load(os.path.join('images', "tank2_down_anim.png"))]
left1 = [
    image.load(os.path.join('images', "tank2_left.png")),
    image.load(os.path.join('images', "tank2_left_anim.png"))]
right1 = [ 
    image.load(os.path.join('images', "tank2_right.png")),
    image.load(os.path.join('images', "tank2_right_anim.png"))]

move_up, move_down, move_left, move_right = True, True, True, True
move_up1, move_down1, move_left1, move_right1 = True, True, True, True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_speed, player_x, player_y, size_x, size_y, direction):
        super().__init__()
        self.image = transform.scale(player_image, (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.stepIndex = 0
        self.direction = direction

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        global p1_move
        if keys[K_a] and self.rect.x > -5 and move_left:
            self.rect.x -= self.speed
            self.direction = [False, False, True, False]
        elif keys[K_d] and self.rect.x < 925 and move_right:
            self.rect.x += self.speed
            self.direction = [False, False, False, True]
        elif keys[K_w] and self.rect.y > 5 and move_up:
            self.rect.y -= self.speed
            self.direction = [True, False, False, False]
        elif keys[K_s] and self.rect.y < 600 and move_down:
            self.rect.y += self.speed
            self.direction = [False, True, False, False]
    # Функція відповідає за анімацію 1 танка
    def reset(self):
        if self.stepIndex > 1:
            self.stepIndex = 0
        if self.direction[0]:

            window.blit(up[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if self.direction[1]:

            window.blit(down[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if self.direction[2]:

            window.blit(left[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if self.direction[3]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(right[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
    def collide_something(self, targets):
        global move_up, move_down, move_left, move_right
        for target in targets:
            if sprite.spritecollide(self, targets, False):
                if abs(self.rect.top - target.rect.bottom) < 10:
                    move_up = False
                    self.rect.y += 1
                if abs(self.rect.bottom - target.rect.top) < 10:
                    move_down = False
                    self.rect.y -= 1
                if abs(self.rect.left - target.rect.right) < 10:
                    move_left = False
                    self.rect.x += 1
                if abs(self.rect.right - target.rect.left) < 10:
                    move_right = False
                    self.rect.x -= 1
            else:
                move_up, move_down, move_left, move_right = True, True, True, True

    def fire(self):
        global b_m
        if self.direction[0]:
            bullet = Bullet(img_bullet, 40, self.rect.centerx,
                            self.rect.top, 10, 10, [True, False, False, False])
            bullets.add(bullet)
        elif self.direction[1]:
            bullet = Bullet(img_bullet, 40, self.rect.centerx,
                            self.rect.bottom, 10, 10, [False, True, False, False])
            bullets.add(bullet)
        elif self.direction[2]:
            bullet = Bullet(img_bullet, 40, self.rect.left,
                            self.rect.centery, 10, 10, [False, False, True, False])
            bullets.add(bullet)
        elif self.direction[3]:
            bullet = Bullet(img_bullet, 40, self.rect.right,
                            self.rect.centery, 10, 10, [False, False, False, True])
            bullets.add(bullet)
        else:
            b_m = [False] * 4


b_m = [False] * 4
bullets = sprite.Group()


class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        global p2_move
        if keys[K_LEFT] and self.rect.x > -5 and move_left1:
            self.rect.x -= self.speed
            self.direction = [False, False, True, False]
        elif keys[K_RIGHT] and self.rect.x < 925 and move_right1:
            self.rect.x += self.speed
            self.direction = [False, False, False, True]
        elif keys[K_UP] and self.rect.y > 5 and move_up1:
            self.rect.y -= self.speed
            self.direction = [True, False, False, False]
        elif keys[K_DOWN] and self.rect.y < 600 and move_down1:
            self.rect.y += self.speed
            self.direction = [False, True, False, False]
    # Функція відповідає за анімацію 2 танка
    def reset(self):
        if self.direction[0]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(up1[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if self.direction[1]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(down1[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if self.direction[2]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(left1[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if self.direction[3]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(right1[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
    def collide_something(self, targets):
        global move_up1, move_down1, move_left1, move_right1
        for target in targets:
            if sprite.spritecollide(self, targets, False):
                if abs(self.rect.top - target.rect.bottom) < 10:
                    move_up1 = False
                    self.rect.y += 1
                if abs(self.rect.bottom - target.rect.top) < 10:
                    move_down1 = False
                    self.rect.y -= 1
                if abs(self.rect.left - target.rect.right) < 10:
                    move_left1 = False
                    self.rect.x += 1
                if abs(self.rect.right - target.rect.left) < 10:
                    move_right1 = False
                    self.rect.x -= 1
            else:
                move_up1, move_down1, move_left1, move_right1 = True, True, True, True
    def fire(self):
        global b_m
        if self.direction[0]:
            bullet = Bullet(img_bullet, 40, self.rect.centerx,
                            self.rect.top, 10, 10, [True, False, False, False])
            bullets.add(bullet)
        elif self.direction[1]:
            bullet = Bullet(img_bullet, 40, self.rect.centerx,
                            self.rect.bottom, 10, 10, [False, True, False, False])
            bullets.add(bullet)
        elif self.direction[2]:
            bullet = Bullet(img_bullet, 40, self.rect.left,
                            self.rect.centery, 10, 10, [False, False, True, False])
            bullets.add(bullet)
        elif self.direction[3]:
            bullet = Bullet(img_bullet, 40, self.rect.right,
                            self.rect.centery, 10, 10, [False, False, False, True])
            bullets.add(bullet)

# клас стіни
class Wall(sprite.Sprite):
    def __init__(self, wall_image, wall_x, wall_y, x_size, y_size,):
        super().__init__()
        self.image = transform.scale(wall_image, (x_size, y_size))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# клас кулі
class Bullet(GameSprite):
    def update(self):
        if self.direction[0]:
            self.rect.y -= self.speed
        elif self.direction[1]:
            self.rect.y += self.speed
        elif self.direction[2]:
            self.rect.x -= self.speed
        elif self.direction[3]:
            self.rect.x += self.speed
        else:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y


run = True
finish = False
# координати танків
x1 = 20
y1 = 300
x2 = 900
y2 = 300
# координати для посилень
boost_x1 = 350
boost_y1 = 20
boost_x2 = 250
boost_y2 = 430
boost_x3 = 350
boost_y3 = 250
#lifes
life1 = 3
life2 = 3
# надписи
font.init()
font = font.Font(None, 50)
win_p1 = font.render("Player 1 Win", True, (0, 255, 255))
win_p2 = font.render("Player 2 Win", True, (0, 255, 255))
reload = font.render("Reloading...", True, (0, 0, 0))
reload1 = font.render("Reloading...", True, (0, 0, 0))
replay = font.render("Press 'R' for replay", True, (0, 255, 255))
# танки
player1 = Player(img_tank1, 8, x1, y1, 100, 100, [True, False, False, False])
player2 = Player2(img_tank2, 8, x2, y2, 100, 100, [True, False, False, False])
p1_hp = 3
p2_hp = 3
speed = 5
# стіни
w1 = Wall(image.load(os.path.join('images', "BIGwoll3.png")), 200, 127, 210, 69)
w2 = Wall(image.load(os.path.join('images', "BIGwoll3.png")), 610, 130, 212, 68)
w3 = Wall(image.load(os.path.join('images', "BIGwoll3.png")), 204, 530, 210, 68)
w4 = Wall(image.load(os.path.join('images', "BIGwoll3.png")), 616, 532, 212, 68)
w5 = Wall(image.load(os.path.join('images', "WallMini.png")), 327, 320, 70, 75)
w6 = Wall(image.load(os.path.join('images', "WallMini.png")), 603, 320, 70, 75)
walls = sprite.Group()
walls.add(w1)
walls.add(w2)
walls.add(w3)
walls.add(w4)
walls.add(w5)
walls.add(w6)

bullets = sprite.Group()

rel_time = False
num_fire = 0
rel_time1 = False
num_fire1 = 0
#Звуки
mixer.init()
mixer.music.load('main_music.wav')
mixer.music.play()
shoot_sound = mixer.Sound('shoot.wav')

while run:
    font_p1 = font.render("P1 HP:  " + str(life1), True, (0, 0, 0))
    font_p2 = font.render("P2 HP:  " + str(life2), True, (0, 0, 0))
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if num_fire < 5 and rel_time == False:
                    num_fire += 1
                    shoot_sound.play()
                    player1.fire()
                if num_fire >=5 and rel_time ==False:
                    last_time = timer()
                    rel_time = True
        if e.type == KEYDOWN:
            if e.key == K_l:
                print("Bah")
                if num_fire1 < 5 and rel_time1 == False:
                    num_fire1 += 1
                    shoot_sound.play()
                    player2.fire()
                if num_fire1 >=5 and rel_time1 ==False:
                    last_time1 = timer()
                    rel_time1 = True

    if not finish:  # finish != True
        window.blit(background, (0, 0))
        window.blit(font_p1, (10, 10))
        window.blit(font_p2, (830, 10))

        player1.update()
        player1.reset()

        player2.update()
        player2.reset()

        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        w4.draw_wall()
        w5.draw_wall()
        w6.draw_wall()

        player1.collide_something(walls)
        player2.collide_something(walls)
        bullets.update()
        bullets.draw(window)

        for bullet in bullets:
            if bullet.rect.x < 0 or bullet.rect.x > win_width or bullet.rect.y < 0 or bullet.rect.y > win_height:
                bullet.kill()
        sprite.groupcollide(bullets, walls, True, False)

        if rel_time == True:
            now_time = timer()
            if now_time - last_time < 3:
                reload = font.render("Reloading...", True, (0, 0, 0))
                window.blit(reload, (20, 60))
            else:
                num_fire = 0
                rel_time = False
        if rel_time1 == True:
            now_time1 = timer()
            if now_time1 - last_time1 < 3:
                reload1 = font.render("Reloading...", True, (0, 0, 0))
                window.blit(reload1, (820, 60))
            else:
                num_fire1 = 0
                rel_time1 = False
        if sprite.spritecollide(player1, bullets, False):
            sprite.spritecollide(player1, bullets, True)
            life1 -= 1
        if sprite.spritecollide(player2, bullets, False):
            sprite.spritecollide(player2, bullets, True)
            life2 -= 1

        if life1 <= 0:
            window.blit(win_p2, (400, 70))
            window.blit(replay, (370, 110))
            mixer.music.load('win_sound.ogg')
            mixer.music.play()
            display.update()
            time.delay(5000)
            finish = True
        if life2 <= 0:
            window.blit(win_p1, (400, 70))
            window.blit(replay, (370, 110))
            mixer.music.load('win_sound.ogg')
            mixer.music.play()
            display.update()
            time.delay(5000)
            finish = True
    else:
        keys = key.get_pressed()
        if keys[K_r]:
            finish = False
            life1, life2 = 3, 3
            for bullet in bullets:
                bullet.kill()
            player1.rect.x = x1
            player1.rect.y = y1
            player2.rect.x = x2
            player2.rect.y = y2
            num_fire = 0
            num_fire1 = 0
            mixer.music.load('main_music.wav')
            mixer.music.play()

    time.delay(50)
    display.update()

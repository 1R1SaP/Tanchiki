from pygame import *
from random import randint
import os

import pygame

pygame.init()

#img_back = image.load(os.path.join("images", "background1.png"))
img_tank1 = image.load(os.path.join('images', "tank1_up.png"))
img_tank2 = image.load(os.path.join('images', "tank2_up.png"))
img_bullet = image.load(os.path.join('images', "bullet.png"))
img_speed = image.load(os.path.join('images', "Speed.png"))


win_width = 800
win_height = 550
display.set_caption("Tanchiki")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(os.path.join('images', 'background1.png')), (win_width, win_height))
stepIndex = 0
step = 1
p1_move = [True, False, False, False]  # ? up, down, left, right
p2_move = [True, False, False, False]  # ? up, down, left, right

stationary = pygame.image.load(os.path.join('images', "tank1_up.png"))
stationary1 = pygame.image.load(os.path.join('images', "tank2_up.png"))
#картинки для анімації
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
    def __init__(self, player_image, player_speed, player_x, player_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(player_image, (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.stepIndex = 0


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        global p1_move
        if keys[K_a] and self.rect.x > -5 and move_left:
            self.rect.x -= self.speed
            p1_move = [False, False, True, False]
        elif keys[K_d] and self.rect.x < 705 and move_right:
            self.rect.x += self.speed
            p1_move = [False, False, False, True]
        elif keys[K_w] and self.rect.y > 5 and move_up:
            self.rect.y -= self.speed
            p1_move = [True, False, False, False]
        elif keys[K_s] and self.rect.y < 450 and move_down:
            self.rect.y += self.speed
            p1_move = [False, True, False, False]
    #Функція відповідає за анімацію 1 танка
    def reset(self):
        if p1_move[0]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(up[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if p1_move[1]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(down[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if p1_move[2]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(left[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if p1_move[3]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(right[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
    def collide(self, targets):
        global move_up, move_down, move_left, move_right
        for target in targets:
            if sprite.spritecollide(self, targets, False):
                if abs(self.rect.top - target.rect.bottom) < 6:
                    move_up = False
                    self.rect.y += 1
                if abs(self.rect.bottom - target.rect.top) < 6:
                   move_down = False
                   self.rect.y -= 1
                if abs(self.rect.left - target.rect.right) < 6:
                    move_left = False
                    self.rect.x += 1
                if abs(self.rect.right - target.rect.left) < 6:
                    move_right = False
                    self.rect.x -= 1
            else:
                move_up, move_down, move_left, move_right = True, True, True, True


class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        global p2_move
        if keys[K_LEFT] and self.rect.x > -5 and move_left1:
            self.rect.x -= self.speed
            p2_move = [False, False, True, False]
        elif keys[K_RIGHT] and self.rect.x < 705 and move_right1:
            self.rect.x += self.speed
            p2_move = [False, False, False, True]
        elif keys[K_UP] and self.rect.y > 5 and move_up1:
            self.rect.y -= self.speed
            p2_move = [True, False, False, False]
        elif keys[K_DOWN] and self.rect.y < 450 and move_down1:
            self.rect.y += self.speed
            p2_move = [False, True, False, False]
    #Функція відповідає за анімацію 1 танка
    def reset(self):
        if p2_move[0]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(up1[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if p2_move[1]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(down1[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if p2_move[2]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(left1[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1
        if p2_move[3]:
            if self.stepIndex > 1:
                self.stepIndex = 0
            window.blit(right1[self.stepIndex], (self.rect.x, self.rect.y))
            self.stepIndex += 1

    def collide(self, targets):
        global move_up1, move_down1, move_left1, move_right1
        for target in targets:
            if sprite.spritecollide(self, targets, False):
                if abs(self.rect.top - target.rect.bottom) < 6:
                    move_up1 = False
                    self.rect.y += 1
                if abs(self.rect.bottom - target.rect.top) < 6:
                    move_down1 = False
                    self.rect.y -= 1
                if abs(self.rect.left - target.rect.right) < 6:
                    move_left1 = False
                    self.rect.x += 1
                if abs(self.rect.right - target.rect.left) < 6:
                    move_right1 = False
                    self.rect.x -= 1
            else:
                move_up1, move_down1, move_left1, move_right1 = True, True, True, True
#клас стіни
class Wall(sprite.Sprite):
    def __init__(self, wall_image, wall_x, wall_y, x_size, y_size):
        super().__init__()
        self.image = transform.scale(wall_image, (x_size, y_size))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#клас кулі
class Bullet(GameSprite):
    def __init__(self, bullet_image,  bullet_x, bullet_y,  bullet_speed, b_size_x, b_size_y):
        super().__init__()
        self.image = transform.scale(bullet_image, (b_size_x, b_size_y))
        self.rect = self.image.get_rect()
        self.rect.x = bullet_x
        self.rect.y = bullet_y
        self.speed = bullet_speed


run = True
finish = False
#координати танків
x1 = 10
y1 = 220
x2 = 700
y2 = 220
#координати для посилень
boost_x1 = 350
boost_y1 = 20
boost_x2 = 250
boost_y2 = 430
boost_x3 = 350
boost_y3 = 250
#надписи
font.init()
font = font.Font(None, 50)
font_p1 = font.render("P1 HP:", True, (0, 0, 0))
font_p2 = font.render("P2 HP:", True, (0, 0, 0))
win_p1 = font.render("Player 1 Win", True, (0, 255, 255))
win_p2 = font.render("Player 2 Win", True, (0, 255, 255))
#танки
player1 = Player(img_tank1, 5, x1, y1, 100, 100)
player2 = Player2(img_tank2, 5, x2, y2, 100, 100)
p1_hp = 3
p2_hp = 3
speed = 5
#стіни
w1 = Wall(image.load(os.path.join('images', "BIGwoll3.png")), 150, 62, 180, 68)
w2 = Wall(image.load(os.path.join('images', "BIGwoll3.png")), 464, 62, 182, 68)
w3 = Wall(image.load(os.path.join('images', "BIGwoll3.png")), 148, 405, 180, 68)
w4 = Wall(image.load(os.path.join('images', "BIGwoll3.png")), 476, 405, 182, 68)
w5 = Wall(image.load(os.path.join('images', "WallMini.png")), 247, 232, 70, 75)
w6 = Wall(image.load(os.path.join('images', "WallMini.png")), 477, 234, 70, 75)
walls = sprite.Group()
walls.add(w1)
walls.add(w2)
walls.add(w3)
walls.add(w4)
walls.add(w5)
walls.add(w6)

bullets = sprite.Group()

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:  # finish != True
        window.blit(background, (0, 0))
        window.blit(font_p1, (10, 10))
        window.blit(font_p2, (650, 10))
        #функція для стрільби(ще не готова)
        def fire(x, y):
            bullet = Bullet(img_bullet, x, y, 15, 10, 10)

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

    player1.collide(walls)
    player2.collide(walls)

    time.delay(50)
    display.update()

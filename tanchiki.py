from pygame import *
from random import randint
import os

import pygame

pygame.init()

#img_back = image.load(os.path.join("images", "background1.png"))
img_tank1 = image.load(os.path.join('images', "tank1_up.png"))
img_tank2 = image.load(os.path.join('images', "tank2_up.png"))

win_width = 800
win_height = 550
display.set_caption("Tanchiki")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(os.path.join(
    'images', 'background1.png')), (win_width, win_height))
stepIndex = 0
step = 1
p1_move = [False] * 4  # ? up, down, left, right
p2_move = [False] * 4  # ? up, down, left, right

stationary = pygame.image.load(os.path.join('images', "tank1_up.png"))
stationary1 = pygame.image.load(os.path.join('images', "tank2_up.png"))

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
        if keys[K_a] and self.rect.x > -5:
            self.rect.x -= self.speed
            p1_move = [False, False, True, False]
        if keys[K_d] and self.rect.x < 705:
            self.rect.x += self.speed
            p1_move = [False, False, False, True]
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
            p1_move = [True, False, False, False]
        if keys[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
            p1_move = [False, True, False, False]

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


class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        global p2_move
        if keys[K_LEFT] and self.rect.x > -5:
            self.rect.x -= self.speed
            p2_move = [False, False, True, False]
        if keys[K_RIGHT] and self.rect.x < 705:
            self.rect.x += self.speed
            p2_move = [False, False, False, True]
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
            p2_move = [True, False, False, False]
        if keys[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
            p2_move = [False, True, False, False]

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


run = True
finish = False

x1 = 10
y1 = 220
x2 = 700
y2 = 220

font.init()
font = font.Font(None, 50)
font_p1 = font.render("P1 HP:", True, (0, 0, 0))
font_p2 = font.render("P2 HP:", True, (0, 0, 0))

player1 = Player(img_tank1, 4, x1, y1, 80, 80)
player2 = Player2(img_tank2, 4, x2, y2, 80, 80)
speed = 5

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:  # finish != True
        window.blit(background, (0, 0))
        window.blit(font_p1, (10, 10))
        window.blit(font_p2, (650, 10))

    player1.update()
    player1.reset()

    player2.update()
    player2.reset()

    time.delay(50)
    display.update()

"""
Project Name: Untitled Zombie Game
File Name: PlayerController.py
Author: Lex Hall
Last Updated: 12-6-2018
Python Version: 3.6
Pygame Version: 1.9.3
"""

import math
import pygame
import Bullet
import Constants as const


class PlayerController(object):
    def __init__(self, pawnMap):
        self.pawnMap = pawnMap
        self.unChangedImage = pygame.image.load("survivor.png").convert_alpha()
        self.reSizedImage = pygame.transform.scale(self.unChangedImage, (40,40))
        self.originalRect = self.reSizedImage.get_rect()
        self.rotatedImage = self.reSizedImage
        self.rotatedRect = self.originalRect
        self.pos = (200, 200)
        self.angle = 0
        self.speed = 0
        self.strafeSpeed = 0
        self.dx = 0
        self.dy = 0
        self.bullets = []
        self.bulletTimer = -1


    def handlePlayerInput(self, keys):
        if keys[pygame.K_w]:
            self.speed = const.PLAYER_MOVE_SPEED
        if keys[pygame.K_s]:
            self.speed = -const.PLAYER_MOVE_SPEED
        if keys[pygame.K_w] and keys[pygame.K_s]:
            self.speed = 0
        if keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
            self.speed = const.PLAYER_RUN_SPEED
        if keys[pygame.K_e]:
            if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_q]:
                self.strafeSpeed = const.PLAYER_STRAFE_SPEED
        if keys[pygame.K_q]:
            if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_e]:
                self.strafeSpeed = -const.PLAYER_STRAFE_SPEED
        if keys[pygame.K_a]:
            self.angle += const.PLAYER_TURN_SPEED
        elif keys[pygame.K_d]:
            self.angle -= const.PLAYER_TURN_SPEED
        if self.angle == 360 or self.angle == -360:
            self.angle = 0
        if keys[pygame.K_SPACE]:
            self.fireGun()


    def update(self, tick):
        self.rotate()
        self.move()
        deadBullets = []
        for bullet in self.bullets:
            if bullet.isAlive:
                bullet.update()
            else:
                deadBullets.append(bullet)
        for deadBullet in deadBullets:
            self.bullets.remove(deadBullet)
        del deadBullets
        if self.bulletTimer > -1:
            self.bulletTimer -= 1
        

    def draw(self):
        self.pawnMap.blit(self.rotatedImage, self.rotatedRect)
        for bullet in self.bullets:
            if bullet.isAlive:
                pygame.draw.circle(self.pawnMap, const.BLACK, (bullet.lastX, bullet.lastY), 3)
                bullet.draw(self.pawnMap)


    def rotate(self):
        self.rotatedImage = pygame.transform.rotate(self.reSizedImage, self.angle)
        self.rotatedRect = self.rotatedImage.get_rect()
        self.rotatedRect.topleft = (self.pos[0] - self.rotatedRect.center[0], self.pos[1] - self.rotatedRect.center[1])


    def move(self):
        if self.strafeSpeed == 0:
            self.dx = self.speed * math.cos(self.angle*(math.pi/180))
            self.dy = self.speed * -math.sin(self.angle*(math.pi/180))
            self.pos = (self.pos[0] + self.dx, self.pos[1] + self.dy)
            self.speed = 0
        else:
            self.dx = self.strafeSpeed * math.cos((self.angle + 90)*(math.pi/180))
            self.dy = self.strafeSpeed * -math.sin((self.angle + 90)*(math.pi/180))
            self.pos = (self.pos[0] + self.dx, self.pos[1] + self.dy)
            self.strafeSpeed = 0
       
    def fireGun(self):
        if self.bulletTimer == -1:
            self.bullets.append(Bullet.Bullet(self.pos[0], self.pos[1], self.angle))
            self.bulletTimer = 3
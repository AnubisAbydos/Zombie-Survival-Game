"""
Project Name: Untitled Zombie Game
File Name: PlayerController.py
Author: Lex Hall
Last Updated: 11-13-2018
Python Version: 3.6
Pygame Version: 1.9.3
"""

import math
import pygame
import Constants as const


class PlayerController(object):
    def __init__(self):
        self.unChangedImage = pygame.image.load("survivor.png").convert_alpha()
        self.reSizedImage = pygame.transform.scale(self.unChangedImage, (40,40))
        self.originalRect = self.reSizedImage.get_rect()
        self.rotatedImage = self.reSizedImage
        self.rotatedRect = self.originalRect
        self.pos = (800, 800)
        self.angle = 0
        self.speed = 0
        self.strafeSpeed = 0
        self.dx = 0
        self.dy = 0

    def handleInput(self, keys):
        if keys[pygame.K_w]:
            self.speed = 1
        if keys[pygame.K_s]:
            self.speed = -1
        if keys[pygame.K_w] and keys[pygame.K_s]:
            self.speed = 0
        if keys[pygame.K_w] and keys[pygame.K_LSHIFT]:
            self.speed = 2
        if keys[pygame.K_e]:
            if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_q]:
                self.strafeSpeed = 1
        if keys[pygame.K_q]:
            if not keys[pygame.K_w] and not keys[pygame.K_s] and not keys[pygame.K_e]:
                self.strafeSpeed = -1
        if keys[pygame.K_a]:
            self.angle += 2
        elif keys[pygame.K_d]:
            self.angle -= 2
        if self.angle == 360 or self.angle == -360:
            self.angle = 0

    def update(self, tick):
        self.rotate()
        self.move()
        

    def draw(self, gameMap):
        gameMap.blit(self.rotatedImage, (self.pos[0] - self.rotatedRect.center[0], self.pos[1] - self.rotatedRect.center[1]))

    def rotate(self):
        self.rotatedImage = pygame.transform.rotate(self.reSizedImage, self.angle)
        self.rotatedRect = self.rotatedImage.get_rect()

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
       
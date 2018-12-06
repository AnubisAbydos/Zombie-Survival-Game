"""
Project Name: Untitled Zombie Game
File Name: Bullet.py
Author: Lex Hall
Last Updated: 12-6-2018
Python Version: 3.6
Pygame Version: 1.9.3
"""

import math
import pygame
from random import *
import Constants as const


class Bullet(object):
    def __init__ (self, startX, startY, angle):
        self.x = startX
        self.y = startY
        self.lastX = startX
        self.lastY = startY
        self.angle = (angle - 90) + randint(-5, 5)
        self.velocity = 20
        self.isAlive = True
        self.dx = self.velocity * math.cos((self.angle + 90)*(math.pi/180))
        self.dy = self.velocity * -math.sin((self.angle + 90)*(math.pi/180))

    def update(self):
        self.lastX = int(round(self.x))
        self.lastY = int(round(self.y))
        self.x = self.x + self.dx
        self.x = int(round(self.x))
        self.y = self.y + self.dy
        self.y = int(round(self.y))
        if self.x >= const.GAMEMAP_X or self.x <= 0:
            self.isAlive = False
        if self.y >= const.GAMEMAP_Y or self.y <= 0:
            self.isAlive = False

    def draw(self, screen):
        pygame.draw.circle(screen, const.WHITE, (self.x, self.y), 2)
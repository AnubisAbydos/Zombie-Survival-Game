"""
Project Name: Untitled Zombie Game
File Name: MapController.py
Author: Lex Hall
Last Updated: 11-13-2018
Python Version: 3.6
Pygame Version: 1.9.3
"""

import math
import pygame
import Constants as const


class MapController(object):
    def __init__(self):
        self.gameMap = pygame.Surface((const.GAMEMAP_X, const.GAMEMAP_Y))
        self.mapX = 600
        self.mapY = 600

    def handleInput(self, mousePos):
        pass

    def update(self, playerController):
        self.gameMap.fill(const.BLACK, playerController.rotatedRect)

    def draw(self, window):
        window.blit(self.gameMap, (0,0), (self.mapX, self.mapY, const.WINDOW_X, const.WINDOW_Y))
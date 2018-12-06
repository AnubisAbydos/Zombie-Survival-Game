"""
Project Name: Untitled Zombie Game
File Name: GameController.py
Author: Lex Hall
Last Updated: 11-15-2018
Python Version: 3.6
Pygame Version: 1.9.3
"""

import pygame
import Constants as const
import MapController
import PlayerController


class GameController(object):
    def __init__(self):
        self.window = pygame.display.set_mode((const.WINDOW_X, const.WINDOW_Y))
        self.gameMap = pygame.Surface((const.GAMEMAP_X, const.GAMEMAP_Y))
        self.pawnMap = pygame.Surface((const.GAMEMAP_X, const.GAMEMAP_Y))
        self.playerController = PlayerController.PlayerController(self.pawnMap)
        self.mapController = MapController.MapController(self.gameMap)
        self.tick = 1


    def handleInput(self):
        keys = pygame.key.get_pressed()
        mousePos = pygame.mouse.get_pos()
        self.playerController.handlePlayerInput(keys)
        self.mapController.handleMapInput(mousePos)


    def update(self):
        self.tick += 1
        if self.tick == const.FRAME_RATE + 1:
            self.tick = 1
        self.mapController.update()
        self.playerController.update(self.tick)


    def draw(self):
        pygame.draw.rect(self.pawnMap, const.BLACK, self.playerController.rotatedRect)
        self.mapController.draw(self.window)
        self.playerController.draw()

        self.window.blit(self.gameMap, (0,0), (self.mapController.mapX, self.mapController.mapY, const.WINDOW_X, const.WINDOW_Y))
        self.window.blit(self.pawnMap, (0,0), (self.mapController.mapX, self.mapController.mapY, const.WINDOW_X, const.WINDOW_Y))
        
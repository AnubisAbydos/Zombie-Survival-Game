"""
Project Name: Untitled Zombie Game
File Name: Untitled_Zombie_Game.py
Author: Lex Hall
Last Updated: 11-13-2018
Python Version: 3.6
Pygame Version: 1.9.3
"""

import os
import sys
import pygame
import Constants as const
import PlayerController
import MapController

# Centers Pygame Window on screen
os.environ['SDL_VIDEO_CENTERED'] = '1'


### Main sets screen and runs game loop
def main():
    pygame.init()

    # Build the screen
    window = pygame.display.set_mode((const.WINDOW_X, const.WINDOW_Y))

    done = False

    # Start the clock
    clock = pygame.time.Clock()
    tick = 1

    # Lock cursor to window
    #pygame.event.set_grab(True)

    # Build Classes
    playerController = PlayerController.PlayerController()
    mapController = MapController.MapController()

    # Loop Start
    while not done:
        keys = pygame.key.get_pressed()
        mousePos = pygame.mouse.get_pos()

        playerController.handleInput(keys)
        mapController.handleInput(mousePos)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        playerController.update(tick)
        mapController.update(playerController)

        window.fill(const.BLACK)
        playerController.draw(mapController.gameMap)
        mapController.draw(window)

        tick += 1
        if tick == const.FRAME_RATE + 1:
            tick = 1

        # Throttle frame rate
        clock.tick(const.FRAME_RATE)
        # Uncomment below to output fps to console
        #print(clock.get_fps())
               
        # Flip to user
        pygame.display.flip()

    #Loop End

    pygame.quit()
    sys.exit()

# Call main to start game
if __name__ == "__main__":
    main()
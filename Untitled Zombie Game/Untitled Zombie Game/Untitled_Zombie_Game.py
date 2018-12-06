"""
Project Name: Untitled Zombie Game
File Name: Untitled_Zombie_Game.py
Author: Lex Hall
Last Updated: 11-15-2018
Python Version: 3.6
Pygame Version: 1.9.3
"""

import os
import sys
import pygame
import Constants as const
import GameController

# Centers Pygame Window on screen
os.environ['SDL_VIDEO_CENTERED'] = '1'


### Main sets screen and runs game loop
def main():
    pygame.init()

    done = False

    # Start the clock
    clock = pygame.time.Clock()

    # Lock cursor to window
    #pygame.event.set_grab(True)

    # Build Game Controller
    gameController = GameController.GameController()

    # Loop Start
    while not done:
        gameController.handleInput()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
        
        gameController.update()

        gameController.draw()

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
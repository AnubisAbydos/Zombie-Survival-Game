"""
Project Name: Untitled Zombie Game
File Name: Untitled_Zombie_Game.py
Author: Lex Hall
Last Updated: 11-13-2018
Python Version: 3.6
Pygame Version: 1.9.3
"""

import sys
import pygame


### Main calls game sets screen and runs game loop
def main():
    pygame.init()

    # Build the screen
    screen = pygame.display.set_mode((800, 800))

    done = False

    # Start the clock
    clock = pygame.time.Clock()

    # Lock cursor to window
    pygame.event.set_grab(True)

    # Loop Start
    while not done:

                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Throttle frame rate
        clock.tick(const.FRAMERATE)
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
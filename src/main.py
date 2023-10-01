import pygame
from labyrinthgame import runGame
 
# Setting window size
WIDTH = 700
HEIGHT = 420
 
# The most important methods for initializing the game - setting screen, caption and music.
# Ambient used as background music is called "Dark Cinematic Suspenseful Ambient" by Ashot-Danielyan-Composer
# and is from free, non-copyrighted library pixabay.com

def main():
  pygame.init()
  SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption("devil's labyrinth")
  pygame.mixer.music.load("../files/ambient.mp3")
  pygame.mixer.music.play(-1)
  runGame(SCREEN)
 
if __name__ == "__main__":
    main()
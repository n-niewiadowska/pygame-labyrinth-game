import pygame, sys, os
from pygame.locals import *

# Functions below describe functionality and looks of the main menu. Player can play the game
# by clicking space bar or quit it with Q key.

def menuScreen(screen, background, color):
  while True:
    # Window events - quitting game
    for e in pygame.event.get():
      if e.type == QUIT or (e.type == pygame.KEYUP and e.key == pygame.K_q):
        sys.exit()
      if e.type == pygame.KEYUP and e.key == pygame.K_SPACE:
        return

    menuFont = pygame.font.SysFont('cambria', 80)
    menuSurf = menuFont.render("devil's labyrinth", True, color)
    menuRect = menuSurf.get_rect()
    menuRect.topleft = (80, 40)

    screen.blit(background, (0,0))

    screen.blit(menuSurf, menuRect)
    menuButtons(screen, color)
    pygame.display.update()
    pygame.time.wait(500)

def menuButtons(screen, color):
  firstButtonFont = pygame.font.SysFont('cambria', 30)
  secButtonFont = pygame.font.SysFont('cambria', 30)
  firstButtonSurf = firstButtonFont.render("press space to start", True, color)
  secButtonSurf = secButtonFont.render("press q to quit", True, color)
  firstButtonRect = firstButtonSurf.get_rect()
  secButtonRect = secButtonSurf.get_rect()
  firstButtonRect.topleft = (50, 300)
  secButtonRect.topleft = (470, 300)

  screen.blit(firstButtonSurf, firstButtonRect)
  screen.blit(secButtonSurf, secButtonRect)
import pygame, sys, os
from pygame.locals import *

# Functions below create game ending screen. finishScreen with finishMessage are displayed after finishing
# a single level.

def finishScreen(screen, background, color):
  while True:
    # Window events - quitting the game
    for e in pygame.event.get():
      if e.type == QUIT:
        sys.exit()
      if e.type == pygame.KEYDOWN:
        return

    finishFont = pygame.font.SysFont('cambria', 110)
    finishSurf = finishFont.render('marvellous!', True, color)
    finishRect = finishSurf.get_rect()
    finishRect.topleft = (80, 40)

    screen.blit(background, (0,0))

    screen.blit(finishSurf, finishRect)
    finishMessage(screen, color)
    pygame.display.update()
    pygame.time.wait(500)

def finishMessage(screen, color):
  messageFont = pygame.font.SysFont('cambria', 50)
  messageSurf = messageFont.render("you found the devil's gold!", True, color)
  messageRect = messageSurf.get_rect()
  messageRect.topleft = (80, 200)
  screen.blit(messageSurf, messageRect)

# theEndScreen starts when all levels are finished.

def theEndScreen(screen, background, color):
  while True:
    for e in pygame.event.get():
      if e.type == QUIT:
        sys.exit()
      if e.type == pygame.KEYDOWN:
        return

    theEndFont = pygame.font.SysFont('cambria', 110)
    theEndSurf = theEndFont.render('the end!', True, color)
    theEndRect = theEndSurf.get_rect()
    theEndRect.topleft = (20, 50)

    screen.blit(background, (0,0))

    screen.blit(theEndSurf, theEndRect)
    pygame.display.update()
    pygame.time.wait(500)
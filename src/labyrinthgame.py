# Important imports of libraries and other project files.

import pygame, sys, os, datetime
from pygame.locals import *
from os import listdir
from os.path import isfile, join
from menuscreens import menuScreen
from finishscreens import finishScreen, theEndScreen
 
# TILESIZE - width and height of squares
TILESIZE = 20
 
#            R    G    B
BLACK     = (0,   0,   0)
CLARET    = (107,  0,  0)
GOLD      = (255,196,  0)
RED       = (255,  0,  0)
RED_LIGHT = (240, 96, 96)
WHITE     = (255,255,255)

# Player Class initializes the player (light-red square looking for gold) and describes their movements in
# the labyrinth. It also contains function collisions, which analyses the board for player's collisions with
# the wall and prevents them from passing through it.
 
class Player(object):
 
  def __init__(self):
    self.rect = pygame.Rect(2*TILESIZE, 2*TILESIZE, TILESIZE, TILESIZE)
 
  def move(self, walls, dx, dy):
    if dx != 0:
      self.moveSingleAxis(walls, dx, 0)
    if dy != 0:
      self.moveSingleAxis(walls, 0, dy)
 
  def moveSingleAxis(self, walls, dx, dy):
    self.rect.x += dx
    self.rect.y += dy
    self.collisions(walls, dx, dy)
 
  def collisions(self, walls, dx, dy):
    for wall in walls:
      if self.rect.colliderect(wall.rect):
        if dx > 0:
          self.rect.right = wall.rect.left
        if dx < 0:
          self.rect.left = wall.rect.right
        if dy > 0:
          self.rect.bottom = wall.rect.top
        if dy < 0:
          self.rect.top = wall.rect.bottom

# Treasure Class creates the treasure - the level's 'exit'. Player tries to reach it.
 
class Treasure(object):

  def __init__(self, x=4, y=4):
    self.rect = pygame.Rect(x*TILESIZE, y*TILESIZE, TILESIZE, TILESIZE)
 
# Wall Class creates a piece of labyrinth's wall.
 
class Wall(object):
 
  def __init__(self, x, y, width=1, height=1):
    self.rect = pygame.Rect(x*TILESIZE, y*TILESIZE, width*TILESIZE, height*TILESIZE)

# runGame is a main function collecting every instruction and calls them.
 
def runGame(screen):

  # Loading background pictures and menu screen.
 
  menu_bg = pygame.image.load("../files/menu_image.png")
  finish_bg = pygame.image.load("../files/finish_image.png")
  end_bg = pygame.image.load("../files/end_image.png")

  menuScreen(screen, menu_bg, WHITE)

  # Code below iterates sorted folder with levels and transform them into functioning board.

  levels = []

  levels_maps = listdir("../levels")
  bubbleSort(levels_maps)

  for plik in reversed(levels_maps):
    a_path = os.path.join("../levels", plik)
    if isfile(a_path):
      lvl = open(a_path).read().splitlines()
      levels.append(lvl)

  for map in levels:
    player = Player()
    treasure = Treasure()
    walls = []
    
    for y, row in enumerate(map):
      for x, col in enumerate(row):
        if col == "W":
          walls.append(Wall(x, y))
        if col == "P":
          treasure = Treasure(x, y)
    
  # Calling functions:
  # After main menu the game starts. After each finished level the time is saved in files/timescores
  # and end-level screen is shown. When all levels are finished, single click of any key will show ending
  # screen, while double click quits the game.

    gameLoop(screen, player, walls, treasure)
    saveScore()
    finishScreen(screen, finish_bg, WHITE)

  theEndScreen(screen, end_bg, WHITE)

# gameLoop is the main loop of the game. It defines window events, keys for moving the player and also draws
# objects.
 
def gameLoop(screen, player, walls, treasure):
  while True:
    # Window events - quitting the game
    for e in pygame.event.get():
      if e.type == QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
        sys.exit()
    
    # Keys - after clicking right key the player moves along a given axis.
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] or key[pygame.K_a]:
      player.move(walls, -1, 0)
    if key[pygame.K_RIGHT] or key[pygame.K_d]:
      player.move(walls, 1, 0)
    if key[pygame.K_UP] or key[pygame.K_w]:
      player.move(walls, 0, -1)
    if key[pygame.K_DOWN] or key[pygame.K_s]:
      player.move(walls, 0, 1)

    # Game's logic - when the player reaches the treasure, the current level ends.
    if player.rect.colliderect(treasure.rect):
      return

    # Screen's color, new game frame.
    screen.fill(BLACK)
    
    # Drawing objects on the frame.
    for wall in walls:
      pygame.draw.rect(screen, CLARET, wall.rect)

    pygame.draw.rect(screen, GOLD, treasure.rect)
    pygame.draw.rect(screen, RED_LIGHT, player.rect)

    # Display on screen when the frame is ready.
    pygame.display.update()

# Function saving the time of finishing game in files/timescores.txt and sorting it.

def saveScore():
  with open('../files/timescores.txt', 'a') as file:
    file.write(f'Time: {datetime.datetime.now()}\n')
  
  with open('../files/timescores.txt', 'r') as file:
    allScores = file.read().splitlines()
    bubbleSort(allScores)

# bubble sort for sorting time scores.

def bubbleSort(file):
  for j in range(len(file) - 1):
    for i in range(len(file) - 1 - j):
      if file[i] < file[i + 1]:
        k = file[i + 1]
        file[i + 1] = file[i]
        file[i] = k

  return file

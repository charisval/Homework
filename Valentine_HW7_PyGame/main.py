"""
Name: Charis Valentine
Date: 3/10/25
Homework: HW8 Moving Objects
Description: Program where frog can be moved across the screen using WASD and three cars move across the screen.

"""
import pygame
from pygame.constants import KEYDOWN

# initialize Pygame
pygame.init()

# window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# set window title
pygame.display.set_caption("Frogger")

# fps
clock = pygame.time.Clock()
dt = 0
speed = 10
"""game loop"""
running = True

# frog current position
frog_pos = [275, 340]

# vehicles current positions
truck_pos = [0, 76]
pcar_pos = [525, 176]
ycar_pos = [0, 275]

while running:
  """handle events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == KEYDOWN:
      if event.key == pygame.K_w:
        frog_pos[1] -= 20
      if event.key == pygame.K_s:
        frog_pos[1] += 20
      if event.key == pygame.K_a:
        frog_pos[0] -= 20
      if event.key == pygame.K_d:
        frog_pos[0] += 20
  """update game state"""
  # x axis bounds for frog
  if frog_pos[0] < 0:
    frog_pos[0] = 0
  if frog_pos[0] > width - 40:
    frog_pos[0] = width - 40
  # y axis bounds for frog
  if frog_pos[1] < 0:
    frog_pos[1] = 0
  if frog_pos[1] > height - 40:
    frog_pos[1] = height - 40
  # car movements
  truck_pos[0] += 20
  ycar_pos[0] += 15
  pcar_pos[0] -= 20
  # car loops - cars will respawn after reaching the edge
  if truck_pos[0] == width:
    truck_pos[0] = 0
  if ycar_pos[0] == width:
    ycar_pos[0] = 0
  if pcar_pos[0] < 0:
    pcar_pos[0] = 525
  """draw on screen"""

  # clear screen
  screen.fill("white")

  # lanes
  pygame.draw.line(screen, "gray", (0, 300), (600, 300), 60)
  pygame.draw.line(screen, "gray", (0, 200), (600, 200), 60)
  pygame.draw.line(screen, "gray", (0, 100), (600, 100), 60)

  # spawn area
  pygame.draw.rect(screen, (255, 212, 229), pygame.Rect((0, 330), (600, 70)))

  # win area
  pygame.draw.rect(screen, (255, 212, 229), pygame.Rect((0, 0), (600, 71)))

  # draw frog
  pygame.draw.rect(screen, (128, 239, 128),
                   pygame.Rect((frog_pos[0], frog_pos[1]), (40, 40)))

  # purple truck
  pygame.draw.rect(screen, (219, 220, 255),
                   pygame.Rect((truck_pos[0], truck_pos[1]), (120, 50)))

  # pink car
  pygame.draw.rect(screen, (238, 203, 255),
                   pygame.Rect((pcar_pos[0], pcar_pos[1]), (75, 50)))

  # yellow car
  pygame.draw.rect(screen, (254, 255, 163),
                   pygame.Rect((ycar_pos[0], ycar_pos[1]), (75, 50)))

  # update screen
  pygame.display.flip()

  # fps
  dt = clock.tick(speed) / 1000

# quit pygame
pygame.quit()

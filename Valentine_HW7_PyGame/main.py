"""
Name: Charis Valentine
Date: 3/3/25
Homework: PyGame
Description:
This is a program that draws shapes on the screen, including three lanes, a frog, and three different types of vehicles.
"""
import pygame

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

while running:
  """handle events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  """update game state"""
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
  pygame.draw.rect(screen, (128, 239, 128), pygame.Rect((275, 340), (40, 40)))

  # purple truck
  pygame.draw.rect(screen, (219, 220, 255), pygame.Rect((0, 76), (120, 50)))

  # pink car
  pygame.draw.rect(screen, (238, 203, 255), pygame.Rect((0, 176), (75, 50)))

  # yellow car
  pygame.draw.rect(screen, (254, 255, 163), pygame.Rect((0, 275), (75, 50)))

  # update screen
  pygame.display.flip()

  # fps
  dt = clock.tick(speed) / 1000

# quit pygame
pygame.quit()

import pygame

# Initialize Pygame
pygame.init()

# window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width, height))

# set window title
pygame.display.set_caption("snake")

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
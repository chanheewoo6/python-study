import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display variables
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Set up asset folders
GAME_FOLDER = OSError.path.dirname(__file__)
IMG_FOLDER = OSError.path.join(GAME_FOLDER, "img")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set the title of the window
pygame.display.set_caption("Super Mario Bros.")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Keep the loop running at the right speed
    clock.tick(FPS)
    # Process input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update game state
    # ...
    # Draw/render
    screen.fill(BLACK)
    # ...
    # Flip the display
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()


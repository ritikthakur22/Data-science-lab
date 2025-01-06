import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Olympic Logo with Thick Circles")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 87, 184)
YELLOW = (255, 185, 0)
BLACK_CIRCLE = (0, 0, 0)
GREEN = (0, 158, 96)
RED = (239, 51, 64)

# Function to draw a thick circle using multiple concentric circles
def ThickCircle(r, xc, yc, color, thickness):
    for t in range(thickness):
        Circle(r + t, xc, yc, color)

# Function to draw a circle using the Midpoint algorithm
def Circle(r, xc, yc, color):
    x = 0
    y = r
    p = 1 - r

    def plot_points(cx, cy, x, y):
        # Plot the symmetrical points for all octants
        screen.set_at((cx + x, cy + y), color)
        screen.set_at((cx - x, cy + y), color)
        screen.set_at((cx + x, cy - y), color)
        screen.set_at((cx - x, cy - y), color)
        screen.set_at((cx + y, cy + x), color)
        screen.set_at((cx - y, cy + x), color)
        screen.set_at((cx + y, cy - x), color)
        screen.set_at((cx - y, cy - x), color)

    plot_points(xc, yc, x, y)

    while x < y:
        if p <= 0:
            x += 1
            p += 2 * x + 1
        else:
            x += 1
            y -= 1
            p += (2 * x) - (2 * y) + 1
        plot_points(xc, yc, x, y)

# Main loop
def main():
    # Draw the circles
    screen.fill(WHITE)

    radius = 80  # Base radius of each circle
    thickness = 10  # Thickness of each circle
    offset = 100  # Distance between circles

    # Top row of circles
    ThickCircle(radius, 200, 200, BLUE, thickness)  # Blue circle
    ThickCircle(radius, 400, 200, BLACK_CIRCLE, thickness)  # Black circle
    ThickCircle(radius, 600, 200, RED, thickness)  # Red circle

    # Bottom row of circles
    ThickCircle(radius, 300, 300, YELLOW, thickness)  # Yellow circle
    ThickCircle(radius, 500, 300, GREEN, thickness)  # Green circle

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()

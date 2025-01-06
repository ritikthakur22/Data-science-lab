import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Circle Drawing Algorithm")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Function to draw a circle using the Midpoint algorithm
def Circle(r, xc, yc):
    x = 0
    y = r
    p = 1 - r

    def plot_points(cx, cy, x, y):
        # Plot the symmetrical points for all octants
        screen.set_at((cx + x, cy + y), WHITE)  # Bottom right
        screen.set_at((cx - x, cy + y), WHITE)  # Bottom left
        screen.set_at((cx + x, cy - y), WHITE)  # Top right
        screen.set_at((cx - x, cy - y), WHITE)  # Top left
        screen.set_at((cx + y, cy + x), WHITE)  # Bottom-top right
        screen.set_at((cx - y, cy + x), WHITE)  # Bottom-top left
        screen.set_at((cx + y, cy - x), WHITE)  # Top-Bottom right
        screen.set_at((cx - y, cy - x), WHITE)  # Top-Bottom left

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
    # Draw the circles only once
    screen.fill(BLACK)
    Circle(100, 400, 400)
    Circle(80, 400, 400)
    Circle(60, 400, 400)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()

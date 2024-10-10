import pygame
import math
import random

# Initialize PyGame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("PyGame Animations")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Bouncing Ball
class BouncingBall:
    def __init__(self):
        self.x, self.y = width // 2, height // 2
        self.dx, self.dy = 5, 5
        self.radius = 30

    def update(self):
        self.x += self.dx
        self.y += self.dy
        if self.x - self.radius < 0 or self.x + self.radius > width:
            self.dx = -self.dx
        if self.y - self.radius < 0 or self.y + self.radius > height:
            self.dy = -self.dy

    def draw(self):
        pygame.draw.circle(window, red, (self.x, self.y), self.radius)

# Rotating Square
class RotatingSquare:
    def __init__(self):
        self.x, self.y = width // 2, height // 2
        self.size = 50
        self.angle = 0

    def update(self):
        self.angle += 5
        self.angle %= 360

    def draw(self):
        points = [
            (self.x + self.size * math.cos(math.radians(self.angle)), 
             self.y + self.size * math.sin(math.radians(self.angle))),
            (self.x + self.size * math.cos(math.radians(self.angle + 90)), 
             self.y + self.size * math.sin(math.radians(self.angle + 90))),
            (self.x + self.size * math.cos(math.radians(self.angle + 180)), 
             self.y + self.size * math.sin(math.radians(self.angle + 180))),
            (self.x + self.size * math.cos(math.radians(self.angle + 270)), 
             self.y + self.size * math.sin(math.radians(self.angle + 270))),
        ]
        pygame.draw.polygon(window, green, points)

# Growing and Shrinking Circle
class GrowingShrinkingCircle:
    def __init__(self):
        self.x, self.y = width // 2, height // 2
        self.radius = 30
        self.growing = True

    def update(self):
        if self.growing:
            self.radius += 2
            if self.radius > 100:
                self.growing = False
        else:
            self.radius -= 2
            if self.radius < 30:
                self.growing = True

    def draw(self):
        pygame.draw.circle(window, blue, (self.x, self.y), self.radius)

# Spiral Motion
class SpiralMotion:
    def __init__(self):
        self.angle = 0
        self.radius = 0

    def update(self):
        self.angle += 5
        self.radius += 0.5
        if self.radius > 200:
            self.radius = 0

    def draw(self):
        x = width // 2 + self.radius * math.cos(math.radians(self.angle))
        y = height // 2 + self.radius * math.sin(math.radians(self.angle))
        pygame.draw.circle(window, yellow, (int(x), int(y)), 10)

# Wave Motion
class WaveMotion:
    def __init__(self):
        self.angle = 0

    def update(self):
        self.angle += 5

    def draw(self):
        for x in range(0, width, 20):
            y = height // 2 + 50 * math.sin(math.radians(self.angle + x))
            pygame.draw.circle(window, white, (x, int(y)), 5)

# Random Walk
class RandomWalk:
    def __init__(self):
        self.x, self.y = width // 2, height // 2

    def update(self):
        direction = random.choice([(0, 5), (0, -5), (5, 0), (-5, 0)])
        self.x += direction[0]
        self.y += direction[1]
        if self.x < 0: self.x = width
        if self.x > width: self.x = 0
        if self.y < 0: self.y = height
        if self.y > height: self.y = 0

    def draw(self):
        pygame.draw.circle(window, red, (self.x, self.y), 5)

# Pulsating Star
class PulsatingStar:
    def __init__(self):
        self.x, self.y = width // 2, height // 2
        self.size = 20
        self.growing = True

    def update(self):
        if self.growing:
            self.size += 1
            if self.size > 50:
                self.growing = False
        else:
            self.size -= 1
            if self.size < 20:
                self.growing = True

    def draw(self):
        points = []
        for i in range(5):
            angle = math.radians(i * 72)
            x = self.x + self.size * math.cos(angle)
            y = self.y + self.size * math.sin(angle)
            points.append((x, y))
            x = self.x + self.size // 2 * math.cos(angle + math.radians(36))
            y = self.y + self.size // 2 * math.sin(angle + math.radians(36))
            points.append((x, y))
        pygame.draw.polygon(window, green, points)

# Create instances of animations
animations = [
    BouncingBall(),
    RotatingSquare(),
    GrowingShrinkingCircle(),
    SpiralMotion(),
    WaveMotion(),
    RandomWalk(),
    PulsatingStar()
]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animations
    for animation in animations:
        animation.update()

    # Draw animations
    window.fill(black)
    for animation in animations:
        animation.draw()
    pygame.display.flip()

    # Control frame rate
    clock.tick(60)

pygame.quit()


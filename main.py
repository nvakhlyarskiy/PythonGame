
import pygame
import random
import os

WIDTH = 1851
HEIGHT = 1020
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
MY_COLOR_0 = (255, 0, 128)
MY_COLOR_1 = (127, 0, 189)
MY_COLOR_2 = (210, 180, 140)
MY_COLOR_3 = (255, 140, 0)

# set up assets folders
# Windows: "C:\Users\chris\Documents\img"
# Mac: "/Users/chris/Documents\img"
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")
player1_img_path = os.path.join(img_folder, "p1_jump.png")
player2_img_path = os.path.join(img_folder, "p2_jump.png")
player3_img_path = os.path.join(img_folder, "p3_jump.png")


class Player(pygame.sprite.Sprite):
    # sprite for the Player
    def __init__(self, img_path, point_xy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = point_xy
        self.y_speed = 5

    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        if self.rect.top < 200:
            self.y_speed = 5
        if self.rect.left > WIDTH:
            self.rect.right = 0


# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player_1 = Player(player1_img_path, (WIDTH*1/4, HEIGHT*4/10))
all_sprites.add(player_1)
player_2 = Player(player2_img_path, (WIDTH*2/4, HEIGHT/2))
all_sprites.add(player_2)
player_3 = Player(player3_img_path, (WIDTH*3/4, HEIGHT*6/10))
all_sprites.add(player_3)
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

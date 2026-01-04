import pygame
import sys

#Tile Manager
from tiles import TileManager 

TILE_SIZE = 40
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 5

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.direction.x = 1
        elif keys[pygame.K_LEFT]: self.direction.x = -1
        else: self.direction.x = 0

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tile_manager = TileManager(TILE_SIZE) 
        self.player = pygame.sprite.GroupSingle()
        self.setup_level(level_data)
    
    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            cells = row.split() 
            for col_index, cell in enumerate(cells):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if cell == 'P':
                    self.player.add(Player((x, y)))
                else:
                    self.tile_manager.create_tile((x, y), cell)
                
    def run(self):
        #Draw
        self.tile_manager.tiles.draw(self.display_surface)
        self.player.update()
        self.player.draw(self.display_surface)

# main
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

with open('level.txt', 'r') as file:
    level_map = [line.strip() for line in file.readlines()]

current_level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('lightblue')
    current_level.run()
    pygame.display.update()
    clock.tick(FPS)
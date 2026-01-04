import pygame
import sys

TILE_SIZE = 40
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60


#Tile Map Loader

#GAME MANAGER
class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.setup_level(level_data)
    
    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if cell == 'X':
                    tile = Tile((x, y))
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                
    def run(self):
        #Draw
        self.tiles.draw(self.display_surface)
        self.player.draw(self.display_surface)

        #Update
        self.player.update()


#main
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

    screen.fill(('lightblue'))
    current_level.run()
    pygame.display.update()
    clock.tick(FPS)
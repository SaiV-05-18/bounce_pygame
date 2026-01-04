import pygame

#TILE DICTIONARY
TILE_CONFIG = {
    '1': {'color': 'grey', 'solid': True},
    '2': {'color': 'green', 'solid': True},
}

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, tile_type):
        super().__init__()
        self.tile_type = tile_type
        self.image = pygame.Surface((size, size))
        
        config = TILE_CONFIG.get(tile_type, {'color': 'white', 'solid': False})
        self.image.fill(config['color'])
        
        self.rect = self.image.get_rect(topleft=pos)

class TileManager:
    def __init__(self, tile_size):
        self.tile_size = tile_size
        self.tiles = pygame.sprite.Group()

    def create_tile(self, pos, tile_type):
        # We only create a tile if it's defined in our config
        if tile_type in TILE_CONFIG:
            new_tile = Tile(pos, self.tile_size, tile_type)
            self.tiles.add(new_tile)
            return new_tile
        return None
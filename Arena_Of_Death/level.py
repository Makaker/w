import pygame
from setting import *
from tile import Tile
from pers import Pers
from debug import debug


class Level:
    def __init__(self):
        # get_surface() помогает в любой части кода получить рабочую поверхность - экран
        self.display_surface = pygame.display.get_surface()

        # настройка группы спрайтов
        # видимые спрайты (группа)
        self.visible_sprite = YSortCameraGroup()
        # группа спрайтов - припятствия
        self.obstacle_sprite = pygame.sprite.Group()

        # sprite setup вызывваем метод этого же класса
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x, y), [self.visible_sprite, self.obstacle_sprite])
                if col == 'p':
                    self.pers = Pers((x, y), [self.visible_sprite], self.obstacle_sprite)

    def run(self):
        self.visible_sprite.custom_draw(self.pers)
        self.visible_sprite.update()
        # обновить и рисовать игру
        debug(self.pers.direction)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):

        #general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, pers):

        # getting the offset
        self.offset.x = pers.rect.centerx - self.half_width
        self.offset.y = pers.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)




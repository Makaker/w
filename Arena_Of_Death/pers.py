import pygame
from setting import *


class Pers(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.image = pygame.image.load('images/pers/pers1_pos_start.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)

        self.direction = pygame.math.Vector2()
        self.speed = 3

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = - 1
        elif keys[pygame.K_s]:
            self.direction.y = + 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = + 1
        elif keys[pygame.K_a]:
            self.direction.x = - 1
        else:
            self.direction.x = 0

    def move(selfs, speed):
        # проверка длины вектора если больше 0 вездде будет 1
        if selfs.direction.magnitude() != 0:
            selfs.direction = selfs.direction.normalize()

        selfs.rect.x += selfs.direction.x * speed
        selfs.colision('horizontal')
        selfs.rect.y += selfs.direction.y * speed
        selfs.colision('vertical')
        # selfs.rect.center += selfs.direction * speed

    def colision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:  # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:  # moving up
                        self.rect.top = sprite.rect.bottom

    def update(self):
        self.input()
        self.move(self.speed)

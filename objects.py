import pygame, random
from pygame.math import Vector2

class Dorito(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.displaySurface = pygame.display.get_surface()
        self.image = pygame.image.load('images/dorito.png').convert_alpha()       
        self.image = pygame.transform.scale(self.image, (124, 102))
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = Vector2()

    def physics(self):
        y = random.randint(50, 500)
        self.rect.center += self.direction
        self.direction.x = -10
        
        if self.rect.centerx <= -100:
            self.rect.centerx = 1400
            self.rect.centery = y
    def update(self):
        # Used to debug hitboxes
        #pygame.draw.rect(self.displaySurface, ('black'), self.rect, 1)
        self.physics()

class Clouds(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)

        self.image = pygame.image.load('images/cloud.png').convert_alpha()
        #self.image = pygame.transform.scale(self.image, (125, 125))
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2()
        self.image.set_alpha(100)

    def physics(self):
        y = random.randint(50, 500)
        self.rect.center += self.direction
        self.direction.x = -3
        
        if self.rect.centerx <= -100:
            self.rect.centerx = 1400
            self.rect.centery = y

    def update(self):
        self.physics()



import pygame
from pygame import Vector2

# Inherits pygmae.sprite.Sprite whatever that is
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        # Inherits ALL the methods and properties of the parent
        super().__init__(groups)

        self.displaySurface = pygame.display.get_surface()
        self.image = pygame.image.load('images/birb2.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (80, 70))
        self.rect = self.image.get_rect(center = pos)
        self.direction = Vector2()
        self.status = True

    # Input controls for the player
    def movement(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            self.direction.y = -9
    # Physics for the player
    def physics(self):
        self.rect.center += self.direction
        gravity = .8
        # Gravity
        self.direction.y += gravity
        gravity += 0.01

    # Updates the player's movement and physics
    def update(self):
        # Used to debug hitbox
        #pygame.draw.rect(self.displaySurface, ('black'), self.rect, 1)
        self.movement()
        self.physics()



        
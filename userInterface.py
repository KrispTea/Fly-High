import pygame, math, time

class Menu:
    def __init__(self):
        self.displaySurface = pygame.display.get_surface()
        self.png = pygame.image.load('images/title-modified.png')
        self.font = pygame.font.Font('misc/Topaznew.ttf', 40)
        self.welcomeText = self.font.render('Press Enter to Start', True, 'black')

    def display(self):
        # Makes the text float with maf\
        self.displaySurface.blit(self.welcomeText, (300, 475 + math.sin(time.time()*5)*5 - 25))
        self.displaySurface.blit(self.png, (250, 69))
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            return "start"

    def settings():
        pass

    
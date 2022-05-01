# Libraries and files
import random, pygame, sys
from player import Player
from objects import Dorito, Clouds
from userInterface import Menu


# General pygame setup
class Game:
    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((1024, 576))
        pygame.display.set_caption("Fly High")
        self.clock = pygame.time.Clock()
        self.color = 142, 181, 240
        # From the window class
        self.window = Window()
        self.run()

    # Pygame loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill(self.color)
            self.window.run()
            pygame.display.update()
            self.clock.tick(60)
    
class Window:
    def __init__(self):
        # Gets the display
        self.displaySurface = pygame.display.get_surface()
        # Sprite groups
        self.visibleSprites = pygame.sprite.Group()
        self.enemySprites = pygame.sprite.Group()

        # UI variables
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 100)
        self.ui = Menu()

        # Game bools
        self.forceStop = True
        self.whileMenu = True
        
    def startGame(self):
        self.forceStop = False
        self.visibleSprites.empty()
        self.enemySprites.empty()
        self.mapPlayer()
        self.mapEnemy()

    def mapPlayer(self):
        # Creates and player then assigns it to position 0, 0 
        # and also assigns it to the visibleSprites grouping
        Player((250, 0),[self.visibleSprites])

    def mapEnemy(self):
        # Selects random elevations to spawn enemies
        randomY1 = random.randint(10, 576)
        randomY2 = random.randint(10, 576)
        randomY3 = random.randint(10, 576)
    
        # See mapPlayer()
        Dorito((1400, randomY1),[self.enemySprites])
        Dorito((1700, randomY2),[self.enemySprites])
        Dorito((2000, randomY3),[self.enemySprites])

    def collision(self):
        # Returns a (tuple? list?) then checks to see if the objects are colliding
        # We kill the targets for now
        # True kills the visiblesprite groups and False doesn't kill the enemySprites group
        collided = pygame.sprite.groupcollide(self.visibleSprites, self.enemySprites, True, True)
        if collided:
            for targets in collided:
                pygame.time.wait(1000)
                targets.kill()
                self.forceStop = True

    def scoreCount(self):
       # Keeps track of score/distance traveled
        scoreBoard = self.font.render(str(self.score // 100), False, ("Black"))
        self.displaySurface.blit(scoreBoard, (450, 75))

        self.score += 1
            
    # Updates the game
    def run(self):

        if self.whileMenu:
            selection = self.ui.display()
            if selection == "start":
                self.whileMenu = False
                self.forceStop = False
                self.startGame()

        if not self.forceStop:
            self.scoreCount()
            self.collision()
            # Draws all visible sprites
            self.visibleSprites.draw(self.displaySurface)
            self.enemySprites.draw(self.displaySurface)
            # Updates all sprites
            self.visibleSprites.update() 
            self.enemySprites.update()

        else:
            self.score = 0
            mouse = pygame.mouse.get_pressed()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                self.whileMenu = False
                self.startGame()
                
            elif mouse[2]:
                self.whileMenu = True


if __name__ == "__main__":
    game = Game()
    game.run()

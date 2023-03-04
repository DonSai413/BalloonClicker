import pygame
from pygame.locals import *
import random

# Define our square object and call super to
# give it all the properties and methods of pygame.sprite.Sprite
# Define the class for our square objects
#ASSET INITIALIZATION
#Test Start
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
         
        # Define the dimension of the surface
        # Here we are making squares of side 25px
        self.surf = pygame.Surface((25, 25))
         
        # Define the color of the surface using RGB color coding.
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()
#Test End
image = pygame.image.load("sky_image.jpg")

#GAME INITIALIZATION
pygame.init()
pygame.display.set_caption("Balloon Clicker")
screen = pygame.display.set_mode((800, 600))

#SPRITE INITIALIZATION
#Test Start
square1 = Square()
square2 = Square()
square3 = Square()
square4 = Square()
#square5 = Square()
#square5.surf.fill(0,0,255)
#square5.surf = pygame.Surface((800,600))
#Test End

#VARIABLES
x = 0
y = 0

xchange = 10
ychange = 10

play = True

zeroZero = (0,0)

#GAME LOOP
while play:
	#screen.blit(square5.surf, (0, 0))
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_BACKSPACE:
				play = False
		elif event.type == QUIT:
			play = False
	#Test Start
	screen.fill((0, 0, 0))
	screen.blit(image, dest = zeroZero)
	screen.blit(square1.surf,(x,y))
	x = random.randrange(1, 800)
	y = random.randrange(1, 600)
	"""if x >= 600 or x <= 0:
		xchange = xchange*-1*random.randrange(1, 5)
	if y >= 800 or x <= 0:
		ychange = ychange*-1*random.randrange(1, 5)"""
	screen.blit(square2.surf,(40,530))
	screen.blit(square3.surf,(730,40))
	screen.blit(square4.surf,(730,530))
	#Test End
	pygame.display.flip()

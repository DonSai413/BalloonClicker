import pygame
from pygame.locals import *
import random
import sys
from collections import defaultdict
import time

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
pygame.font.init()
pygame.display.set_caption("Balloon Clicker")
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Circle(pygame.sprite.Sprite):
	def __new__(cls, *args, **kwargs):
		#print("1. Create a new instance of Circle.")
		return super().__new__(cls)
	def __init__(self):
		self.index = 0
		self.radius = 20
		self.balloonX = random.randrange(1, 799)
		self.balloonY = random.randrange(1, 599)
		self.red = random.randrange(0, 255)
		self.green = random.randrange(0, 255)
		self.blue = random.randrange(0, 255)
		self.color = (self.red, self.green, self.blue)
		self.thickness = 0;
		self.center_point = (self.balloonX, self.balloonY)
	#random.seed(clock.get_time())
	"""balloonX = random.randrange(1, 799)
	balloonY = random.randrange(1, 599)
	red = random.randrange(100, 150)
	green = random.randrange(100, 150)
	blue = random.randrange(100, 150)
	color = (red, green, blue)
	thickness = 0;
	center_point = (balloonX, balloonY)"""
	def drawCircle(self):
		#print("DrawCircle is running.")
		#print(self.balloonX,self.balloonY)
		pygame.draw.circle(screen, self.color, self.center_point, self.radius, self.thickness)
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
	#Balloon Default Values 
#balloonX = 100
#balloonY = 100
#radius = 20
#thickness = 0

balloonsInList = 0
balloonSpawn = 1

font1 = pygame.font.SysFont('freesanbold.ttf', 50)
font2 = pygame.font.SysFont('freesanbold.ttf', 100)
buttonFont = pygame.font.SysFont('freesanbold.ttf', 30)
mouse1 = False

xchange = 10
ychange = 10

circleCounter = 0;
autoPopCounter = 0;

points = 0
pointsValue = 1

clockSpeed = 1
autoPop = 0

pointsCost = 10
speedUpCost = 10*clockSpeed
speedDownCost = speedUpCost/5
balloonSpawnCost = 50
autoPopCost = 100

circleGroup = list()
play = True

zeroZero = (0,0)

#TEXT
text1 = font1.render(f"Points: {points}", True, (20, 10, 150))
morePoints = buttonFont.render(f"More Points per Balloon: {pointsCost}", True, (0, 0, 0))
loseText = font2.render("YOU LOSE", True, (255, 0, 0))

pointsBox = text1.get_rect()

pointsBox.center = (700, 50)


#GAME LOOP
#circleGroup.append(Circle())
while play:
	clock.tick(clockSpeed)
	#ticks = pygame.time.get_ticks()
	#screen.blit(square5.surf, (0, 0))
	#EVENT CAPTURING
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_BACKSPACE:
				play = False
		elif event.type == MOUSEBUTTONDOWN:
			mouse1 = True
			mousePos = pygame.mouse.get_pos()
			for circle in circleGroup:
				if mousePos >= (circle.balloonX - circle.radius, circle.balloonY - circle.radius) and mousePos <= (circle.balloonX + circle.radius, circle.balloonY + circle.radius):
					points += pointsValue
					newint = circle.index
					for x in range(newint, len(circleGroup)):
						circleGroup[x].index -= 1
					del circleGroup[newint]
					break
		elif event.type == MOUSEBUTTONUP:
			mouse1 = False
		elif event.type == QUIT:
			play = False
	#Test Start
	screen.fill((0, 0, 0))
	#points += 1
	screen.blit(image, dest = zeroZero)
	#screen.blit(square1.surf,(balloonX,balloonY))
	#if ticks > 10000:
	#x = random.randrange(1, 800)
	#y = random.randrange(1, 600)
	"""if x >= 600 or x <= 0:
		xchange = xchange*-1*random.randrange(1, 5)
	if y >= 800 or x <= 0:
		ychange = ychange*-1*random.randrange(1, 5)"""
	#screen.blit(square2.surf,(40,530))
	#screen.blit(square3.surf,(730,40))
	#screen.blit(square4.surf,(730,530))
	text1 = font1.render(f"Points: {points}", True, (20, 10, 150))
	#circleGroup.append(Circle())
	for x in range(balloonSpawn):
		circleGroup.append(Circle())
		balloonsInList = len(circleGroup)
		for circle in circleGroup:
			circle.index = circleCounter
			circle.drawCircle()
			circleCounter += 1

		"""
		#Note: Attempt to fix multi-circle deletion bug. Come back
		#to later if time.
		for circle in circleGroup:
			print(circle.index)"""
		"""balloonX = random.randrange(1, 799)
		balloonY = random.randrange(1, 599)
		red = random.randrange(100, 150)
		green = random.randrange(100, 150)
		blue = random.randrange(100, 150)
		color = (red, green, blue)
		center_point = (balloonX, balloonY)
		pygame.draw.circle(screen, color, center_point, radius, thickness)"""
	screen.blit(text1, pointsBox)
	circleCounter = 0
	if balloonsInList > 100:
		#loseText = font2.render("YOU LOSE", True, (255, 0, 0))
		loseBox = loseText.get_rect()
		loseBox.center = (400, 300)
		screen.blit(loseText, loseBox)
		pygame.display.flip()
		time.sleep(5)
		quit()
	if points > 10000:
		winText = font2.render("YOU WIN", True, (0, 255, 0))
		winBox = winText.get_rect()
		winBox.center = (400, 300)
		screen.blit(winText, winBox)
		pygame.display.flip()
		time.sleep(5)
		quit()
	while autoPopCounter < autoPop:
		circleGroup.pop()
		points += pointsValue
	#Test End
	autoPopCounter = 0;
	pygame.display.flip()

import pygame
from pygame.locals import *
from pygame import mixer
import random
import sys
import time
import numpy as np
import math

#GAME INITIALIZATION
pygame.init()
mixer.init()
pygame.font.init()
pygame.display.set_caption("Balloon Clicker")
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

imageName = ["sky_image.jpg"]
image = pygame.image.load(imageName[0])

musicName = ["pop.mp3", "victory.mp3", "lose.mp3", "wrong.mp3", "Ping.mp3"]
mixer.music.load(musicName[0])
mixer.music.set_volume(.3)

def wrong():
	mixer.music.load(musicName[3])
	mixer.music.set_volume(.1)
	mixer.music.play()

def ping():
	mixer.music.load(musicName[4])
	mixer.music.set_volume(.1)
	mixer.music.play()

class Circle(pygame.sprite.Sprite):
	def __new__(cls, *args, **kwargs):
		#print("1. Create a new instance of Circle.")
		return super().__new__(cls)
	def __init__(self):
		self.index = 0
		self.radius = 20
		self.balloonX = random.randrange(1, 599)
		self.balloonY = random.randrange(1, 599)
		self.red = random.randrange(0, 255)
		self.green = random.randrange(0, 255)
		self.blue = random.randrange(0, 255)
		self.color = (self.red, self.green, self.blue)
		self.thickness = 0;
		self.center_point = (self.balloonX, self.balloonY)
	def drawCircle(self):
		pygame.draw.circle(screen, self.color, self.center_point, self.radius, self.thickness)

#VARIABLES

balloonsInList = 0
balloonSpawn = 1

font1 = pygame.font.SysFont('freesanbold.ttf', 50)
font2 = pygame.font.SysFont('freesanbold.ttf', 100)
titleFont = pygame.font.SysFont('freesanbold.ttf', 100)
buttonFont = pygame.font.SysFont('freesanbold.ttf', 20)
infoFont = pygame.font.SysFont('freesanbold.ttf', 35)
mouse1 = False

xchange = 10
ychange = 10

circleCounter = 0;
autoPopCounter = 0;

points = 998
pointsValue = 1

clockSpeed = 30
autoPop = 0
popSpeed = 0
timerbase = 2

timer2 = 2
pointsCost = 10
speedUpCost = 10*timerbase
speedDownCost = speedUpCost/5
balloonSpawnCost = 50
autoPopCost = 100

circleGroup = list()
play = True
menu = True

gray = (100, 100, 100)
zeroZero = (0,0)

mouseClickBacklog = list()

def drawButton (posX, posY):
	pygame.draw.rect(screen , gray, [posX, posY, 200, 50])

#TEXT
text1 = font1.render(f"Points: {points}", True, (20, 10, 150))
morePoints = buttonFont.render(f"More Points per Balloon: {pointsCost}", True, (0, 0, 0))
speedUpText = buttonFont.render(f"Speed up: {speedUpCost}", True, (0, 0, 0))
speedDownText = buttonFont.render(f"Slow down: {speedDownCost}", True, (0, 0, 0))
balloonSpawnText1 = buttonFont.render(f"Spawn more balloons per ", True, (0, 0, 0))
balloonSpawnText2 = buttonFont.render(f"tick: {balloonSpawnCost}", True, (0, 0, 0))
autoPopText1 = buttonFont.render(f"Auto-pops balloons if there", True, (0, 0, 0))
autoPopText2 = buttonFont.render(f"are any: {autoPopCost}", True, (0, 0, 0))
loseText = font2.render("YOU LOSE", True, (255, 0, 0))
titleText = titleFont.render("BALLOON CLICKER", True, (255, 255, 255))
playText = font1.render("PLAY", True, (255, 255, 255))
quitText = font1.render("QUIT", True, (255, 255, 255))
infoText = infoFont.render("Get over 1000 points to win. Lose if there are over 100 balloons", True, (255, 255, 255))

pointsBox = text1.get_rect()
pointsPurchaseBox = morePoints.get_rect()
speedUpBox = speedUpText.get_rect()
speedDownBox = speedDownText.get_rect()
balloonSpawnBox1 = balloonSpawnText1.get_rect()
balloonSpawnBox2 = balloonSpawnText2.get_rect()
autoPopBox1 = autoPopText1.get_rect()
autoPopBox2 = autoPopText2.get_rect()
titleBox = titleText.get_rect()
playBox = playText.get_rect()
quitBox = quitText.get_rect()
infoBox = infoText.get_rect()

pointsBox.center = (650, 50)
pointsPurchaseBox.center = (700, 125)
speedUpBox.center = (700, 200)
speedDownBox.center = (700, 275)
balloonSpawnBox1.center = (700, 350)
balloonSpawnBox2.center = (700, 360)
autoPopBox1.center = (700, 425)
autoPopBox2.center = (700, 435)
titleBox.center = (400, 200)
playBox.center = (375, 400)
quitBox.center = (375, 500)
infoBox.center = (400, 300)

#MENU LOOP
while menu:
	clock.tick(clockSpeed)
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_BACKSPACE:
				quit()
		elif event.type == MOUSEBUTTONDOWN:
			mousePos = list(pygame.mouse.get_pos())
			mousePos2 = [int(mousePos[0]), int(mousePos[1])]
			if mousePos2[0] > 350 and mousePos2[0] < 425:
				if mousePos2[1] > 375 and mousePos2[1] < 425:
					menu = False
					ping()
				elif mousePos2[1] > 475 and mousePos2[1] < 525:
					quit()
		elif event.type == MOUSEBUTTONUP:
			mouse1 = False
		elif event.type == QUIT:
			quit()
	screen.blit(titleText, titleBox)
	screen.blit(playText, playBox)
	screen.blit(quitText, quitBox)
	pygame.display.flip()
#GAME LOOP
screen.fill((0, 0, 0))
screen.blit(infoText, infoBox)
pygame.display.flip()
time.sleep(5)
pygame.display.flip()
while play:
	clock.tick(clockSpeed)
	#EVENT CAPTURING
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_BACKSPACE:
				play = False
		elif event.type == MOUSEBUTTONDOWN:
			mousePos = list(pygame.mouse.get_pos())
			mousePos2 = [int(mousePos[0]), int(mousePos[1])]
			mouseClickBacklog.append(mousePos2)
		elif event.type == MOUSEBUTTONUP:
			mouse1 = False
		elif event.type == QUIT:
			play = False
	
	text1 = font1.render(f"Points: {points}", True, (20, 10, 150))
	#ITEM SPAWN LOOP
	if (timer2 % clockSpeed == 0):
		timer2 = timerbase
		screen.fill((0, 0, 0))
		screen.blit(image, dest = zeroZero)
		for x in range(balloonSpawn):
			circleGroup.append(Circle())
			for circle in circleGroup:
				circle.index = circleCounter
				circle.drawCircle()
				circleCounter += 1

		screen.blit(text1, pointsBox)

		#BUTTONS
		drawButton(600, 100)
		morePoints = buttonFont.render(f"More Points per Balloon: {pointsCost}", True, (0, 0, 0))
		screen.blit(morePoints,pointsPurchaseBox)

		drawButton(600, 175)
		speedUpText = buttonFont.render(f"Speed up: {speedUpCost}", True, (0, 0, 0))
		screen.blit(speedUpText,speedUpBox)

		drawButton(600, 250)
		speedDownText = buttonFont.render(f"Slow down: {speedDownCost}", True, (0, 0, 0))
		screen.blit(speedDownText, speedDownBox)

		drawButton(600, 325)
		balloonSpawnText1 = buttonFont.render(f"Spawn more balloons per ", True, (0, 0, 0))
		balloonSpawnText2 = buttonFont.render(f"tick: {balloonSpawnCost}", True, (0, 0, 0))
		screen.blit(balloonSpawnText1, balloonSpawnBox1)
		screen.blit(balloonSpawnText2, balloonSpawnBox2)

		drawButton(600, 400)
		autoPopText1 = buttonFont.render(f"Auto-pops balloons if there", True, (0, 0, 0))
		autoPopText2 = buttonFont.render(f"are any: {autoPopCost}", True, (0, 0, 0))
		screen.blit(autoPopText1, autoPopBox1)
		screen.blit(autoPopText2, autoPopBox2)

		#END OF BUTTONS
		circleCounter = 0
		#AUTOPOPPER
		while autoPopCounter < autoPop:
			autoPopCounter += 1
			#print(autoPopCounter)
			#print(autoPop)
			if(len(circleGroup) != 0):
				#print(balloonsInList)
				#print(len(circleGroup)-1)
				del circleGroup[len(circleGroup)-1]
				mixer.music.load(musicName[0])
				mixer.music.set_volume(.3)
				mixer.music.play()
				points += pointsValue
	#CLICK HANDLER
	for iterator in mouseClickBacklog:
		#print(mouseClickBacklog)
		if iterator[0] >= 600 and iterator[0]  <= 800:
			if iterator[1] >= 100 and iterator[1] <= 150:
				if points >= pointsCost:
					ping()
					pointsValue += 1
					points = points - pointsCost
					pointsCost *= 1.25
				else:
					wrong()
			elif  iterator[1] >= 175 and iterator[1] <= 225:
				if points >= speedUpCost and timerbase < clockSpeed:
					ping()
					timerbase += 1
					points = points - speedUpCost
					speedUpCost = 10 * timerbase
				else:
					wrong()
			elif iterator[1] >= 250 and iterator[1] <= 300:
				if points >= speedDownCost and timerbase > 1:
					ping()
					timerbase -= 1
					points = points - speedDownCost
					speedDownCost = speedUpCost / 5
				else:
					wrong()
			elif iterator[1] >= 325 and iterator[1] <= 375:
				if points >= balloonSpawnCost:
					ping()
					balloonSpawn += 1
					points = points - balloonSpawnCost
					balloonSpawnCost *= 1.5
				else:
					wrong()
			elif iterator[1] >= 400 and iterator[1] <= 450:
				if points >= autoPopCost:
					ping()
					autoPop += 1
					points = points - autoPopCost
					autoPopCost *= 1.75
				else:
					wrong()
		else:
			for circle in circleGroup:
				if iterator[0] >= (circle.balloonX - circle.radius) and iterator[0] <= (circle.balloonX + circle.radius):
					if iterator[1] >= (circle.balloonY - circle.radius) and iterator[1] <= (circle.balloonY + circle.radius):
						points += pointsValue
						newint = circleGroup.index(circle)
						for x in range(newint, len(circleGroup)):
							circleGroup[x].index -= 1
						del circleGroup[newint]
						mixer.music.load(musicName[0])
						mixer.music.set_volume(.3)
						mixer.music.play()
		mouseClickBacklog.remove(iterator)
	#WIN/LOSE MESSAGES
	if len(circleGroup) > 100:
		loseBox = loseText.get_rect()
		loseBox.center = (400, 300)
		screen.blit(loseText, loseBox)
		pygame.display.flip()
		mixer.music.load(musicName[2])
		mixer.music.set_volume(.2)
		mixer.music.play()
		time.sleep(5)
		quit()
	if points > 1000:
		winTime = pygame.time.get_ticks()
		winTimeS = math.floor(winTime/1000)
		winTimeM = math.floor(winTimeS/60)
		winTimeTrueS = (winTimeS-winTimeM*60)
		winText = font2.render("YOU WIN", True, (0, 255, 0))
		if len(str(winTimeTrueS)) == 1:
			winText2 = buttonFont.render(f"Time: {winTimeM}:0{winTimeTrueS}", True, (0, 0, 0))
		else:
			winText2 = buttonFont.render(f"Time: {winTimeM}:{winTimeTrueS}", True, (0, 0, 0))
		winBox = winText.get_rect()
		winBox2 = winText2.get_rect()
		winBox.center = (400, 300)
		winBox2.center = (400, 350)
		screen.blit(winText2, winBox2)
		screen.blit(winText, winBox)
		#text1 = font1.render(f"Points: {points}", True, (20, 10, 150))
		screen.blit(text1, pointsBox)
		pygame.display.flip()
		mixer.music.load(musicName[1])
		mixer.music.set_volume(.2)
		mixer.music.play()
		time.sleep(5)
		quit()

	autoPopCounter = 0;
	timer2 += 1
	pygame.display.flip()

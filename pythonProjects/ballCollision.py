#Imports
import math
import random
import time
from random import randint
import pygame
import sys
 
#initialize pygame
pygame.init()
#Defines the ScreenWidth and Height
screenWidth = 500
screenHeight = 500
#Creates ScreenSize
screenSize = (screenWidth,screenHeight)
# set the size for the surface (screen)
screen = pygame.display.set_mode((screenSize),0)
# set the caption for the screen
pygame.display.set_caption("Collision Template")
 
#Creates Colours w/ RGB Values
white = (255,255,255)
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)
yellow = (255,239,0)

#Fills the Screen White and update the screen
screen.fill(white)
pygame.display.update()

#Loops 
program = True
setUpScreen = True
bouncingScreen = False
finalScreen = False
#Min/Max Values (Altered for Pygame / Visibility)
maxX = 500
maxY = 500
minX = 0
minY = 0
minRadius = 10
maxRadius = 80
minAngle = 0
maxAngle = 359

#Number of balls and colours for the balls
ballAmount = 0
ballColours = [green,red,blue,yellow]
#Thickness for circle (0 for a coloured in circle
thickness = 0
#Speed of travel for the ball (Visibility)
ballSpeed = screenWidth / 25 * 2
#Did a collision occur yet
collisionOccurred = False
#Info for text
colourText = red
textX = screenWidth / 6  
textY = screenHeight / 5
titleFont = pygame.font.SysFont("Comic Sans MS", 32)

#Class
class BouncingBall(object):
    #Init method for variable setup 
    def __init__(self,x,y,radius,angle,colour):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
        self.colour = colour

    #Checks if an angle must be changed
    def changeAngle(self):
        #For the right wall and changes angle
        if self.x + self.radius >= screenWidth and self.angle >= 0 and self.angle <= 90:  
            self.angle = 180 - self.angle

        if self.x + self.radius >= screenWidth and self.angle >= 270 and self.angle <= 360:
            self.angle = 180 + (360 - self.angle)

        #For the left wall and changes angle
        if self.x - self.radius <= 0 and self.angle >= 90 and self.angle <= 180:
            self.angle = 180 - self.angle 

        if self.x - self.radius <= 0 and self.angle >= 180 and self.angle <= 270:
            self.angle = 360 -(self.angle - 180)

        #For the bottom wall and changes angle
        if self.y + self.radius >= screenHeight and self.angle <= 359 and self.angle >= 270:
            self.angle = 360 - self.angle

        if self.y + self.radius >= screenHeight and self.angle >= 180 and self.angle <= 270:
            self.angle = 360 - self.angle
            
        #For the top wall and changes angle
        if self.y - self.radius <= 0 and self.angle >= 0 and self.angle <= 90:
            self.angle = 360 - self.angle
            
        if self.y - self.radius <= 0 and self.angle >= 90 and self.angle <= 180:
            self.angle = 360 - self.angle 
            
    #Checks Collision between the self ball and and incoming ball
    def checkCollision(self,incomingBallX,incomingBallY,incomingBallRadius):
        #Declares local variable
        collisionOccurred = False
        #If both the x values and y values overlap..
        if (self.radius + incomingBallRadius) > (abs(self.x - incomingBallX)) and (self.radius + incomingBallRadius) > (abs(self.y - incomingBallY)):
            collisionOccurred = True
        #Returns result
        return collisionOccurred

     #For movement
    def move(self):
        #Updates X and Y Values (using cosine and sine)
        #Multiples value by ballSpeed for visibility
        self.x = self.x +(math.cos(math.radians(self.angle))) * ballSpeed
        self.y = self.y -(math.sin(math.radians(self.angle))) * ballSpeed

        #Realigns X or Y if the ball will appear off the screen
        if self.x + self.radius > screenWidth:
            self.x = screenWidth - self.radius

        if self.y + self.radius > screenHeight:
            self.y = screenHeight - self.radius

        if self.x - self.radius < 0:
            self.x = self.radius

        if self.y - self.radius < 0:
            self.y = self.radius

        #If the ball collided with the wall, calls the changeAngle method
        if self.x + self.radius >= 500 or self.x - self.radius <= 0:
            self.changeAngle()
 
        if self.y + self.radius >= 500 or self.y - self.radius <= 0:
            self.changeAngle()

    #Displays the ball
    def display(self):

        pygame.draw.circle(screen,self.colour,(int(self.x),int(self.y)),self.radius, thickness)

#Program
while program:
    #For the setUp Screen
    while setUpScreen:

        #Sets up text
        setUpScreenText = titleFont.render("2,3,4 Balls Wanted?" ,True,colourText)
        screen.blit(setUpScreenText,(int(textX),int(textY)))
        pygame.display.update()

        #Forces user to input value
        while ballAmount == 0:
            #For a pygame event
            for event in pygame.event.get():
                #If its quit
                if event.type == pygame.QUIT:
                    #Quit loop
                    program = False
                #If there is a keydown
                elif event.type == pygame.KEYDOWN:
                    #If its 2 or 3 or 4, updates ballAmount move to next code
                    if event.key == pygame.K_2:
                        ballAmount = 2

                    elif event.key == pygame.K_3:
                        ballAmount = 3

                    elif event.key == pygame.K_4:
                        ballAmount = 4
        #for every ball
        for i in range(ballAmount):
            #Provide random values for Radius,X,Y and Angle, colour is semi predetermined
            randomRadius = random.randint(minRadius,maxRadius)
            randomX = random.randint(minX + randomRadius,maxX - randomRadius)
            randomY = random.randint(minY + randomRadius,maxY - randomRadius)
            randomAngle = random.randint(0,359)
            ballColour = ballColours[i]
            #Execute code 
            exec(f'ball{i+1} = BouncingBall(randomX,randomY,randomRadius,randomAngle,ballColour)')
        #Opens current loop and opens new loop    
        setUpScreen = False
        bouncingScreen = True
          
    #For second loop..
    while bouncingScreen:
        #Reset screen
       screen.fill(white)
       #For every ball, moves and displays the,
       for i in range(ballAmount):
           exec(f'ball{i+1}.move()')
           exec(f'ball{i+1}.display()')
       #Depending on ballAmount, checks collision between all balls
       #If collisionOccurred, updates variable
       if ballAmount >= 2:
           Collision12 = ball2.checkCollision(ball1.x,ball1.y,ball1.radius)

           if Collision12 == True:
               collisionOccurred = True

           if ballAmount >= 3:
               Collision13 = ball3.checkCollision(ball1.x,ball1.y,ball1.radius)
               Collision23 = ball3.checkCollision(ball2.x,ball2.y,ball2.radius)

               if Collision13 == True or Collision23 == True:
                   collisionOccurred = True

               if ballAmount >= 4:
                   Collision14 = ball4.checkCollision(ball1.x,ball1.y,ball1.radius)
                   Collision24 = ball4.checkCollision(ball2.x,ball2.y,ball2.radius)    
                   Collision34 = ball4.checkCollision(ball3.x,ball3.y,ball3.radius) 
       
                   if Collision14 == True or Collision24 == True or Collision34 == True:
                       collisionOccurred = True
                       
    # If a Collision occured, prints statement and close current loop and opens new loop
       if collisionOccurred == True:
           bouncingScreen = False
           finalScreen = True
           print("Collision")
#       #Updates screen and waits a second
       pygame.display.update()
       time.sleep(1)
    #On the final loop..
    while finalScreen:
        #Makes screen white and displays text
        screen.fill(white)
        finalScreenText = titleFont.render("The Two Balls Collided" ,True, colourText)
        screen.blit(finalScreenText, (int(textX),int(textY)))
        pygame.display.update()
 
  
pygame.QUIT #Quits Pygame
sys.exit()
 

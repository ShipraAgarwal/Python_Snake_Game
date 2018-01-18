# Snake Game!

import pygame
import sys     # contains exit() function
import random  # to start snack from a random position
import time    #to use sleep() n all

#all above 4 lines can be replaced by a single line as follows :
# import pygame, sys, random, time
#------------------------------------------------------------------------------------------------------------------------

#function for changing direction.
def change(old, new):
	if old == 'Right':
		if new == 'Right' or new == 'Down':
			return 'Down'
		else:
			return 'Up'
	elif old == 'Left':
		if new == 'Left' or new == 'Down':
			return 'Down'
		else:
			return 'Up'
	elif old == 'Up':
		if new == 'Left':
			return 'Left'
		elif new == 'Right':
			return 'Right'
		else:
			return old
	elif old == 'Down':
		if new == 'Left':
			return 'Left'
		elif new == 'Right':
			return 'Right'
		else:
			return old
#_________________________________________________________________________________________________________________________		

# Body Movement Function
def snake(direction):
	if direction == 'Right':
		snakeBody.insert(0,list([snakeBody[0][0] + 10,snakeBody[0][1]]))
	elif direction == 'Left':
		snakeBody.insert(0,list([snakeBody[0][0] - 10,snakeBody[0][1]]))
		
	elif direction == 'Up':
		snakeBody.insert(0,list([snakeBody[0][0],snakeBody[0][1] - 10]))
		
	elif direction == 'Down':
		snakeBody.insert(0,list([snakeBody[0][0],snakeBody[0][1] + 10]))
	
#-------------------------------------------------------------------------------------------------------------------------
# Display Score
def text_objects(score, font):
    textSurface = font.render(score, True, black)
    return textSurface, textSurface.get_rect()

def score_board(score):
	largeText = pygame.font.Font('freesansbold.ttf',20)
	TextSurf,TextRect = text_objects('Score:'+score, largeText)
	TextRect.center = (630,20)
	playSurface.blit(TextSurf, TextRect)

#-------------------------------------------------------------------------------------------------------------------------

def game_over():
	pygame.font.init()
	largeText = pygame.font.Font('freesansbold.ttf',20)
	TextSurf1,TextRect1 = text_objects("Snake Is Dead", largeText)
	TextSurf2,TextRect2 = text_objects("Do you want to play again?", largeText)
	TextSurf3,TextRect3 = text_objects("Press Left_arraow to Quit or Right_arrow to Continue", largeText)
	TextRect1.center = (750/2,460/2)
	TextRect2.center = ((750/2),(460/2)+25)
	TextRect3.center = ((750/2),(460/2)+50)
	playSurface.fill(white)
	playSurface.blit(TextSurf1, TextRect1)
	playSurface.blit(TextSurf2, TextRect2)
	playSurface.blit(TextSurf3, TextRect3)
	
	pygame.display.flip()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					return 'y'
				elif event.key == pygame.K_LEFT:
					return 'n'
			
	
#-------------------------------------------------------------------------------------------------------------------------

#initialize pygame and check for initializing errors
check_errors = pygame.init()    
if check_errors[1] > 0:
    print("(!)we are having {0} initializing errors, exiting.....".format(check_errors[1]))
    sys.exit()      
else:
    print("(+) PyGame successfully initialized!")


# Create a Playing Surface
playSurface = pygame.display.set_mode((750 , 460)) # here 750 is width and 460 is height of the game window
pygame.display.set_caption('Snake Game!')          #changing the header of game window(default is "pygame window"...

# Set Colours
red = pygame.Color(255,0,0) #Game Over
blue = pygame.Color(0,0,255) # Food 
green = pygame.Color(0,255,0) # Snake
black = pygame.Color(0,0,0) #Score
white = pygame.Color(255,255,255) #Background

#important variables
foodPos = [random.randrange(1,75)*10,random.randrange(1,46)*10]
snakeBody = [[100,50], [90,50], [80,50]]
direction = 'Right'
ate = 'T'
score = 0
Exit = False
temp = ''
fpsController = pygame.time.Clock()




############################# Main Logic(Event Handeling and Drawing) ######################################
while True:
	
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				direction = change(direction,'Left') 
			elif event.key == pygame.K_RIGHT:
				direction = change(direction,'Right') 
			elif event.key == pygame.K_UP:
				direction = change(direction,'Up')
			elif event.key == pygame.K_DOWN:
				direction = change(direction,'Down') 
	snake(direction)
	if foodPos[0] == snakeBody[0][0] and foodPos[1] == snakeBody[0][1]:
		ate = 'F'
		score += 1
		
	else:
		snakeBody.pop()
	
	if ate == 'F':
		foodPos = [random.randrange(1,75)*10,random.randrange(1,46)*10]
		ate = 'T'
		
	
	#Change Background Color
	playSurface.fill(white)
	
	# drawing Snake Body
	for i in snakeBody:
		pygame.draw.circle(playSurface, green, [i[0], i[1]], 5)	
		
	score_board(str(score));
	
	if snakeBody[0][0] < 6 or snakeBody[0][1] < 6:
		Exit = True
		
	if snakeBody[0][0] > 746 or snakeBody[0][1] > 456:
		Exit = True
	# Drawing Snake Food
	pygame.draw.circle(playSurface, blue, [foodPos[0], foodPos[1]], 5)
	if Exit:
		
		temp = game_over()
		if temp == 'y':
			snakeBody = [[100,50], [90,50], [80,50]]
			direction = 'Right'
			Exit = False
		elif temp == 'n':
			pygame.quit()
			quit()

	pygame.display.flip()
	fpsController.tick(10)
############################################################################################################		



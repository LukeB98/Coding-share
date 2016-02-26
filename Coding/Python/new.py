
import sys, pygame
pygame.init()

size = width, height = 620, 440
speed = [1, 2]
black = 100, 50, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.bmp")
ballrect = ball.get_rect()

while active:
	for event in pygame.event.get():
		action = pygame.key.get_pressed()
	
	elif action[pygame.K_w]:
	
	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()
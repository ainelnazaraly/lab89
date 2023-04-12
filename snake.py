import pygame
import time
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
done = True
v = 15
sc = 0

clock = pygame.time.Clock()

snpos = [100, 50]
snbody = [[100, 50], [90, 50], [80, 50], [70, 50]]
frpos = [random.randrange(1, (500//10)) * 10, random.randrange(1, (500//10)) * 10]
frap = True

def shsc(color, font, size):
	scfont = pygame.font.SysFont(font, size)
	scsurf = scfont.render("Score : " + str(sc), True, color)
	screct = scsurf.get_rect()
	screen.blit(scsurf, screct)
	
def game_over():
	gofont = pygame.font.SysFont("comicsans", 50)
	gosurf = gofont.render("Your Score is : " + str(sc), True, (255,0,0))
	gorect = gosurf.get_rect()
	gorect.midtop = (500/2, 500/4)
	screen.blit(gosurf, gorect)

direction = 'RIGHT'
change_to = direction

while done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				change_to = 'UP'
			if event.key == pygame.K_DOWN:
				change_to = 'DOWN'
			if event.key == pygame.K_LEFT:
				change_to = 'LEFT'
			if event.key == pygame.K_RIGHT:
				change_to = 'RIGHT'

	if change_to == 'UP' and direction != 'DOWN':
		direction = 'UP'
	if change_to == 'DOWN' and direction != 'UP':
		direction = 'DOWN'
	if change_to == 'LEFT' and direction != 'RIGHT':
		direction = 'LEFT'
	if change_to == 'RIGHT' and direction != 'LEFT':
		direction = 'RIGHT'

	if direction == 'UP':
		snpos[1] -= 10
	if direction == 'DOWN':
		snpos[1] += 10
	if direction == 'LEFT':
		snpos[0] -= 10
	if direction == 'RIGHT':
		snpos[0] += 10

	snbody.insert(0, list(snpos))
	if snpos[0] == frpos[0] and snpos[1] == frpos[1]:
		sc += 1
		frap = False
	else:
		snbody.pop()
		
	if not frap:
		frpos = [random.randrange(1, (500//10)) * 10, random.randrange(1, (500//10)) * 10]
		
	frap = True
	screen.fill((0,0,0))
	
	for pos in snbody:
		pygame.draw.rect(screen, (255,0,0), pygame.Rect(pos[0], pos[1], 10, 10))
	pygame.draw.rect(screen, (255,255,255), pygame.Rect(frpos[0], frpos[1], 10, 10))

	if snpos[0] < 0 or snpos[0] > 500-10: game_over()
	if snpos[1] < 0 or snpos[1] > 500-10: game_over()

	for block in snbody[1:]:
		if snpos[0] == block[0] and snpos[1] == block[1]: game_over()

	shsc((255,255,255), "comicsans", 20)
	pygame.display.flip()
	clock.tick(v)
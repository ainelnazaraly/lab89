import pygame
from pygame.locals import *
import random 
import sys
import time
from pygame import mixer 

pygame.init()
mixer.init()
screen=pygame.display.set_mode((400, 600))
screen.fill((255,255,255))
pygame.display.set_caption("racer")

height=600
width=400
speed=5
score=0
v=4

clock=pygame.time.Clock()
run=True

font=pygame.font.SysFont("Arial", 50)
small=pygame.font.SysFont("Arial", 20)
game_over=font.render("GAME OVER", True, (255, 0, 0))

bg=pygame.image.load('road.png')
go=pygame.image.load('bg.jpg')
go=pygame.transform.scale(go, (400, 600))
bg=pygame.transform.scale(bg, (400, 600))

list=[60, 150, 250, 340]

class coins(pygame.sprite.Sprite): 
    
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('coin.png')
        self.image=pygame.transform.scale(self.image, (40,40))
        self.rect=self.image.get_rect()
        self.rect.center=(random.choice(list), 0)
        #while pygame.sprite.spritecollideany(self, enemies):
            #self.rect.center = (random.choice(list), 0)
        

    def move(self): 
        self.rect.move_ip(0, v)
        
        if (self.rect.top > 600):
            self.kill()

class coins2(coins): 
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('coin2.png')
        self.image=pygame.transform.scale(self.image, (40,40))
        self.rect=self.image.get_rect()
        self.rect.center=(random.choice(list), 0)
        """while pygame.sprite.spritecollideany(self, enemies): 
            self.rect.center = (random.choice(list), 0) 
        while pygame.sprite.spritecollideany(self, coins): 
            self.rect.center = (random.choice(list), 0)"""

class player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('player.png')
        self.image=pygame.transform.scale(self.image, (50, 80))
        self.rect=self.image.get_rect()
        self.rect.center=(160, 520)
    
    def move(self): 
        pressed=pygame.key.get_pressed()
        if self.rect.left>0: 
            if pressed[K_LEFT]: 
                self.rect.move_ip(-5, 0)
        if self.rect.right<400: 
            if pressed[K_RIGHT]: 
                self.rect.move_ip(5, 0)
    

class Enemy1(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load('car.png')
        self.image=pygame.transform.scale(self.image, (50, 80))
        self.rect=self.image.get_rect()
        self.rect.center=((random.randint(40, width-40)), 0)
    
    def move(self): 
        global speed
        self.rect.move_ip(0, speed)
        if score>10: 
            speed=7
            
        if self.rect.bottom>600: 
            self.rect.top=0
            self.rect.center=((random.randint(30, 370)), 0)

P=player()
Y1=Enemy1()
C1=coins()
C2=coins2()

enemies=pygame.sprite.Group()
enemies.add(Y1)
Coi1=pygame.sprite.Group()
Coi1.add(C1)
Coi2=pygame.sprite.Group()
Coi2.add(C2)
all_spr=pygame.sprite.Group()
all_spr.add(P)
all_spr.add(Y1)
all_spr.add(C1)
all_spr.add(C2)


#incr=pygame.USEREVENT+1 #unique ID since there 23 pre defines ids we create unique one 
#pygame.time.set_timer(incr, 3000)

while run: 
    for event in pygame.event.get(): 
        if event.type==pygame.QUIT: 
            pygame.quit()
            sys.exit()

    screen.blit(bg, (0,0))
 
    
    
    if pygame.sprite.spritecollideany(P, Coi1):
        score+=1
        pygame.mixer.Sound('bonus.wav').play()
        C1.rect.top = 0
        C1.rect.center = (random.choice(list), 0)

    if pygame.sprite.spritecollideany(P, Coi2):
        score+=3
        pygame.mixer.Sound('bonus.wav').play()
        C2.rect.top = 0
        C2.rect.center = (random.choice(list), 0)


        
        

    if pygame.sprite.spritecollideany(P, enemies): 
           
            pygame.mixer.Sound('dead.wav').play()
            time.sleep(2)
            screen.blit(go, (0, 0))
            fscore=small.render(fscore, True, (255, 0, 0))
            screen.blit(fscore, (170, 500))
            pygame.mixer.Sound('done.wav').play()
            pygame.display.update()
            for bbys in enemies: 
                bbys.kill()
            time.sleep(2)
            pygame.quit()
            sys.exit()
      
    for entity in all_spr: 
        screen.blit(entity.image, entity.rect)
        entity.move()

    scores=small.render(str(score), True, (0, 0, 0))
    screen.blit(scores, (10, 10))
    fscore="score: "+str(score)    
    
    pygame.display.flip()
    clock.tick(60)
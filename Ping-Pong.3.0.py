from pygame import *
from random import randint
window = display.set_mode((700,500))
background = transform.scale(image.load('neon.jpg'),(700,500))
class GameSprite(sprite.Sprite):
    def __init__(self,hero,speed,x,y, length, width):
        super().__init__()
        self.image = transform.scale(image.load(hero),(length,width))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_s]:
            self.rect.y += 10
        if keys[K_w]:
            self.rect.y -= 10
    def dvig(self):
        keys = key.get_pressed()
        if keys[K_DOWN]:
            self.rect.y += 10
        if keys[K_UP]:
            self.rect.y -= 10
Palka1 = Player('Palka1.png',30, 10,20, 23, 90)
Palka2 = Player('Palka1.png',30, 670,400, 23, 90)
ball = Player('miach-4.png',30, 30, 0, 70, 70)
clock = time.Clock()
font.init()
font = font.SysFont('Arial', 30)
speedx = 10
speedy = 10
FPS = 60
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        winer = font.render('Player_2 lose!', True, (8, 232, 222))
        loser = font.render('Player_1 lose!', True, (8, 232, 222))
        Palka1.reset()
        Palka1.update()
        Palka2.reset()
        Palka2.dvig()
        ball.reset()
        ball.rect.y += speedy
        ball.rect.x += speedx
        if ball.rect.y == 0 or ball.rect.y == 430:
            speedy = speedy * -1
        if sprite.collide_rect(ball, Palka2):
            speedx = speedx * -1
        if sprite.collide_rect(ball, Palka1):
            speedx = speedx * -1
        if ball.rect.x == -80:
            finish = True
            window.blit(loser, (280, 240)) 
        if ball.rect.x == 700:
            finish = True
            window.blit(winer, (280, 240)) 

        
        clock.tick(FPS)
        display.update()
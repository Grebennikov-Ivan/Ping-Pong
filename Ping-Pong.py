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
        if keys[K_d]:
            self.rect.x += 10
        if keys[K_a]:
            self.rect.x -= 10

clock = time.Clock()
FPS = 60
finish = True
while finish:
    for e in event.get():
        if e.type == QUIT:
            finish = False
    window.blit(background,(0,0))
    clock.tick(FPS)
    display.update()
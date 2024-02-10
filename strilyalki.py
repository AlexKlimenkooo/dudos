import pygame
from pygame import*
import random
pygame.init()

x = 1000
y = 700
window = display.set_mode((x, y))
display.set_caption("Strilyaki")
background = transform.scale(image.load("fon_fortnite.png"), (x, y))
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, x, y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x, y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed [K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed [K_d] and self.rect.x < 930:
            self.rect.x += self.speed
pomp = Player("pomp-removebg-preview.png",450, 480, 70, 202, 5)


i = 0
class Enemy(GameSprite):
    def reset(self):
        self.rect.y = 0
        self.rect.x = random.randint(0, 900)  # Генеруємо нове випадкове положення по осі X

    def update(self):
        self.rect.y += self.speed  
        if self.rect.y > y:
            self.reset()



for i in range(5):
    x1 = random.randint(0, 1000) 
    x2 = random.randint(0, 1000) 
    x3 = random.randint(0, 1000) 
    x4 = random.randint(0, 1000) 
    x5 = random.randint(0, 1000) 
    burya_pers1 = Enemy("burya__pers-removebg-preview.png", x1, y, 165, 145, 2)
    burya_pers2 = Enemy("burya__pers-removebg-preview.png", x2, y, 165, 145, 2)
    burya_pers3 = Enemy("burya__pers-removebg-preview.png", x3, y, 165, 145, 2)
    burya_pers4 = Enemy("burya__pers-removebg-preview.png", x4, y, 165, 145, 2)
    burya_pers5 = Enemy("burya__pers-removebg-preview.png", x5, y, 165, 145, 2)
    monsters = sprite.Group()
    monsters.add(burya_pers1, burya_pers2, burya_pers3, burya_pers4, burya_pers5)




mixer.init()
mixer.music.load("01. Battle Royal (Guitar Theme).mp3")
mixer.music.play()  
finish = False
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        pomp.reset()
        pomp.update()
        monsters.update()
        monsters.draw(window) 

    display.update()
    clock.tick(FPS)
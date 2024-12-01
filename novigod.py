from pygame import *
from random import *
clock = time.Clock()
window = display.set_mode((700, 500))
background = transform.scale(image.load('izba.png'), (700, 500))

rect [(177, 156), (), (),]
177 156
379 282
-18 241
251 42
585 250

class gamesprite(sprite.Sprite):
    def __init__(self, speed, pimage, rect_x, rect_y, size_x, size_y):
        super().__init__()
        self.speed = speed

        self.image = transform.scale(image.load(pimage), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
# class enemy(gamesprite):
#     def update(self):

x = 0
y = 0
sprite_kiianka = gamesprite(10, 'kiianka.png', x, y, 80, 100)
risovat = 0
game = True 
while game:
    window.blit(background, (0,0))
    for i in event.get():
        if i.type == QUIT:
            game = False
            keys_pressed = key.get_pressed()
        if i.type == MOUSEBUTTONDOWN and i.button == 1:
            sprite_kiianka.rect.x, sprite_kiianka.rect.y = i.pos[0] - 50, i.pos[1] - 50
            risovat = 10
            print(sprite_kiianka.rect.x, sprite_kiianka.rect.y)
    if risovat:
        sprite_kiianka.reset()
        risovat -= 1

    display.update()
    clock.tick(60)

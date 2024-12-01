from pygame import *
from random import *
x_ball = randint(1, 2)
y_ball = randint(1, 2)
player_1_score = 0
player_2_score = 0
power_ball = 0

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

class player(gamesprite):
    def update_player_2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def update_player_1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed

class ball(gamesprite):
    def update(self):
        global y_ball 
        global x_ball 
        global player_2_score
        global player_1_score
        global power_ball
        if x_ball == 1:
            self.rect.x += self.speed
        elif x_ball == 2:
            self.rect.x -= self.speed
        if y_ball == 1:
            self.rect.y += self.speed
        elif y_ball == 2:
            self.rect.y -= self.speed
        if self.rect.y >= 475:
            y_ball = 2
        elif self.rect.y <= 25:
            y_ball = 1
        if sprite.collide_rect(self, sprite_platform2):
            x_ball = 1
            power_ball += 1
        if sprite.collide_rect(self, sprite_platform1):
            x_ball = 2
            power_ball += 1
        if self.rect.x <= 0:
            x_ball = randint(1, 2)
            self.rect.x = 350
            self.rect.y = 250
            player_2_score += 1
        if self.rect.x >= 700:
            x_ball = randint(1, 2)
            self.rect.x = 350
            self.rect.y = 250
            player_1_score += 1
    def speed_up(self):
        global power_ball
        if power_ball >= 10:
            self.speed += 1
            power_ball = 0
    def update_1_player_game(self):
        global y_ball 
        global x_ball 
        global player_2_score
        global power_ball
        if x_ball == 1:
            self.rect.x += self.speed
        elif x_ball == 2:
            self.rect.x -= self.speed
        if y_ball == 1:
            self.rect.y += self.speed
        elif y_ball == 2:
            self.rect.y -= self.speed
        if self.rect.y >= 475:
            y_ball = 2
        elif self.rect.y <= 25:
            y_ball = 1
        if sprite.collide_rect(self, sprite_platform2):
            x_ball = 1
            power_ball += 1
        if self.rect.x == 700:
            x_ball = 2
            power_ball += 1
        if self.rect.x <= 0:
            x_ball = randint(1, 2)
            self.rect.x = 350
            self.rect.y = 250
            player_2_score += 1
        if self.rect.x >= 700:
            x_ball = randint(1, 2)

        


#sprite_platform
                    





window = display.set_mode((700, 500))
background = transform.scale(image.load('i.png'), (700, 500))

sprite_platform2 = player(10, 'platform.png', 0, 250, 80, 100)
sprite_platform1 = player(10, 'platform2.png', 625, 250, 80, 100)
sprite_ball = ball(5, ('i(1).png'), 350, 250, 25, 25)
font.init()
font = font.SysFont(None, 35)

win_2 = font.render('Игрок 2 Выиграл!', True,  (255, 255, 255 ))
win_1 = font.render('Игрок 1 Выиграл!', True,  (255, 255, 255 ))
win1 = font.render('Ты проиграл', True,  (255, 255, 255 ))
restart = font.render('Нажми q чтобы начать заново', True,  (25, 25, 25))
input_player = font.render('Выбери кол-во игроков на клавиатуре! (1,2)', True,  (0, 0, 0))
window.blit(background, (0, 0))


game = True
finish = False
clock = time.Clock()
game_mode = 0
start = False
while game:
    
    for i in event.get():
        if i.type == QUIT:
            game = False
        keys_pressed = key.get_pressed()
        if keys_pressed[K_q] and finish:
            finish = False
            player_1_score = 0
            player_2_score = 0
        if keys_pressed[K_2] and not start:
            game_mode = 2
            start = True
        elif keys_pressed[K_1] and not start:
            game_mode = 1
            start = True

    if not start:
        window.blit(input_player, (100, 250))
    if finish != True and start and game_mode==2:
        window.blit(background, (0, 0))
        sprite_platform2.reset()
        sprite_platform1.reset()
        sprite_platform2.update_player_2()
        sprite_platform1.update_player_1()
        sprite_ball.reset()
        sprite_ball.update()
        sprite_ball.speed_up()
        player_2_score_print = font.render('Пропущено:' + str(player_2_score), True,  (255, 255, 255 )) 
        window.blit(player_2_score_print, (0, 0))
        player_1_score_print = font.render('Пропущено:' + str(player_1_score), True,  (255, 215, 0 ))
        window.blit(player_1_score_print, (525, 0))
        if player_1_score >= 10:
            window.blit(win_2, (250, 250))
            window.blit(restart, (200, 200))
            finish = True
        elif player_2_score >=10:
            window.blit(win_1, (250, 250))
            window.blit(restart, (200, 200))
            ball.speed = 5
            finish = True
    if finish != True and start and game_mode==1:
        window.blit(background, (0, 0))
        sprite_platform2.reset()
        sprite_platform2.update_player_2()
        sprite_ball.reset()
        sprite_ball.update_1_player_game()
        sprite_ball.speed_up()
        player_2_score_print = font.render('Пропущено:' + str(player_2_score), True,  (255, 255, 255 )) 
        window.blit(player_2_score_print, (0, 0))
        if player_2_score >=10:
            window.blit(win1, (250, 250))
            window.blit(restart, (200, 200))
            ball.speed = 5
            finish = True
    display.update()
    clock.tick(60)
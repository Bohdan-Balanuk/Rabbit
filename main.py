from pygame import*
from time import time as time1
from time import sleep
from random import randint 
import sys

init()
clock = time.Clock()


window = display.set_mode((1150, 750))
display.set_caption('Rabbit')
background = transform.scale(image.load("Rabbit\Objects/Background.png"), (1150, 750))
window.blit(background, (0,0))

class GameCard():

    def __init__(self, x, y, width, height, color = None):
        self.rect = Rect(x, y, width, height)
        self.fill_color = color
        self.color = color

    def frame(self, window, color= (0, 0, 0), thinkness = 5):
        draw.rect(window, color, self.rect, thinkness)

    def draw_rect(self, window):
        draw.rect(window, self.fill_color, self.rect)
        self.frame()

    def set_text(self, text, fsize = 50, text_color=(0,0,0)):
        self.image = font.SysFont("Arial", fsize).render(text, True, self.color)

    def draw_text(self, shift_x=5, shift_y=55):
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

    def draw_info(self, window):
        draw.rect(window, self.fill_color, self.rect)
        window.blit(self.image,(self.rect.x, self.rect.y))

class Rabbit():
    def __init__(self, filename, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.image = transform.scale(image.load(filename), (100, 100))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw_player(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
    def move_Up(self):
        self.rect.y -= 3
    
    def move_Down(self):
        self.rect.y += 3

    def move_Left(self):
        self.rect.x -= 3
    
    def move_Right(self):
        self.rect.x += 3

    def change_filename(self, new_filename):
        self.image = transform.scale(image.load(new_filename), (100, 100))

class Carrot():
    def __init__(self, filename, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        self.image = transform.scale(image.load(filename), (70, 90))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def colliderect(self, rect):
        return self.rect.colliderect(rect)
    
    def move(self, rect):
        self.rect.x = randint(0, 1000)
        self.rect.y = randint(430, 650)
        if self.colliderect(rect):
            self.rect.x = randint(0, 1000)
            self.rect.y = randint(430, 650)

    def draw_carrot(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

game = True

player_right = False
player_left = False
player_up = False
player_down = False
amount = 0
time_stats = 0

filename = "Rabbit\Objects/RabbitR.png"

player = Rabbit(filename, 50, 550, 100, 100)
carrot = Carrot("Rabbit\Objects/Carrot.png", randint(0, 1000), randint(430, 650), 70, 90)

stats_text = GameCard(0, -20, 100, 100, (0, 0, 255))
stats_text.set_text("Зібрано:")

stats = GameCard(170, -20, 100, 100, (0, 0, 255))
stats.set_text(str(amount))

while game:
    time_stats += time1()
    time_stats = int(time_stats)

    window.blit(background, (0,0))

    for ev in event.get():
        if ev.type == QUIT:
            finish_image = font.SysFont("Goudy Stout", 50).render("GOOD BYE", True, (255, 0, 255))
            game = False
        
        if ev.type == KEYDOWN:
            if ev.key == K_RIGHT:
                player_right = True
                filename = "Rabbit\Objects/RabbitR.png"
            if ev.key == K_LEFT:
                player_left = True
                filename = "Rabbit\Objects/RabbitL.png"

            if ev.key == K_UP:
                player_up = True
            if ev.key == K_DOWN:
                player_down = True
        
        if ev.type == KEYUP:
            if ev.key == K_RIGHT:
                player_right = False
            if ev.key == K_LEFT:
                player_left = False

            if ev.key == K_UP:
                player_up = False
            if ev.key == K_DOWN:
                player_down = False

    if player_right and player.rect.x <= 1050:
        player.move_Right()
    if player_left and player.rect.x >= 0:
        player.move_Left()
    if player_up and player.rect.y >= 430:
        player.move_Up()
    if player_down and player.rect.y <= 650:
        player.move_Down()

    if carrot.colliderect(player):
        carrot.move(player)
        amount += 1
        stats.set_text(str(amount))

    if amount == 15:
        finish_image = font.SysFont("Goudy Stout", 50).render("YOU WIN", True, (255, 0, 255))
        game = False

    player.change_filename(filename)
    player.draw_player()
    carrot.draw_carrot()

    stats_text.draw_text()
    stats.draw_text()

    display.update()
    clock.tick(120)

game = True
counter = 0
window.blit(finish_image,(window.get_width() / 2 - 220, window.get_height() / 2 - 70))
display.update()
while counter != 15*60 and game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    counter += 1
    clock.tick(120)
import pygame
from dino_runner.utils.constants import HAMMER_LIST, SCREEN_WIDTH
from pygame import Surface
from pygame.sprite import Sprite

class Hammerfly(Sprite):
    POS_X=80
    POS_Y = 310
    def __init__(self):
        self.image_hommer = HAMMER_LIST[0]
        self.rect_hommer = self.image_hommer.get_rect()
        self.rect_hommer.x = SCREEN_WIDTH
        self.rect_hommer.y = self.POS_Y
        self.time = 0
        
    
    def update(self,game_speed):
        if self.time >= 20:
           self.time = 0
        self.image_hommer = HAMMER_LIST[self.time// 5]
        self.time += 1
        self.rect_hommer.x += game_speed
        if self.rect_hommer.x < -self.rect_hommer.width:
            self.list_hommmer.pop()
        
    def draw(self,screen:Surface):
        screen.blit(self.image_hommer, (self.rect_hommer.x, self.rect_hommer.y))
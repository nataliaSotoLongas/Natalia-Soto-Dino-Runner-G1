import pygame
from dino_runner.utils.constants import HAMMER_LIST
from pygame import Surface
from pygame.sprite import Sprite

class Hammerfly(Sprite):
    POS_X=80
    POS_Y = 310
    def __init__(self):
        self.image_hommer = HAMMER_LIST[0]
        self.rect_hommer = self.image_hommer.get_rect()
        self.rect_hommer.x = self.POS_X
        self.rect_hommer.y = self.POS_Y
        self.list_hommmer = []
        self.time = 0
        
    
    def update(self,game_speed):
        if self.time >= 20:
           self.time = 0
        self.image_hommer = HAMMER_LIST[self.time// 5]
        self.time += 1
        if len(self.list_hommmer) == 1:
            self.rect_hommer.x += game_speed
            if self.rect_hommer.x >= 1100:
                self.list_hommmer.pop(0)
                self.rect_hommer.x = self.POS_X
    
    def add(self):
        if len(self.list_hommmer) == 0: 
            self.list_hommmer.append(self.image_hommer)
        
    def draw(self,screen:Surface):
        if len(self.list_hommmer) == 1:
            screen.blit(self.image_hommer, (self.rect_hommer.x, self.rect_hommer.y))
        else:
            pass
        
    def reset(self):
        self.list_hommmer = []
import pygame
from pygame import Surface
from pygame.sprite import Sprite
from dino_runner.utils.constants import RUNNING , JUMPING , DUCKING

DINO_JUMPING = "JUMPING"
DINO_RUNNING = "RUNNING"
DINO_DUCKING = "DUCKING"

class Dinosaur(Sprite): 
    POS_X=80
    POS_Y = 310
    JUMPING_VELOCITY = 8.5
    
    def __init__(self):
        self.image = RUNNING[0]
        self.step = 0
        self.action = DINO_RUNNING 
        self.jump_velocity = self.JUMPING_VELOCITY
        
    def position(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
          
    def update(self, user_input):
        if self.action == DINO_RUNNING :
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()
            
        #Saltar     
        if self.action !=  DINO_JUMPING:
            if user_input[pygame.K_UP]:
                pygame.mixer.music.load('dino_runner/components/music/jump.mp3')
                pygame.mixer.music.play()
                self.action =   DINO_JUMPING
            else:
                self.action = DINO_RUNNING 
                
        #bajar       
        if self.action !=  DINO_JUMPING:
            if user_input[pygame.K_DOWN]:
                self.action =   DINO_DUCKING
            else:
                self.action = DINO_RUNNING 
                
        if self.step >= 10:
           self.step = 0
    def run(self):
        self.image = RUNNING[self.step // 5]
        self.position()
        self.step += 1
        
    def jump(self):
        #jump
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMPING_VELOCITY:
            self.action = DINO_RUNNING
            self.rect.y = self.POS_Y
            self.jump_velocity = self.JUMPING_VELOCITY
            
    def duck(self):
        self.image = DUCKING[self.step // 5]
        self.rect.y = 340
        self.step += 1
        
    def draw(self, screen:Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
   
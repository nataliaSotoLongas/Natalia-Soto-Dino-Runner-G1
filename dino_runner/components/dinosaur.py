import pygame
from pygame import Surface
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING , JUMPING , DUCKING ,DEAD ,DEFAULT_TYPE, SHIELD_TYPE, RUNNING_SHIELD, JUMPING_SHIELD, DUCKING_SHIELD

DINO_JUMPING = "JUMPING"
DINO_RUNNING = "RUNNING"
DINO_DUCKING = "DUCKING"
IMG_RUNNING = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE:RUNNING_SHIELD}
IMG_JUMPING = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE:JUMPING_SHIELD}
IMG_DUCKING = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE:DUCKING_SHIELD}

class Dinosaur(Sprite): 
    POS_X=80
    POS_Y = 310
    POS_Y_DUCK = 340
    JUMPING_VELOCITY = 8.5
    
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.update_image(IMG_DUCKING[self.type][0])
        self.image = RUNNING[0]
        self.position()
        self.step = 0
        self.action = DINO_RUNNING 
        self.jump_velocity = self.JUMPING_VELOCITY
        self.power_up_time = 0
        self.time_to_show = 0
        
    def position(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
       
          
    def update(self, user_input):
        if self.action == DINO_RUNNING:
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
            elif user_input[pygame.K_DOWN]:
                self.action =   DINO_DUCKING
            else:
                self.action = DINO_RUNNING 
                       
        if self.step >= 10:
           self.step = 0
           
    def run(self):
        self.update_image(IMG_RUNNING[self.type][self.step // 5]) 
        self.position()
        self.step += 1
        
    def jump(self):
        #jump
        pos_y =  self.rect.y - self.jump_velocity * 4
        self.update_image(IMG_JUMPING[self.type], pos_y=pos_y)
        self.jump_velocity -= 0.8
        if self.jump_velocity < -self.JUMPING_VELOCITY:
            self.action = DINO_RUNNING
            self.rect.y = self.POS_Y
            self.jump_velocity = self.JUMPING_VELOCITY
        
            
    def duck(self):
        #bajar
        self.update_image(IMG_DUCKING[self.type][self.step // 5])
        self.position()
        self.rect.y = self.POS_Y_DUCK
        self.step += 1
        
    def draw(self, screen:Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
    def update_image(self, image:pygame.Surface , pos_y = None, pos_x = None,on_death = False):
        self.image = image
        if not on_death:
            self.rect =  image.get_rect()
            self.rect.x = pos_x or self.POS_X
            self.rect.y =  pos_y or self.POS_Y
          
    def dead(self):
        #TRAER LA IMAGEN DE DEAD
        self.image=DEAD
        pygame.mixer.music.load('dino_runner/components/music/dead.mp3')
        pygame.mixer.music.play()
    
    def on_pick_power_up(self, power_up):
        self.type =  power_up.type
        
    
    def draw_power_up(self, message, colors):
        if self.type != DEFAULT_TYPE:
            self.time_to_show += 1
            pygame.time.delay(20)
            if self.time_to_show <= 100:
                if colors >= 200:
                    message(f"{self.type.capitalize()} enabled for {self.time_to_show} seconds", 900, 80,(255,255,255),22 )
                else:
                    message(f"{self.type.capitalize()} enabled for {self.time_to_show} seconds", 900, 80,(0,0,0) ,22)
                if self.time_to_show >= 100:
                    self.time_to_show = 0
                    self.type = DEFAULT_TYPE
    
   
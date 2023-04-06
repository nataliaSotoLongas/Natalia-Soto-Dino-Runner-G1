from pygame.sprite import Sprite
import pygame

class Score(Sprite):
    def __init__(self):
        self.score = 0
    
    def update(self, game):
        self.score += 1 
        if self.score % 100 == 0:
            game.game_speed += 2
            
    #color para la letra del score        
    def draw(self,colors, message):
        if colors >= 200:
            message(f'Score: {self.score}', 1000, 50,(255,255,255),22 )
        else:
            message(f'Score: {self.score}', 1000, 50,(0,0,0) ,22)
            
    # Metodo para resetear tiempo    
    def reset(self):
        self.score = 0
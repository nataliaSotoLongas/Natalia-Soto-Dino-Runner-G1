from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.components.power_ups.shield import Shield
from dino_runner.utils.constants import DEFAULT_TYPE
import pygame
import random
class PowerUpManager():
    def __init__(self):
        self.power_ups : list[PowerUp] = []
        self.when_appers = 0
        
    def generete_power_ups(self, score):
        if not self.power_ups and score == self.when_appers:
            self.when_appers += random.randint(300,400)
            self.power_ups.append(Shield())
        
            
    def update(self, game_speed, score , player):
        self.generete_power_ups(score)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if power_up.rect.colliderect(player.rect):
                power_up.start_time = pygame.time.get_ticks()
                player.on_pick_power_up(power_up)
                self.power_ups.remove(power_up)
            
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
            
    def reset(self, player):
        self.power_ups = []
        self.when_appers = random.randint(200,300)
        player.type = DEFAULT_TYPE 
        
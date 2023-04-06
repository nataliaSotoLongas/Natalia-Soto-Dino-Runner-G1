from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer
from dino_runner.components.power_ups.heart import Heart
from dino_runner.utils.constants import DEFAULT_TYPE
import pygame
import random
class PowerUpManager():
    POWER_SHIELD = 5
    POWER_HEART = 5
    POWER_HAMMER = 5
    def __init__(self):
        self.power_ups : list[PowerUp] = []
        self.when_appers = 0
        
    def generete_power_ups(self, player):
        if not self.power_ups and self.POWER_SHIELD == random.randint(0,300) and player.type == DEFAULT_TYPE:
            self.power_ups.append(Shield())
        elif  not self.power_ups and self.POWER_HEART == random.randint(0,300) and player.type == DEFAULT_TYPE: # los agrega a la lista 
            self.power_ups.append(Heart())
        elif not self.power_ups and self.POWER_HAMMER == random.randint(0,300) and player.type == DEFAULT_TYPE: # los agrega a la lista 
            self.power_ups.append(Hammer())
            
    def update(self, game_speed, player):
        self.generete_power_ups( player)
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
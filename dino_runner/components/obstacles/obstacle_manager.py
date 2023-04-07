import pygame
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.stone import Stone
from dino_runner.components.obstacles.birds import Bird
from dino_runner.components.power_ups.hammer_fly import Hammerfly

class ObstacleManager():
  OBSTACLE = [Cactus, Bird , Stone]
  def __init__(self):
    self.obstacles : list[Obstacle] = []
    self.hammer_fly = Hammerfly()
      
  def update(self, game, on_death):
    if not self.obstacles:
      obstacle = random.choice(self.OBSTACLE)
      self.obstacles.append(obstacle())
            
    for obstacle in self.obstacles:
      obstacle.update(game.game_speed, self.obstacles)
      if obstacle.rect.colliderect(game.player.rect):
        on_death(obstacle, self.obstacles) #busca, cual es el objeto cuando hay colision 
  
  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)
    
  def validate(self):
    for obstacle in self.obstacles:
      if self.hammer_fly.rect_hommer.colliderect(obstacle.rect):
        self.obstacles.remove(obstacle)
        print("yes")# remueve el obstaculo
      
  def reset(self):
    self.obstacles = []
      
 
import pygame
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.cactus import Cactus

class ObstacleManager():
  def __init__(self):
    self.obstacles : list[Obstacle] = []
      
  def update(self, game):
    if not self.obstacles:
      self.obstacles.append(Cactus())
            
    for obstacle in self.obstacles:
      obstacle.update(game.game_speed, self.obstacles)
      if obstacle.rect.colliderect(game.player.rect):
        pygame.time.delay(500)
        game.playing = False
  
  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)
      
 
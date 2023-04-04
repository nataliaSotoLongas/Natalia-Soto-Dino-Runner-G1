import pygame
import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.stone import Stone
from dino_runner.components.obstacles.birds import Bird

class ObstacleManager():
  def __init__(self):
    self.obstacles : list[Obstacle] = []
      
  def update(self, game):
    if not self.obstacles:
      random_obstacle = random.randint(0,1)
      if random_obstacle == 0:
        self.obstacles.append(Cactus())
      #elif random_obstacle == 1:
        #self.obstacles.append(Stone())
      else:
        self.obstacles.append(Bird())
            
    for obstacle in self.obstacles:
      obstacle.update(game.game_speed, self.obstacles)
      if obstacle.rect.colliderect(game.player.rect):
        pygame.time.delay(500)
        game.playing = False
  
  def draw(self, screen):
    for obstacle in self.obstacles:
      obstacle.draw(screen)
      
 
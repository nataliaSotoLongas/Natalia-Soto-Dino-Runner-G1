import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import  BIRD
class Bird(Obstacle):
  BIRD_HEIGHT =[260,210,160]
  def __init__(self):
    self.index = 0
    pos_y = self.BIRD_HEIGHT[random.randint(0,2)]
    self.image = BIRD[0]
    super().__init__( self.image, pos_y)
  
  #para que me dibuje el pajaro
  def draw(self, screen):
    if self.index >= 9:
     self.index = 0
     
    screen.blit(BIRD[self.index // 5], self.rect)
    self.index+=1 
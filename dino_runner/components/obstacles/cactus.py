import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class Cactus(Obstacle):
  cactus = {0:(LARGE_CACTUS,300),
            1:(SMALL_CACTUS,325)}
  def __init__(self):
    random_img = random.randint(0,1)# para definir si es large o small 
    self.tipo=self.cactus[random_img] #para defnir 
    self.image_posicion = self.tipo[0] # escoger la posicion se la imagen
    self.pos_y = self.tipo[1] # escoger la posicion  de y
    random_tipo = random.randint(0,2)# para escoger cual de las tres imagenes es
    self.image = self.image_posicion[random_tipo]
    super().__init__( self.image, pos_y=self.pos_y)# trae la imagen y la posicion 
    
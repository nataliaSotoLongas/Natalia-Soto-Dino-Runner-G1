import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import STONE

class Stone(Obstacle):
    STONE = [(STONE[0],310),(STONE[1],330),(STONE[2],350)]
    def __init__(self):
        image, pos_y = random.choice(self.STONE)
        super().__init__( image, pos_y)  
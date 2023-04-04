import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import STONE

class Stone(Obstacle):
    def __init__(self):
        random_stone = random.randint(0,2)
        self.image = STONE[random_stone]
        if random_stone == 0:
            self.image = STONE[0]
            pos_y = 310
        elif random_stone == 1:
            self.image = STONE[1]
            pos_y = 330
        elif random_stone == 2:
            self.image = STONE[2]
            pos_y = 350  
        super().__init__( self.image, pos_y)
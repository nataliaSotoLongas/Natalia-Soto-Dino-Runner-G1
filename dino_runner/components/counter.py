import pygame

class Counter ():
    def __init__ (self):
        self.count = 0
        
    def update(self): #para contar
        self.count += 1
    def reset(self): # para resetear el contador
        self.count = 0
    def set_count(self, value): 
        self.count = value
import pygame
import random
from dino_runner.components.power_ups.heart import Heart
from dino_runner.components.power_ups.hammer_fly import Hammerfly
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.score import Score
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, GAMEOVER, RESET , ICON_1 , SUN, MOON,STAR, SHIELD_TYPE, HAMMER_TYPE, HEART_TYPE, DEFAULT_TYPE, HEART


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.obstacle_manager = ObstacleManager() 
        self.clock = pygame.time.Clock()
        self.running = False
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.death_count = 0
        self.player = Dinosaur()
        self.score = Score()
        self.hammer_fly = Hammerfly()
        self.death = 0
        self.highest_score = 0 #Tiempo record 
        self.icon = ICON_1[0]
        self.step = 0
        self.colors = 0 # cambiar de color
        self.power_up_manager = PowerUpManager()
        self.life = []
        self.heart_x = 10
        self.posicion = []

    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_Menu()
        pygame.quit()
      
    #metodo para recetar el juego   
    def reset(self):
        self.obstacle_manager.reset()
        self.power_up_manager.reset(self.player)
        self.score.reset()
        self.player.POS_X = 80 #resetea la pocision en x
        self.game_speed = 20
        self.colors = 0
        self.hammer_fly.reset()
        
        
    def play(self):
        self.playing = True
        self.reset()# Metodo para recetear el juego
        while self.playing:
            self.events()
            self.update()
            self.draw()
        pygame.time.delay(1000)
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        self.user_input = pygame.key.get_pressed()
        self.player.update(self.user_input, self.hammer_fly, self.player)
        self.obstacle_manager.update(self, self.on_death)  
        self.score.update(self)
        self.hammer_fly.update(self.game_speed)
        self.power_up_manager.update(self.game_speed, self.player, self.on_powerd)
        
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255,255,255))
        self.black_While() # llamar el metodo para cambiar el color
        self.draw_background()
        #llamamos las imagenes
        self.draw_clouds()
        self.hammer_fly.draw(self.screen)
        #self.hammer_fly.draw_homer(self.screen)
        self.heart_generator_draw()
        self.player.draw(self.screen)
        self.player.draw_power_up(self.message,self.colors)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.colors,self.message) # dibujar el cambio de color
        self.power_up_manager.draw(self.screen) 
        pygame.display.update()
        pygame.display.flip()
        
    #metodo para cambiar el color
    def black_While(self):
        self.colors += 1
        if self.colors >= 200:
            self.screen.fill((0, 0, 0))
            self.screen.blit(MOON, (150, 20)) # Dibujar la luna
            self.star()
            if self.colors >= 400:
                self.colors = 0
        else:
            self.screen.fill((255,255,255))
            self.screen.blit(SUN, (500,10)) # Dibujar el sol
    
    def heart_generator_draw(self):
        for life in self.life: 
            self.heart_x = 10
            self.screen.blit(life, (150, self.heart_x))
            break
          
    #dibujar las imagenes
    def draw_clouds(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1020, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1070, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2030, self.y_pos_bg -300))
        
    def star(self):
        image_width = STAR.get_width() 
        self.screen.blit(STAR, (image_width + self.x_pos_bg +1520, self.y_pos_bg -250))
        self.screen.blit(STAR, (image_width + self.x_pos_bg +1870, self.y_pos_bg -350))
        self.screen.blit(STAR, (image_width + self.x_pos_bg +2400 , self.y_pos_bg -300))
    
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def on_death(self, obstcacle, obstacles):
        if self.player.type == SHIELD_TYPE:
            pass # seguir el codigo sin nunguna accion 
        elif self.player.type == HAMMER_TYPE:
            self.obstacle_manager.validate()
        elif self.player.type == HEART_TYPE:
            pass
        else:
            self.player.dead() #llamar la imagen
            pygame.time.delay(100) #al tocar el obstaculo 
            self.playing = False
            self.death_count +=1
            
    def on_powerd(self,power_up, power_ups):
        if HEART_TYPE == self.player.type:
            self.life.append(HEART)
            self.heart_generator_draw()
            self.type = DEFAULT_TYPE
        else:
            power_up.start_time = pygame.time.get_ticks()
            self.player.on_pick_power_up(power_up)
            power_ups.remove(power_up)
    
    #para hacer caminar el dinosaurio en el menu   
    def Icon_walk(self):
        if self.step >= 800:
            self.step = 0
        self.icon = ICON_1[self.step // 400]
        self.step += 1 
        
    #menu   
    def show_Menu(self):
        half_screen_height = SCREEN_HEIGHT //2
        half_screen_width = SCREEN_WIDTH //2
        self.screen.fill((225,225,225))
        if self.death_count >= 1:
            self.screen.blit(GAMEOVER, (half_screen_width -370, half_screen_height - 140,))
            self.screen.blit(RESET, (half_screen_width - 50, half_screen_height - 70,))
            self.update_highest_score() # definir el mayor puntaje
            self.message("Game over. Press any key to reset", half_screen_width, half_screen_height +50, (0,0,0),30)
            self.message(f"Your Score: {self.score.score}", half_screen_width, half_screen_height +85, (0,0,0),30)
            self.message(f"Highest Score: {self.highest_score}", half_screen_width,half_screen_height +120, (0,0,0),30)
            self.message(f"Total Deaths: {self.death_count}", half_screen_width,half_screen_height  +155, (0,0,0),30)
        else:
            self.Icon_walk()
            self.screen.blit(self.icon,(half_screen_width -90, half_screen_height -200))
            self.message("Predd any key to start the game",half_screen_width -30, half_screen_height +50, (0,0,0),30)
        pygame.display.flip()
        self.menu_events()
      
     #crear metodo para traer la posicion y dibujar  clase   
    def message (self ,menssage,x,y,colors,tamaño):
        font = pygame.font.Font("freesansbold.ttf" ,tamaño)
        text = font.render(menssage, True, colors)
        text_rect = text.get_rect()
        text_rect.center = (x,y)
        self.screen.blit(text, text_rect)
        
    def menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.play()
      
    #Tiempo record           
    def update_highest_score(self):
        if self.score.score > self.highest_score:
            self.highest_score = self.score.score
            
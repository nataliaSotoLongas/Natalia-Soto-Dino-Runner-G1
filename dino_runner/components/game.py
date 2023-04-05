import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.score import Score
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, CLOUD, START , GAMEOVER, RESET , ICON_1


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
        self.death = 0
        self.highest_score = 0 #Tiempo record 
        self.icon = ICON_1[0]
        self.step = 0

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
        self.score.reset()
        self.game_speed = 20
        
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
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self, self.on_death)  
        self.score.update(self) 
    
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        #llamamos las imagenes
        self.draw_clouds()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()
          
    #dibujar las imagenes
    def draw_clouds(self):
        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1020, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +1070, self.y_pos_bg -250))
        self.screen.blit(CLOUD, (image_width + self.x_pos_bg +2030, self.y_pos_bg -300))
    
    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
        
    def on_death(self):
        pygame.time.delay(500)
        self.playing = False
        self.death_count +=1
    
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
            self.update_highest_score()
            self.menssage("Game over. Press any key to reset", half_screen_width, half_screen_height +50)
            self.menssage(f"Your Score: {self.score.score}", half_screen_width, half_screen_height +85)
            self.menssage(f"Highest Score: {self.highest_score}", half_screen_width,half_screen_height +120)
            self.menssage(f"Total Deaths: {self.death_count}", half_screen_width,half_screen_height  +155)
        else:
            self.Icon_walk()
            self.screen.blit(self.icon,(half_screen_width -90, half_screen_height -200))
            self.menssage("Predd any key to start the game",half_screen_width -30, half_screen_height +50)
        pygame.display.flip()
        self.menu_events()
      
     #crear metodo para traer la posicion y dibujar    
    def menssage (self ,menssage,x,y):
        font = pygame.font.Font("freesansbold.ttf" ,30)
        text = font.render(menssage, True, (0,0,0))
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
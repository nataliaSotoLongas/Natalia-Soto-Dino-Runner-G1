import pygame
import os

# Global Constants
TITLE = "Chrome Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))
ICON_1 = [
    pygame.image.load(os.path.join(IMG_DIR, "DinoRun1icon.png")),
    pygame.image.load(os.path.join(IMG_DIR, "DinoRun2icon.png")),
]
DEAD = pygame.image.load(os.path.join(IMG_DIR,"Dino/DinoDead.png"))
RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUN_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer1.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

STONE =[
    pygame.image.load(os.path.join(IMG_DIR, "Stone/Stone1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Stone/Stone2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Stone/Stone3.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))
START = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoStart.png'))

GAMEOVER = pygame.image.load(os.path.join(IMG_DIR, 'Other/GameOver.png'))

MOON = pygame.image.load(os.path.join(IMG_DIR, 'Other/luna.png'))
SUN= pygame.image.load(os.path.join(IMG_DIR, 'Other/sol.png'))
STAR= pygame.image.load(os.path.join(IMG_DIR, 'Other/estrella.png'))

RESET= pygame.image.load(os.path.join(IMG_DIR, 'Other/Reset.png'))
DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
HEART_TYPE = "heart"
HAMMER_TYPE = "hammer"

HAMMER_LIST = [
    pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer1.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer2.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer3.png')),
    pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer4.png')),
]

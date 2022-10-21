import pygame
import pygame as pg

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 550
WIDTH_LINES = int(WINDOW_WIDTH / 50)
HEIGHT_LINES = int(WINDOW_HEIGHT / 25)

GRASS_IMAGE = pygame.image.load('grass.png')
SOLDIER_IMAGE = pygame.image.load('soldier.png')
SOLDIER_IMAGE = pg.transform.scale(SOLDIER_IMAGE, (((WINDOW_WIDTH / 50)*4), (WINDOW_HEIGHT / 25)*2))

BACKGROUND = (138, 201, 38)
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)

BLOCK_SIZE = (WINDOW_HEIGHT * WINDOW_WIDTH) / (50 * 25)

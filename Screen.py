# import Stack
import consts
import pygame
import random
import math

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
screen.fill(consts.BACKGROUND)
# for i in range(0, consts.WINDOW_WIDTH, 25):
#     pygame.draw.line(screen, consts.WHITE, (0, i), (consts.WINDOW_WIDTH, i))
#     pygame.draw.line(screen, consts.WHITE, (i, 0), (i, consts.WINDOW_HEIGHT))
pygame.display.update()


def draw_soldier():
    soldier_x = (consts.WINDOW_WIDTH / 50)
    soldier_y = (consts.WINDOW_HEIGHT / 25)
    # screen.blit(consts.SOLDIER_IMAGE, (soldier_x, soldier_y))
    screen.blit(consts.SOLDIER_IMAGE, (-consts.WIDTH_LINES, 0))
    pygame.display.update()


def draw_grid(color):
    blockSize_width = int(consts.WINDOW_WIDTH / 50)  # Set the size of the grid block
    blockSize_height = int(consts.WINDOW_HEIGHT / 25)
    for x in range(0, consts.WINDOW_WIDTH, blockSize_width):
        for y in range(0, consts.WINDOW_HEIGHT, blockSize_height):
            rect = pygame.Rect(x, y, blockSize_width, blockSize_height)
            pygame.draw.rect(screen, consts.WHITE, rect, 1)
    pygame.display.update()
    # for line in range(0, consts.WINDOW_WIDTH, consts.WIDTH_LINES):
    #     pygame.draw.line(screen, color, (line, 0), (line, consts.WINDOW_HEIGHT))
    # pygame.display.update()
    # for line in range(0, consts.WINDOW_HEIGHT, consts.HEIGHT_LINES):
    #     pygame.draw.line(screen, color, (0, line), (consts.WINDOW_WIDTH, line))
    # pygame.display.update()


def draw_bush():
    screen.blit(consts.GRASS_IMAGE, random.randrange(0, consts.WINDOW_HEIGHT), random.randrange(0, consts.WINDOW_WIDTH))

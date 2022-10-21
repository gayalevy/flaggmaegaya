import random
import pygame
import consts
import Screen

grid = []
mine_list = []


def create():
    spot = {
        "state": "EMPTY",
        "x": 0,
        "y": 0
    }
    blockSize_width = int(consts.WINDOW_WIDTH / 50)  # Set the size of the grid block
    blockSize_height = int(consts.WINDOW_HEIGHT / 25)
    for row in range(25):
        grid.append([spot])
        for col in range(49):
            grid[row].append(spot)
    for row in range(25):
        for col in range(49):
            for x in range(0, consts.WINDOW_WIDTH, blockSize_width):
                for y in range(0, consts.WINDOW_HEIGHT, blockSize_height):
                    box = grid[row][col]
                    box["x"] = x
                    box["y"] = y
    print(grid[1][0])
    create_mines()
    create_player()


def create_player():
    grid[3][0] = "PLAYER"
    grid[3][1] = "PLAYER"


def create_mines():
    extra = insert_mines()
    while True:
        if extra == 0:
            break
        extra = insert_mines(extra)


def insert_mines(mines=20):
    extra_mine = 0
    for mine in range(mines):
        row = random.randrange(4, 25)
        col = random.randrange(2, 47)
        if not check_if_empty(row, col):
            extra_mine += 1
    return extra_mine


def check_if_empty(row, col):
    check = 0
    for i in range(3):
        box = grid[row][col + i]
        if box["state"] == "EMPTY":
            check += 1
    if check == 3:
        mine_list.append([row, col])
        for i in range(3):
            box["state"] = "mine"
        return True
    return False

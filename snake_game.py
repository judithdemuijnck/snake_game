import random
import pygame
import tkinter as tk
from tkinter import messagebox

from Snake import Snake
from Cube import Cube

root = tk.Tk()
root.attributes("-topmost", True)
root.withdraw()

pygame.init()

width = 500
height = 500
rows = 20
starting_position = 10, 10

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0


def message_box(subject, content):
    messagebox.showinfo(subject, content)
    try:
        root.destory()
    except:
        pass


def draw_grid(width, rows, surface):
    cell_size = width // rows
    x = 0
    y = 0
    for line in range(rows):
        x += cell_size
        y += cell_size

        pygame.draw.line(surface, white, (x, 0), (x, width))
        pygame.draw.line(surface, white, (0, y), (width, y))


def redraw_window(surface):
    surface.fill(black)
    snake.draw(surface)
    snack.draw(surface)
    draw_grid(width, rows, surface)
    pygame.display.update()


def random_snack(rows, snake):
    positions = snake.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)

        if len([z for z in positions if z.position == (x, y)]) > 0:
            continue
        else:
            break

    return (x, y)


snake = Snake(red, starting_position)
snack = Cube(random_snack(rows, snake), color=green)


def app():
    global snack
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    while True:
        pygame.time.delay(50)
        clock.tick(10)
        snake.move()
        if snake.body[0].position == snack.position:
            snake.add_cube()
            snack = Cube(random_snack(rows, snake), color=green)

        for idx in range(len(snake.body)):
            # checking for collision
            if snake.body[idx].position in [z.position for z in snake.body[idx+1:]]:
                score = len(snake.body)
                print("Score:", len(snake.body))
                message_box("Game Over", f"Score: {score} \nPlay again")
                snake.reset(starting_position)
                break
        redraw_window(screen)


app()

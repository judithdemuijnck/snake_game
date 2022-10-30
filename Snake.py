from curses import KEY_RIGHT
import pygame
import sys
from Cube import Cube


class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, position):
        self.color = color
        self.head = Cube(position)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1

    def __match_pressed_key(self, keys):
        if keys[pygame.K_LEFT]:
            self.dirnx = -1
            self.dirny = 0
            self.turns[self.head.position[:]] = [
                self.dirnx, self.dirny]

        elif keys[pygame.K_RIGHT]:
            self.dirnx = 1
            self.dirny = 0
            self.turns[self.head.position[:]] = [
                self.dirnx, self.dirny]

        elif keys[pygame.K_UP]:
            self.dirnx = 0
            self.dirny = -1
            self.turns[self.head.position[:]] = [
                self.dirnx, self.dirny]

        elif keys[pygame.K_DOWN]:
            self.dirnx = 0
            self.dirny = 1
            self.turns[self.head.position[:]] = [
                self.dirnx, self.dirny]

    def __move_cube(self, cube):
        if cube.dirnx == -1 and cube.position[0] <= 0:
            cube.position = (cube.rows-1, cube.position[1])
        elif cube.dirnx == 1 and cube.position[0] >= cube.rows-1:
            cube.position = (0, cube.position[1])
        elif cube.dirny == 1 and cube.position[1] >= cube.rows-1:
            cube.position = (cube.position[0], 0)
        elif cube.dirny == -1 and cube.position[1] <= 0:
            cube.position = (cube.position[0], cube.rows-1)
        else:
            cube.move(cube.dirnx, cube.dirny)

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            keys = pygame.key.get_pressed()
            self.__match_pressed_key(keys)

        for idx, cube in enumerate(self.body):
            current_position = cube.position[:]
            if current_position in self.turns:
                turn = self.turns[current_position]
                cube.move(turn[0], turn[1])
                if idx == len(self.body)-1:
                    self.turns.pop(current_position)
            else:
                self.__move_cube(cube)

    def add_cube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        match dx, dy:
            case 1, 0:
                self.body.append(Cube((tail.position[0]-1, tail.position[1])))
            case -1, 0:
                self.body.append(Cube((tail.position[0]+1, tail.position[1])))
            case 0, 1:
                self.body.append(Cube((tail.position[0], tail.position[1]-1)))
            case 0, -1:
                self.body.append(Cube((tail.position[0], tail.position[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def reset(self, position):
        self.head = Cube(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def draw(self, surface):
        for idx, cube in enumerate(self.body):
            if idx == 0:
                # with eyes
                cube.draw(surface, True)
            else:
                # without eyes
                cube.draw(surface)

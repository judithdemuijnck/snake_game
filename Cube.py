import pygame

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0


def draw_eyes(size, pos1, pos2, surface):
    centre = size // 2
    radius = 3
    circleMiddle = (pos1*size+centre-radius, pos2*size+8)
    circleMiddle2 = (pos1*size+size-radius*2, pos2*size+8)
    pygame.draw.circle(surface, black, circleMiddle, radius)
    pygame.draw.circle(surface, black, circleMiddle2, radius)


class Cube(object):
    rows = 20
    width = 500

    def __init__(self, start, dirnx=1, dirny=0, color=red):
        self.position = start
        self.dirnx = dirnx
        self.dirny = dirny

        self.color = color

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.position = (
            self.position[0] + self.dirnx, self.position[1] + self.dirny)

    def draw(self, surface, eyes=False):
        gap = self.width // self.rows
        i = self.position[0]
        j = self.position[1]

        pygame.draw.rect(surface, self.color, (i*gap+1, j*gap+1, gap-2, gap-2))
        if eyes:
            draw_eyes(gap, i, j, surface)

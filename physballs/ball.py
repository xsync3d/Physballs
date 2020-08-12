import pygame

from graphics.render import screen

(width, height) = (1200, 720)
balls = []


class Ball:
    def __init__(self, pos: tuple, size, velocity: tuple, radius, color: tuple):
        self.pos = pos
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.size = size
        self.color = color
        self.thickness = size
        self.velocity = velocity
        self.future_pos = (0, 0)
        self.radius = radius

    def display(self):
        pygame.draw.circle(screen, self.color, (self.pos_x, self.pos_y), self.size, self.thickness)


def add_ball(position: tuple, size, velocity: tuple, color):
    nu_velocity = (velocity[0], velocity[1])
    balls.append(Ball(position, size, nu_velocity, int(size ** 1), color))
    print("Planet created at: {}".format(position))

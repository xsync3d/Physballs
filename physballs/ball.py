import pygame
import math
import random

from graphics.render import screen, width, height

# from physics.body_physics import add_vectors

balls = []


class Ball:
    def __init__(self, pos: tuple, size, color: tuple, mass):
        self.pos = pos
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.size = size
        self.color = color
        self.angle = 0
        self.velocity = 0
        self.mass = mass

    def display(self):
        pygame.draw.circle(screen, self.color, (int(self.pos_x), int(self.pos_y)), self.size, self.size)

    def _accelerate(self, vector):
        """ Change angle and speed by a given vector """
        # self.angle, self.velocity = add_vectors((self.angle, self.velocity, vector)
        pass

    def _attract(self, other):
        dx = (self.pos_x - other.pos_x)
        dy = (self.pos_y - other.pos_y)
        dist = math.hypot(dx, dy)

        theta = math.atan2(dy, dx)
        force = 0.2 * self.mass * other.mass / dist ** 2
        self.accelerate((theta - 0.5 * math.pi, force / self.mass))
        other.accelerate((theta + 0.5 * math.pi, force / other.mass))

    def move(self):
        self.pos_x += math.sin(self.angle) * self.velocity
        self.pos_y += math.cos(self.angle) * self.velocity

    def bounce(self):
        if self.pos_x > width - self.size:
            self.pos_x = 2 * (width - self.size) - self.pos_x
            self.angle = - self.angle
        elif self.pos_x < self.size:
            self.pos_x = 2 * self.size - self.pos_x
            self.angle = - self.angle
        if self.pos_y > height - self.size:
            self.pos_y = 2 * (height - self.size) - self.pos_y
            self.angle = math.pi - self.angle
        elif self.pos_y < self.size:
            self.pos_y = 2 * self.size - self.pos_y
            self.angle = math.pi - self.angle

    def __del__(self):
        print("[WARNING] Planet deleted at: {}".format(self.pos))


def add_ball(position: tuple, size, color):
    density = random.randint(1, 20)
    new_ball = Ball(position, size, color, density * size ** 2)
    new_ball.velocity = random.random()
    new_ball.angle = random.uniform(0, math.pi * 2)
    balls.append(new_ball)
    print("Planet created at: {}".format(position))

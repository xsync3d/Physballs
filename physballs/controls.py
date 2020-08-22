import pygame
import sys
import ball
import random
import graphics.render as render
from ball import Ball


# TODO: Make it so you can select, edit, delete planets


def check_event(running):
    for event in pygame.event.get():

        # Check for mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # TODO: make sure to implement mouse pos here
                ball.add_ball(pygame.mouse.get_pos(), random.randint(5, 80), render.rand_color())

        if event.type == pygame.QUIT:
            running = False

            sys.exit()

import pygame
import sys
import ball
import random
import graphics.render as render


# TODO make it so when a player clicks a planet is created in that position


def check_event(running):
    for event in pygame.event.get():

        # Check for mouse input
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # TODO: make sure to implement mouse pos here
                ball.add_ball(pygame.mouse.get_pos(), random.randint(1, 80), render.rand_color())

        if event.type == pygame.QUIT:
            running = False

            sys.exit()

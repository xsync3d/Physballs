#!/usr/bin/python
import pygame

from game.loop import loop
from graphics.render import midScreenX, midScreenY, screen


def open_window():
    bg_color = (0, 0, 0)
    pygame.init()
    pygame.display.set_caption("Physballs")
    pygame.mouse.set_pos((midScreenX, midScreenY))
    loop(screen, bg_color, True)


open_window()

#!/usr/bin/python
import pygame

from game.loop import loop
from graphics.render import midScreenX, midScreenY, screen
from graphics.console import print_ascii_title

print_ascii_title()


def open_window():
    bg_color = (0, 0, 0)
    pygame.init()
    pygame.display.set_caption("Physballs")
    pygame.mouse.set_pos((midScreenX, midScreenY))
    loop(screen, bg_color, True)


open_window()

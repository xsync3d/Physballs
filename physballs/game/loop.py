import pygame
import controls
from ball import balls


def loop(a_screen, bg_color, running):
    # Game loop starts here.
    while running:
        # Watch for keyboard and mouse events.
        controls.check_event(running)

        # fill
        a_screen.fill(bg_color)
        # draw
        for ball in balls:
            ball.display()
        # display
        pygame.display.flip()

    pygame.quit()

import pygame
import controls


def loop(a_screen, bg_color, running):
    # Game loop starts here.
    while running:
        # Watch for keyboard and mouse events.
        controls.check_event(running)

        # fill
        a_screen.fill(bg_color)
        # draw

        # display
        pygame.display.flip()

    pygame.quit()

import pygame
import controls
import multiprocessing
from ball import balls
from physics import body_physics


def loop(a_screen, bg_color, running):
    # Game loop starts here.
    while running:
        # Watch for input, keyboard and mouse events.
        controls.check_event(running)
        # fill
        a_screen.fill(bg_color)
        # draw
        for i, ball in enumerate(balls):
            ball.move()
            ball.bounce()
            for ball2 in balls[i + 1:]:
                body_physics.collide(ball, ball2)
            ball.display()

        # display
        pygame.display.flip()

    pygame.quit()

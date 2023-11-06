import pygame
from pygame.locals import *

from Ball import Ball
from Bar import Bar

from constants import BACKGROUND_COLOR, BALL_COLOR, BALL_RADIUS, BAR_COLOR, BAR_HEIGHT, BAR_WIDTH, HEIGHT, WIDTH

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball Game")

ball = Ball()
bar = Bar()

bounce_sound = pygame.mixer.Sound('bounce.mp3')

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bar.move_left()
    if keys[pygame.K_RIGHT]:
        bar.move_right()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if ball.bounce():
        bounce_sound.play()

    if ball.collides_with(bar):
        bounce_sound.play()

    if ball.position[1] >= HEIGHT - BALL_RADIUS:
        running = False

    pygame.draw.circle(screen, BALL_COLOR, ball.position, BALL_RADIUS)
    pygame.draw.rect(screen, BAR_COLOR, (bar.position, HEIGHT - BAR_HEIGHT, BAR_WIDTH, BAR_HEIGHT))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
pygame.mixer.quit()

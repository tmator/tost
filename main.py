import os, sys
import pygame
from pygame import gfxdraw
from pygame.locals import *

pygame.init()

# Set the height and width of the screen
size = (800, 480)
#screen = pygame.display.set_mode(size,)
screen = pygame.display.set_mode(size,pygame.FULLSCREEN)

done = False
clock = pygame.time.Clock()

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (51,218,255)

mood = 0

def display_head(mood):
    #0 normal, 1 happy, 2 sad, 3 asking, 4 bored
    if mood == 0: #normal
        pygame.gfxdraw.filled_ellipse(screen, 200,175,50,75, BLUE)
        pygame.gfxdraw.filled_ellipse(screen, 600,175,50,75, BLUE)
        pygame.gfxdraw.box(screen,[200,330,20,30],BLUE)
        pygame.gfxdraw.box(screen,[580,330,20,30],BLUE)
        pygame.gfxdraw.box(screen,[200,360,400,20],BLUE)
    elif mood == 1: #happy
        pygame.gfxdraw.filled_ellipse(screen, 200,175,50,75, BLUE)
        pygame.gfxdraw.filled_ellipse(screen, 600,175,50,75, BLUE)
        pygame.gfxdraw.box(screen,[200,330,20,30],BLUE)
        pygame.gfxdraw.box(screen,[580,330,20,30],BLUE)
        pygame.gfxdraw.box(screen,[200,360,400,20],BLUE)
    elif mood == 2: #sad
        pygame.gfxdraw.filled_ellipse(screen, 200,175,50,50, BLUE)
        pygame.gfxdraw.filled_ellipse(screen, 600,175,50,50, BLUE)
        pygame.gfxdraw.box(screen,[200,380,20,30],BLUE)
        pygame.gfxdraw.box(screen,[580,380,20,30],BLUE)
        pygame.gfxdraw.box(screen,[200,360,400,20],BLUE) #line
    elif mood == 3: #asking
        pygame.gfxdraw.filled_ellipse(screen, 200,175,50,75, BLUE)
        pygame.gfxdraw.filled_ellipse(screen, 600,215,50,35, BLUE)
        pygame.gfxdraw.box(screen,[200,360,400,20],BLUE)
    elif mood == 4: #bored ok
        pygame.gfxdraw.filled_ellipse(screen, 200,175,50,75, BLUE)
        pygame.gfxdraw.filled_ellipse(screen, 600,175,50,75, BLUE)
        pygame.gfxdraw.box(screen,[200,360,400,20],BLUE)
    return

while not done:
    screen.fill(BLACK)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            done = True  
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                done = True  
            elif event.key == K_a:
                mood=0
            elif event.key == K_b:
                mood=1
            elif event.key == K_c:
                mood=2
            elif event.key == K_d:
                mood=3
            elif event.key == K_e:
                mood=4
             



    display_head(mood)
    #ellipse opened eyes OK
    #pygame.gfxdraw.filled_ellipse(screen, 200,175,50,75, BLUE)
    #pygame.gfxdraw.filled_ellipse(screen, 600,175,50,75, BLUE)

    #mouth line OK
    #pygame.gfxdraw.box(screen,[200,360,400,20],BLUE)

    #mouth ask OK
    #pygame.gfxdraw.box(screen,[200,360,400,20],BLUE)

    #mouth smile OK
    #pygame.gfxdraw.box(screen,[200,330,20,30],BLUE)
    #pygame.gfxdraw.box(screen,[480,330,20,30],BLUE)
    #pygame.gfxdraw.box(screen,[200,360,400,20],BLUE)

    #ellipse eyes asking OK
    #pygame.gfxdraw.filled_ellipse(screen, 200,175,50,75, BLUE)
    #pygame.gfxdraw.filled_ellipse(screen, 600,215,50,35, BLUE)
    
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()

